from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str

class LoginRequest(SQLModel):
    username: str
    password: str

sqlite_url = "sqlite:///:memory:"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        user_exists = session.exec(select(User).where(User.username == "admin")).first()
        if not user_exists:
            sample_user = User(username="admin", password="password123")
            session.add(sample_user)
            session.commit()

app = FastAPI(title="Login API Minimalista")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

def get_session():
    with Session(engine) as session:
        yield session

@app.post("/login")
def login(login_data: LoginRequest, session: Session = Depends(get_session)):
    statement = select(User).where(User.username == login_data.username)
    user = session.exec(statement).first()

    if not user or user.password != login_data.password:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return {"message": "Login exitoso", "user": user.username}
  
