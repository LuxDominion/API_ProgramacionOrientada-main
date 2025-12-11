import re

def validar_nombre(nombre):
    """Valida que el nombre no esté vacío"""
    if not nombre or not nombre.strip():
        print("El nombre no puede estar vacío.")
        return False
    return True

def validar_correo(correo):
    """Valida el formato del correo electrónico"""
    if not correo or '@' not in correo: 
        print("Correo inválido.")
        return False
    return True

def validar_contrasena(contrasena):
    """Valida que la contraseña tenga al menos 6 caracteres"""
    if len(contrasena) < 6:
        print("La contraseña debe tener al menos 6 caracteres.")
        return False
    return True

def validar_confirmacion_contrasena(contrasena, confirmacion):
    """Valida que las contraseñas coincidan"""
    if contrasena != confirmacion:
        print("Las contraseñas no coinciden.")
        return False
    return True
