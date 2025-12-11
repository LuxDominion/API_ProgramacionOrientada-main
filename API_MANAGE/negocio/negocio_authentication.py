"""
Módulo de Autenticación - Gestión de registro y login
Incluye encriptación segura de contraseñas
"""

import bcrypt
from modelos import Usuario
from datos import insertar_objeto, obtener_listado_objetos
from datos.conexion import sesion


def encriptar_contrasena(contrasena: str) -> tuple:
    """
    Encripta una contraseña usando bcrypt.
    Retorna una tupla (hash, salt)
    
    Args:
        contrasena (str): Contraseña a encriptar
    
    Returns:
        tuple: (hash_contrasena, salt)
    """
    try:
        salt = bcrypt.gensalt(rounds=12)
        hash_contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), salt)
        return hash_contrasena.decode('utf-8'), salt.decode('utf-8')
    except Exception as e:
        print(f"Error al encriptar contraseña: {e}")
        return None, None


def verificar_contrasena(contrasena: str, hash_almacenado: str) -> bool:
    """
    Verifica si una contraseña coincide con su hash.
    
    Args:
        contrasena (str): Contraseña a verificar
        hash_almacenado (str): Hash almacenado en BD
    
    Returns:
        bool: True si las contraseñas coinciden, False si no
    """
    try:
        return bcrypt.checkpw(contrasena.encode('utf-8'), hash_almacenado.encode('utf-8'))
    except Exception as e:
        print(f"Error al verificar contraseña: {e}")
        return False


def registrar_usuario(nombre: str, correo: str, contrasena: str) -> bool:
    """
    Registra un nuevo usuario en la BD con contraseña encriptada.
    
    Args:
        nombre (str): Nombre del usuario
        correo (str): Correo electrónico
        contrasena (str): Contraseña sin encriptar
    
    Returns:
        bool: True si el registro fue exitoso, False si no
    """
    try:
        usuario_existente = sesion.query(Usuario).filter_by(correo=correo).first()
        if usuario_existente:
            print("El correo ya está registrado.")
            return False
        
        hash_contrasena, salt = encriptar_contrasena(contrasena)
        if not hash_contrasena:
            return False
        
        nuevo_usuario = Usuario(
            nombre=nombre,
            correo=correo,
            contrasena_hash=hash_contrasena,
            contrasena_salt=salt
        )
        
        id_usuario = insertar_objeto(nuevo_usuario)
        print(f"Usuario registrado exitosamente con ID: {id_usuario}")
        return True
    
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        sesion.rollback()
        return False


def autenticar_usuario(correo: str, contrasena: str) -> Usuario:
    """
    Autentica a un usuario verificando su correo y contraseña.
    
    Args:
        correo (str): Correo electrónico del usuario
        contrasena (str): Contraseña sin encriptar
    
    Returns:
        Usuario: Objeto Usuario si la autenticación es correcta, None si no
    """
    try:
        usuario = sesion.query(Usuario).filter_by(correo=correo).first()
        
        if not usuario:
            print("Usuario no encontrado.")
            return None
        
        if verificar_contrasena(contrasena, usuario.contrasena_hash):
            print(f"Autenticación exitosa.")
            return usuario
        else:
            print("Contraseña incorrecta.")
            return None
    
    except Exception as e:
        print(f"Error al autenticar usuario: {e}")
        return None


def listar_usuarios_registrados():
    """
    Lista todos los usuarios registrados en la BD.
    
    Returns:
        list: Lista de objetos Usuario
    """
    try:
        usuarios = obtener_listado_objetos(Usuario)
        return usuarios if usuarios else []
    except Exception as e:
        print(f"Error al listar usuarios: {e}")
        return []
