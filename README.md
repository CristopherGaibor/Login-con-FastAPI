# Login-con-FastAPI


Este taller es una implementación mínima de un sistema de autenticación utilizando FastAPI y SQLModel con una base de datos SQLite en memoria.

## Instalación

1. Clonar el repositorio.
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

## Login exitoso:
{
  "message": "Login exitoso",
  "user": "admin"
}


## Login fallido:
{
  "username": "admin",
  "password": "wrongpassword"
}

## Login sin autorización:
{
  "detail": "Credenciales incorrectas"
}


