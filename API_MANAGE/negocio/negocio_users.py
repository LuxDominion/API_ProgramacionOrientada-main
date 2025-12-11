from prettytable import PrettyTable
import requests
import json
from modelos import User
from datos import insertar_objeto, obtener_listado_objetos
from .negocio_geos import crear_geolocalizacion
from .negocio_addresses import crear_direccion
from .negocio_companies import crear_compania
from decouple import config


def obtener_data_usuarios(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data...")
        usuarios = respuesta.json()
        contador = 0
        for user in usuarios:
            try:
                usuario_existente = obtener_listado_objetos(User)
                ids_existentes = [u.id for u in usuario_existente] if usuario_existente else []
                
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
        
        print(f"[OK] {contador} usuarios cargados.")

    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")

def listado_users_api(url):
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = [
        'N°', 'Nombre', 'Usuario', 'Correo', 'Teléfono', 'Sitio Web']
    
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data...")
        usuarios = respuesta.json()
        for user in usuarios:
            tabla_usuarios.add_row(
                [user['id'],
                user['name'],
                user['username'],
                user['email'],
                user['phone'],
                user['website']])
        print(tabla_usuarios)
    elif respuesta.status_code==400:
        print('No se puede acceder al servidor.')
    else:
        print('No se han encontrado datos...')

def listado_users_db():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = [
        'N°', 'Nombre', 'Usuario', 'Correo', 'Teléfono', 'Sitio Web']
    listado_usuarios = obtener_listado_objetos(User)

    if listado_usuarios:
        for usuario in listado_usuarios:
            tabla_usuarios.add_row(
                [usuario.id, usuario.name, usuario.username, usuario.email, usuario.phone, usuario.website])
        print(tabla_usuarios)


def crear_user_db(nombre, nombre_usuario, correo, telefono, sitio_web, id_direccion, id_compania):
    usuario = User(
        name=nombre,
        username=nombre_usuario,
        email=correo,
        phone=telefono,
        website=sitio_web,
        addressId=id_direccion,
        companyId=id_compania
    )
    try:
        id_usuario = insertar_objeto(usuario)
        return id_usuario
    except Exception as error:
        print(f'[ERROR] Error al guardar al usuario: {error}')


def crear_user_api():
    url = config('url_users')

    nombre = input('Ingrese Nombre: ')
    nombre_usuario = input('Nombre Usuario:')
    correo = input('Correo electrónico: ')
    telefono = input('Teléfono: ')
    sitio_web = input('Sitio Web: ')

    user = {
        'name': nombre,
        'username': nombre_usuario,
        'email': correo,
        'phone': telefono,
        'website': sitio_web
    }

    respuesta = requests.post(str(url), data=user)

    print(respuesta.text)


def modificar_user_api():
    url = config('url_users')

    while True:
        id_usuario = input('Ingrese User ID:')
        try:
            id_usuario = int(id_usuario)
            url = f'{url}/{id_usuario}'
            
            nombre = input('Ingrese Nombre: ')
            nombre_usuario = input('Nombre Usuario:')
            correo = input('Correo electrónico: ')
            telefono = input('Teléfono: ')
            sitio_web = input('Sitio Web: ')

            user = {
                'name': nombre,
                'username': nombre_usuario,
                'email': correo,
                'phone': telefono,
                'website': sitio_web
            }

            respuesta = requests.put(str(url), data=user)

            print(respuesta.text)
            break
        except:
            print('Ingrese un número entero.')


def eliminar_user_api():
    url = config('url_users')

    while True:
        id_usuario = input('Ingrese User ID:')
        try:
            id_usuario = int(id_usuario)
            url = f'{url}/{id_usuario}'

            respuesta = requests.delete(str(url))

            print(respuesta.text)
            break
        except:
            print('Ingrese un número entero.')
