import sys
import os
from datos.conexion import crear_tablas, sesion
from modelos.modelos import Usuario
from negocio.negocio_authentication import registrar_usuario, autenticar_usuario
from servicios.api_service import obtener_recurso_api
from auxiliares.api_data import url_users

def test_db_and_auth():
    print("--- Pruebas de BD y Autenticación ---")
    crear_tablas()
    
    test_email = "test_verification@example.com"
    existing = sesion.query(Usuario).filter_by(correo=test_email).first()
    if existing:
        sesion.delete(existing)
        sesion.commit()
        print("Usuario de prueba anterior eliminado.")

    print("Registrando usuario...")
    success = registrar_usuario("Usuario Prueba", test_email, "password123")
    if success:
        print("Registro exitoso.")
    else:
        print("Error en el registro.")
        return

    print("Iniciando sesión...")
    user = autenticar_usuario(test_email, "password123")
    if user:
        print(f"Inicio de sesión exitoso para {user.nombre}.")
    else:
        print("Error al iniciar sesión.")

    print("Intentando iniciar sesión con contraseña incorrecta...")
    user_wrong = autenticar_usuario(test_email, "wrongpass")
    if not user_wrong:
        print("Inicio de sesión falló como se esperaba con contraseña incorrecta.")
    else:
        print("Inicio de sesión con contraseña incorrecta (inesperado).")

def test_api_service():
    print("\n--- Pruebas del Servicio de API (GET) ---")
    import requests
    try:
        response = requests.get(url_users)
        if response.status_code == 200:
            print(f"Conexión a {url_users} exitosa.")
        else:
            print(f"Error en la conexión: {response.status_code}")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":
    test_db_and_auth()
    test_api_service()
