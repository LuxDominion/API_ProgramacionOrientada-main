"""
Aplicación Principal - API_MANAGE
Gestión de usuarios, posts y comentarios desde JSONPlaceholder
Autor: Sistema de API Management
Fecha: Diciembre 2025
"""

import sys
import os
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    from datos.conexion import crear_tablas
    
    crear_tablas()
    
    from auxiliares.api_data import url_users, url_posts, url_comments
    from negocio import (
        obtener_data_usuarios, listado_users_db, listado_users_api,
        obtener_data_publicaciones, listado_publicaciones,
        obtener_data_comentarios, listado_comentarios,
        registrar_usuario, autenticar_usuario
    )
    from servicios.api_service import (
        crear_recurso_api, actualizar_recurso_api, 
        eliminar_recurso_api, obtener_recurso_api
    )
except ImportError as e:
    print(f" Error de importación: {e}")
    print(" Por favor, instale las dependencias:")
    print("  pip install -r requirements.txt")
    sys.exit(1)


class MenuPrincipal:
    """Clase que gestiona el menú principal de la aplicación"""
    
    def __init__(self):
        self.usuario_autenticado = None
        self.url_users = url_users
        self.url_posts = url_posts
        self.url_comments = url_comments
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu_autenticacion(self):
        """Muestra el menú de autenticación"""
        self.limpiar_pantalla()
        print("\nSISTEMA DE AUTENTICACIÓN - API_MANAGE")
        print("-" * 40)
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        print("-" * 40)
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal después de autenticación"""
        self.limpiar_pantalla()
        print(f"\nAPI_MANAGE - Usuario: {self.usuario_autenticado}")
        print("-" * 40)
        print("GESTION DE DATOS:")
        print("1. Obtener usuarios desde API")
        print("2. Ver usuarios en BD")
        print("3. Ver usuarios en API")
        print("4. Obtener publicaciones desde API")
        print("5. Ver publicaciones")
        print("6. Obtener comentarios desde API")
        print("7. Ver comentarios")
        print("\nOPERACIONES CRUD:")
        print("8. Crear recurso")
        print("9. Actualizar recurso")
        print("10. Eliminar recurso")
        print("11. Obtener recurso")
        print("\nOTRAS OPCIONES:")
        print("12. Cerrar sesion")
        print("0. Salir")
        print("-" * 40)
    
    def registrar(self):
        """Gestiona el registro de nuevos usuarios"""
        self.limpiar_pantalla()
        print("\nREGISTRO DE NUEVO USUARIO")
        print("-" * 40)
        
        try:
            nombre = input("Nombre completo: ").strip()
            if not nombre:
                print("[ERROR] El nombre no puede estar vacío.")
                input("Enter para continuar...")
                return False
            
            correo = input("Correo electrónico: ").strip()
            if not correo or '@' not in correo:
                print("[ERROR] Correo inválido.")
                input("Enter para continuar...")
                return False
            
            contrasena = input("Contraseña (mín 6 caracteres): ").strip()
            if len(contrasena) < 6:
                print("[ERROR] La contraseña debe tener al menos 6 caracteres.")
                input("Enter para continuar...")
                return False
            
            contrasena_confirm = input("Confirmar contraseña: ").strip()
            if contrasena != contrasena_confirm:
                print("[ERROR] Las contraseñas no coinciden.")
                input("Enter para continuar...")
                return False
            
            if registrar_usuario(nombre, correo, contrasena):
                print("[OK] Registro exitoso. Ya puede iniciar sesión.")
                input("Enter para continuar...")
                return True
            else:
                print("[ERROR] El correo ya está registrado.")
                input("Enter para continuar...")
                return False
        
        except Exception as e:
            print(f"[ERROR] {e}")
            input("Enter para continuar...")
            return False
    
    def login(self):
        """Gestiona el inicio de sesión"""
        self.limpiar_pantalla()
        print("\nINICIAR SESIÓN")
        print("-" * 40)
        
        try:
            correo = input("Correo electrónico: ").strip()
            contrasena = input("Contraseña: ").strip()
            
            usuario = autenticar_usuario(correo, contrasena)
            if usuario:
                self.usuario_autenticado = usuario.nombre
                print("[OK] Bienvenido, {usuario.nombre}!")
                input("Enter para continuar...")
                return True
            else:
                print("[ERROR] Correo o contraseña incorrectos.")
                input("Enter para continuar...")
                return False
        
        except Exception as e:
            print(f"[ERROR] {e}")
            input("Enter para continuar...")
            return False
    
    def obtener_usuarios_api(self):
        """Obtiene usuarios desde la API y los guarda en BD"""
        self.limpiar_pantalla()
        print("\nOBTENER USUARIOS DESDE API")
        print("-" * 40)
        
        try:
            print("Descargando usuarios...")
            obtener_data_usuarios(self.url_users)
            print("[OK] Usuarios descargados y guardados.")
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def ver_usuarios_bd(self):
        """Muestra usuarios almacenados en la BD"""
        self.limpiar_pantalla()
        print("\nUSUARIOS EN BASE DE DATOS")
        print("-" * 40)
        
        try:
            listado_users_db()
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def ver_usuarios_api(self):
        """Muestra usuarios desde la API"""
        self.limpiar_pantalla()
        print("\nUSUARIOS DESDE API")
        print("-" * 40)
        
        try:
            listado_users_api(self.url_users)
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def obtener_publicaciones_api(self):
        """Obtiene publicaciones desde la API"""
        self.limpiar_pantalla()
        print("\nOBTENER PUBLICACIONES DESDE API")
        print("-" * 40)
        
        try:
            print("Descargando publicaciones...")
            obtener_data_publicaciones(self.url_posts)
            print("[OK] Publicaciones descargadas y guardadas.")
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def ver_publicaciones(self):
        """Muestra publicaciones almacenadas"""
        self.limpiar_pantalla()
        print("\nPUBLICACIONES EN BASE DE DATOS")
        print("-" * 40)
        
        try:
            listado_publicaciones()
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def obtener_comentarios_api(self):
        """Obtiene comentarios desde la API"""
        self.limpiar_pantalla()
        print("\nOBTENER COMENTARIOS DESDE API")
        print("-" * 40)
        
        try:
            print("Descargando comentarios...")
            obtener_data_comentarios(self.url_comments)
            print("[OK] Comentarios descargados y guardados.")
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def ver_comentarios(self):
        """Muestra comentarios almacenados"""
        self.limpiar_pantalla()
        print("\nCOMENTARIOS EN BASE DE DATOS")
        print("-" * 40)
        
        try:
            listado_comentarios()
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def crear_recurso(self):
        """Crea un nuevo recurso mediante POST"""
        self.limpiar_pantalla()
        print("\nCREAR RECURSO")
        print("-" * 40)
        print("1. Usuario")
        print("2. Publicacion")
        print("3. Comentario")
        
        try:
            opcion = input("Seleccione: ").strip()
            
            if opcion == "1":
                crear_recurso_api(self.url_users, "users")
            elif opcion == "2":
                crear_recurso_api(self.url_posts, "posts")
            elif opcion == "3":
                crear_recurso_api(self.url_comments, "comments")
            else:
                print("[ERROR] Opcion invalida.")
        
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def actualizar_recurso(self):
        """Actualiza un recurso mediante PUT"""
        self.limpiar_pantalla()
        print("\nACTUALIZAR RECURSO")
        print("-" * 40)
        print("1. Usuario")
        print("2. Publicacion")
        print("3. Comentario")
        
        try:
            opcion = input("Seleccione: ").strip()
            
            if opcion == "1":
                actualizar_recurso_api(self.url_users, "users")
            elif opcion == "2":
                actualizar_recurso_api(self.url_posts, "posts")
            elif opcion == "3":
                actualizar_recurso_api(self.url_comments, "comments")
            else:
                print("[ERROR] Opcion invalida.")
        
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def eliminar_recurso(self):
        """Elimina un recurso mediante DELETE"""
        self.limpiar_pantalla()
        print("\nELIMINAR RECURSO")
        print("-" * 40)
        print("1. Usuario")
        print("2. Publicacion")
        print("3. Comentario")
        
        try:
            opcion = input("Seleccione: ").strip()
            
            if opcion == "1":
                eliminar_recurso_api(self.url_users, "users")
            elif opcion == "2":
                eliminar_recurso_api(self.url_posts, "posts")
            elif opcion == "3":
                eliminar_recurso_api(self.url_comments, "comments")
            else:
                print("[ERROR] Opcion invalida.")
        
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def obtener_recurso(self):
        """Obtiene un recurso específico mediante GET"""
        self.limpiar_pantalla()
        print("\nOBTENER RECURSO")
        print("-" * 40)
        print("1. Usuario")
        print("2. Publicacion")
        print("3. Comentario")
        
        try:
            opcion = input("Seleccione: ").strip()
            
            if opcion == "1":
                obtener_recurso_api(self.url_users, "users")
            elif opcion == "2":
                obtener_recurso_api(self.url_posts, "posts")
            elif opcion == "3":
                obtener_recurso_api(self.url_comments, "comments")
            else:
                print("[ERROR] Opcion invalida.")
        
        except Exception as e:
            print(f"[ERROR] {e}")
        
        input("Enter para continuar...")
    
    def ejecutar(self):
        """Ejecuta el flujo principal de la aplicación"""
        while not self.usuario_autenticado:
            self.mostrar_menu_autenticacion()
            opcion = input("Seleccione opción: ").strip()
            
            if opcion == "1":
                self.registrar()
            elif opcion == "2":
                if self.login():
                    break
            elif opcion == "3":
                print("\n👋 ¡Hasta luego!")
                sys.exit(0)
            else:
                print("[ERROR] Opción inválida.")
                input("Presione Enter para continuar...")
        
        while True:
            self.mostrar_menu_principal()
            opcion = input("Seleccione opción: ").strip()
            
            if opcion == "1":
                self.obtener_usuarios_api()
            elif opcion == "2":
                self.ver_usuarios_bd()
            elif opcion == "3":
                self.ver_usuarios_api()
            elif opcion == "4":
                self.obtener_publicaciones_api()
            elif opcion == "5":
                self.ver_publicaciones()
            elif opcion == "6":
                self.obtener_comentarios_api()
            elif opcion == "7":
                self.ver_comentarios()
            elif opcion == "8":
                self.crear_recurso()
            elif opcion == "9":
                self.actualizar_recurso()
            elif opcion == "10":
                self.eliminar_recurso()
            elif opcion == "11":
                self.obtener_recurso()
            elif opcion == "12":
                self.usuario_autenticado = None
                print("\n[OK] Sesión cerrada.")
                input("Presione Enter para continuar...")
                break
            elif opcion == "0":
                print("\n👋 ¡Hasta luego!")
                sys.exit(0)
            else:
                print("[ERROR] Opción inválida.")
                input("Presione Enter para continuar...")


if __name__ == "__main__":
    crear_tablas()
    menu = MenuPrincipal()
    menu.ejecutar()
