import sys
import os
from datos.conexion import crear_tablas, sesion
from modelos.modelos import Usuario
from negocio.negocio_authentication import registrar_usuario, autenticar_usuario
from servicios.api_service import obtener_recurso_api
from auxiliares.api_data import url_users

def test_db_and_auth():
    print("--- Testing DB and Auth ---")
    crear_tablas()
    
    test_email = "test_verification@example.com"
    existing = sesion.query(Usuario).filter_by(correo=test_email).first()
    if existing:
        sesion.delete(existing)
        sesion.commit()
        print("Cleaned up previous test user.")

    print("Registering user...")
    success = registrar_usuario("Test User", test_email, "password123")
    if success:
        print("[OK] Registration successful.")
    else:
        print("[ERROR] Registration failed.")
        return

    print("Logging in...")
    user = autenticar_usuario(test_email, "password123")
    if user:
        print(f"[OK] Login successful for {user.nombre}.")
    else:
        print("[ERROR] Login failed.")

    print("Logging in with wrong password...")
    user_wrong = autenticar_usuario(test_email, "wrongpass")
    if not user_wrong:
        print("[OK] Login failed as expected with wrong password.")
    else:
        print("[ERROR] Login succeeded with wrong password (unexpected).")

def test_api_service():
    print("\n--- Testing API Service (GET) ---")
    import requests
    try:
        response = requests.get(url_users)
        if response.status_code == 200:
            print(f"[OK] API connectivity to {url_users} successful.")
        else:
            print(f"[ERROR] API connectivity failed: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] API connectivity error: {e}")

if __name__ == "__main__":
    test_db_and_auth()
    test_api_service()
