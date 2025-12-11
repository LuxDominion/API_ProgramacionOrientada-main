# Lógica de Usuarios

from prettytable import PrettyTable
import requests
from modelos import User
from datos import insertar_objeto, obtener_listado_objetos
from .negocio_geos import crear_geolocalizacion
from .negocio_addresses import crear_direccion
from .negocio_companies import crear_compania

def obtener_data_usuarios(url):
    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            usuarios = respuesta.json()
            contador = 0
            
            for user in usuarios:
                try:
                    usuarios_existentes = obtener_listado_objetos(User)
                    ids_existentes = [u.id for u in usuarios_existentes] if usuarios_existentes else []
                    
                    if user['id'] in ids_existentes:
                        continue
                    
                    id_geo = crear_geolocalizacion(
                        user['address']['geo']['lat'],
                        user['address']['geo']['lng']
                    )
                    
                    id_direccion = crear_direccion(
                        user['address']['street'],
                        user['address']['suite'],
                        user['address']['city'],
                        user['address']['zipcode'],
                        id_geo
                    )
                    
                    id_compania = crear_compania(
                        user['company']['name'],
                        user['company']['catchPhrase'],
                        user['company']['bs']
                    )
                    
                    crear_user_db(
                        user['name'],
                        user['username'],
                        user['email'],
                        user['phone'],
                        user['website'],
                        id_direccion,
                        id_compania
                    )
                    contador += 1
                except Exception as e:
                    continue
            
            print(f"Se descargaron {contador} usuarios")
        else:
            print(f"Error: {respuesta.status_code}")
    
    except Exception as e:
        print(f"Error: {e}")

def listado_users_api(url):
    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            usuarios = respuesta.json()
            
            tabla = PrettyTable()
            tabla.field_names = ['ID', 'Nombre', 'Usuario', 'Correo', 'Teléfono', 'Web']
            
            for user in usuarios:
                tabla.add_row([
                    user['id'],
                    user['name'],
                    user['username'],
                    user['email'],
                    user['phone'],
                    user['website']
                ])
            
            print(tabla)
        else:
            print("No se pudo conectar a la API")
    
    except Exception as e:
        print(f"Error: {e}")

def listado_users_db():
    try:
        usuarios = obtener_listado_objetos(User)
        
        if usuarios:
            tabla = PrettyTable()
            tabla.field_names = ['ID', 'Nombre', 'Usuario', 'Correo', 'Teléfono', 'Web']
            
            for usuario in usuarios:
                tabla.add_row([
                    usuario.id,
                    usuario.name,
                    usuario.username,
                    usuario.email,
                    usuario.phone,
                    usuario.website
                ])
            
            print(tabla)
        else:
            print("No hay usuarios guardados")
    
    except Exception as e:
        print(f"Error: {e}")

def crear_user_db(nombre, nombre_usuario, correo, telefono, sitio_web, id_direccion, id_compania):
    try:
        nuevo_usuario = User(
            name=nombre,
            username=nombre_usuario,
            email=correo,
            phone=telefono,
            website=sitio_web,
            addressId=id_direccion,
            companyId=id_compania
        )
        
        id_usuario = insertar_objeto(nuevo_usuario)
        return id_usuario
    
    except Exception as e:
        print(f"Error al guardar el usuario: {e}")
        return None
