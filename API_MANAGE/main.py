import os
from datos.conexion import crear_tablas
from auxiliares.api_data import url_users, url_posts, url_comments
from negocio import (
    obtener_data_usuarios, listado_users_db, listado_users_api,
    obtener_data_publicaciones, listado_publicaciones,
    obtener_data_comentarios, listado_comentarios,
    registrar_usuario, autenticar_usuario
)

usuario_logueado = None
url_base_users = url_users
url_base_posts = url_posts
url_base_comments = url_comments

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("\nPresione Enter para continuar...")

def mostrar_menu_login():
    limpiar()
    print("\n" + "="*40)
    print("SISTEMA DE AUTENTICACIÓN")
    print("="*40)
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    print("="*40)
    return input("Seleccione opción: ").strip()

def mostrar_menu_principal(usuario):
    limpiar()
    print("\n" + "="*40)
    print(f"Bienvenido: {usuario}")
    print("="*40)
    print("1. Ver usuarios de API")
    print("2. Ver usuarios guardados")
    print("3. Descargar usuarios de API")
    print("4. Ver publicaciones")
    print("5. Descargar publicaciones")
    print("6. Ver comentarios")
    print("7. Descargar comentarios")
    print("8. Cerrar sesión")
    print("0. Salir")
    print("="*40)
    return input("Seleccione opción: ").strip()

def registrar_nuevo_usuario():
    limpiar()
    print("\nREGISTRO DE NUEVO USUARIO")
    print("-"*40)
    
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío")
        pausa()
        return False
    
    correo = input("Correo: ").strip()
    if not correo or '@' not in correo:
        print("Correo inválido")
        pausa()
        return False
    
    contrasena = input("Contraseña (mín 6 caracteres): ").strip()
    if len(contrasena) < 6:
        print("Mínimo 6 caracteres")
        pausa()
        return False
    
    contrasena_confirmar = input("Confirmar contraseña: ").strip()
    if contrasena != contrasena_confirmar:
        print("Las contraseñas no coinciden")
        pausa()
        return False
    
    if registrar_usuario(nombre, correo, contrasena):
        print("Registro exitoso")
        pausa()
        return True
    else:
        print("El correo ya está registrado")
        pausa()
        return False

def login_usuario():
    limpiar()
    print("\nINICIAR SESIÓN")
    print("-"*40)
    
    correo = input("Correo: ").strip()
    contrasena = input("Contraseña: ").strip()
    
    usuario = autenticar_usuario(correo, contrasena)
    if usuario:
        print(f"¡Bienvenido {usuario.nombre}!")
        pausa()
        return usuario.nombre
    else:
        print("Correo o contraseña incorrectos")
        pausa()
        return None

def opcion_ver_usuarios_api():
    limpiar()
    print("\nUSUARIOS DE LA API")
    print("-"*40)
    listado_users_api(url_base_users)
    pausa()

def opcion_ver_usuarios_bd():
    limpiar()
    print("\nUSUARIOS GUARDADOS")
    print("-"*40)
    listado_users_db()
    pausa()

def opcion_descargar_usuarios():
    limpiar()
    print("\nDESCARANDO USUARIOS...")
    print("-"*40)
    obtener_data_usuarios(url_base_users)
    pausa()

def opcion_ver_publicaciones():
    limpiar()
    print("\nPUBLICACIONES")
    print("-"*40)
    listado_publicaciones()
    pausa()

def opcion_descargar_publicaciones():
    limpiar()
    print("\nDESCARANDO PUBLICACIONES...")
    print("-"*40)
    obtener_data_publicaciones(url_base_posts)
    pausa()

def opcion_ver_comentarios():
    limpiar()
    print("\nCOMENTARIOS")
    print("-"*40)
    listado_comentarios()
    pausa()

def opcion_descargar_comentarios():
    limpiar()
    print("\nDESCARANDO COMENTARIOS...")
    print("-"*40)
    obtener_data_comentarios(url_base_comments)
    pausa()

def main():
    global usuario_logueado
    
    crear_tablas()
    
    while not usuario_logueado:
        opcion = mostrar_menu_login()
        
        if opcion == "1":
            registrar_nuevo_usuario()
        elif opcion == "2":
            usuario_logueado = login_usuario()
        elif opcion == "3":
            print("\n¡Hasta luego!")
            return
        else:
            print("Opción inválida")
            input("Presione Enter...")
    
    while True:
        opcion = mostrar_menu_principal(usuario_logueado)
        
        if opcion == "1":
            opcion_ver_usuarios_api()
        elif opcion == "2":
            opcion_ver_usuarios_bd()
        elif opcion == "3":
            opcion_descargar_usuarios()
        elif opcion == "4":
            opcion_ver_publicaciones()
        elif opcion == "5":
            opcion_descargar_publicaciones()
        elif opcion == "6":
            opcion_ver_comentarios()
        elif opcion == "7":
            opcion_descargar_comentarios()
        elif opcion == "8":
            usuario_logueado = None
            print("\nSesión cerrada")
            pausa()
            break
        elif opcion == "0":
            print("\n¡Hasta luego!")
            return
        else:
            print("Opción inválida")
            input("Presione Enter...")

if __name__ == "__main__":
    main()

