"""
Módulo Servicios - Operaciones CRUD con la API
Gestiona solicitudes GET, POST, PUT, DELETE
"""

import requests
import json
from requests.exceptions import RequestException, Timeout, ConnectionError


class APIServiceError(Exception):
    """Excepción personalizada para errores de API"""
    pass


def manejar_errores_http(status_code: int, respuesta: requests.Response = None) -> str:
    """
    Maneja y retorna mensajes de error según el código HTTP.
    
    Args:
        status_code (int): Código de estado HTTP
        respuesta (requests.Response): Objeto respuesta (opcional)
    
    Returns:
        str: Mensaje de error descriptivo
    """
    errores = {
        400: "Solicitud inválida. Verifique los datos enviados.",
        401: "No autorizado. Debe autenticarse.",
        403: "Acceso prohibido. No tiene permisos.",
        404: "Recurso no encontrado. Verifique el ID o URL.",
        409: "Conflicto. El recurso ya existe o hay datos inconsistentes.",
        429: "Demasiadas solicitudes. Intente más tarde.",
        500: "Error interno del servidor. Intente más tarde.",
        502: "Puerta de enlace defectuosa. Intente más tarde.",
        503: "Servicio no disponible. Intente más tarde.",
        504: "Tiempo de espera agotado. El servidor no responde.",
    }
    
    return errores.get(status_code, f"Error HTTP {status_code}")


def crear_recurso_api(url_base: str, tipo_recurso: str):
    """
    Crea un nuevo recurso mediante una solicitud POST.
    
    Args:
        url_base (str): URL base de la API
        tipo_recurso (str): Tipo de recurso (users, posts, comments)
    """
    try:
        print(f"\n➕ Crear nuevo {tipo_recurso}")
        print("-" * 50)
        
        datos = {}
        
        if tipo_recurso == "users":
            datos = {
                'name': input("Nombre: "),
                'username': input("Nombre de usuario: "),
                'email': input("Correo electrónico: "),
                'phone': input("Teléfono: "),
                'website': input("Sitio web: ")
            }
        elif tipo_recurso == "posts":
            datos = {
                'title': input("Título: "),
                'body': input("Contenido: "),
                'userId': int(input("ID del usuario: "))
            }
        elif tipo_recurso == "comments":
            datos = {
                'name': input("Nombre: "),
                'email': input("Correo electrónico: "),
                'body': input("Comentario: "),
                'postId': int(input("ID del post: "))
            }
        
        print("\n📤 Enviando solicitud POST...")
        respuesta = requests.post(url_base, json=datos, timeout=10)
        
        if respuesta.status_code in [200, 201]:
            print(f"{tipo_recurso.capitalize()} creado exitosamente!")
            print(f"📊 Respuesta: {json.dumps(respuesta.json(), indent=2)}")
        elif respuesta.status_code == 400:
            print("Datos inválidos. Verifique los campos e intente de nuevo.")
            print(f"Detalles: {respuesta.text}")
        else:
            print(manejar_errores_http(respuesta.status_code, respuesta))
            print(f"📝 Respuesta: {respuesta.text}")
    
    except ValueError:
        print("Error: Debe ingresar valores numéricos donde corresponda.")
    except Timeout:
        print("Error: La solicitud tardó demasiado. El servidor no responde.")
    except ConnectionError:
        print("Error de conexión. Verifique su conexión a internet.")
    except RequestException as e:
        print(f"Error en la solicitud: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def actualizar_recurso_api(url_base: str, tipo_recurso: str):
    """
    Actualiza un recurso existente mediante una solicitud PUT.
    
    Args:
        url_base (str): URL base de la API
        tipo_recurso (str): Tipo de recurso (users, posts, comments)
    """
    try:
        print(f"\n✏️  Actualizar {tipo_recurso}")
        print("-" * 50)
        
        try:
            id_recurso = int(input(f"Ingrese ID del {tipo_recurso.rstrip('s')}: "))
        except ValueError:
            print("El ID debe ser un número.")
            return
        
        url_recurso = f"{url_base}/{id_recurso}"
        datos = {}
        
        if tipo_recurso == "users":
            datos = {
                'name': input("Nombre: "),
                'username': input("Nombre de usuario: "),
                'email': input("Correo electrónico: "),
                'phone': input("Teléfono: "),
                'website': input("Sitio web: ")
            }
        elif tipo_recurso == "posts":
            datos = {
                'title': input("Título: "),
                'body': input("Contenido: "),
                'userId': int(input("ID del usuario: "))
            }
        elif tipo_recurso == "comments":
            datos = {
                'name': input("Nombre: "),
                'email': input("Correo electrónico: "),
                'body': input("Comentario: "),
                'postId': int(input("ID del post: "))
            }
        
        print("\n📤 Enviando solicitud PUT...")
        respuesta = requests.put(url_recurso, json=datos, timeout=10)
        
        if respuesta.status_code == 200:
            print(f"{tipo_recurso.capitalize()} actualizado exitosamente!")
            print(f"📊 Respuesta: {json.dumps(respuesta.json(), indent=2)}")
        elif respuesta.status_code == 404:
            print(f"No se encontró el {tipo_recurso.rstrip('s')} con ID {id_recurso}.")
        elif respuesta.status_code == 400:
            print("Datos inválidos. Verifique los campos.")
            print(f"Detalles: {respuesta.text}")
        else:
            print(manejar_errores_http(respuesta.status_code, respuesta))
            print(f"📝 Respuesta: {respuesta.text}")
    
    except Timeout:
        print("Error: La solicitud tardó demasiado.")
    except ConnectionError:
        print("Error de conexión.")
    except RequestException as e:
        print(f"Error en la solicitud: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def eliminar_recurso_api(url_base: str, tipo_recurso: str):
    """
    Elimina un recurso mediante una solicitud DELETE.
    
    Args:
        url_base (str): URL base de la API
        tipo_recurso (str): Tipo de recurso (users, posts, comments)
    """
    try:
        print(f"\n🗑️  Eliminar {tipo_recurso}")
        print("-" * 50)
        
        try:
            id_recurso = int(input(f"Ingrese ID del {tipo_recurso.rstrip('s')} a eliminar: "))
        except ValueError:
            print("El ID debe ser un número.")
            return
        
        url_recurso = f"{url_base}/{id_recurso}"
        
        confirmacion = input(f"¿Está seguro de que desea eliminar el {tipo_recurso.rstrip('s')} con ID {id_recurso}? (s/n): ").lower()
        if confirmacion != 's':
            print("Operación cancelada.")
            return
        
        print("\n📤 Enviando solicitud DELETE...")
        respuesta = requests.delete(url_recurso, timeout=10)
        
        if respuesta.status_code in [200, 204]:
            print(f"{tipo_recurso.capitalize()} eliminado exitosamente!")
            if respuesta.content:
                print(f"📊 Respuesta: {json.dumps(respuesta.json(), indent=2)}")
        elif respuesta.status_code == 404:
            print(f"No se encontró el {tipo_recurso.rstrip('s')} con ID {id_recurso}.")
        else:
            print(manejar_errores_http(respuesta.status_code, respuesta))
            if respuesta.content:
                print(f"📝 Respuesta: {respuesta.text}")
    
    except Timeout:
        print("Error: La solicitud tardó demasiado.")
    except ConnectionError:
        print("Error de conexión.")
    except RequestException as e:
        print(f"Error en la solicitud: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def obtener_recurso_api(url_base: str, tipo_recurso: str):
    """
    Obtiene un recurso específico mediante una solicitud GET.
    
    Args:
        url_base (str): URL base de la API
        tipo_recurso (str): Tipo de recurso (users, posts, comments)
    """
    try:
        print(f"\n🔍 Obtener {tipo_recurso}")
        print("-" * 50)
        
        try:
            id_recurso = int(input(f"Ingrese ID del {tipo_recurso.rstrip('s')}: "))
        except ValueError:
            print("El ID debe ser un número.")
            return
        
        url_recurso = f"{url_base}/{id_recurso}"
        
        print("\n📥 Enviando solicitud GET...")
        respuesta = requests.get(url_recurso, timeout=10)
        
        if respuesta.status_code == 200:
            print(f"{tipo_recurso.capitalize()} obtenido exitosamente!")
            print(f"📊 Datos:\n{json.dumps(respuesta.json(), indent=2)}")
        elif respuesta.status_code == 404:
            print(f"No se encontró el {tipo_recurso.rstrip('s')} con ID {id_recurso}.")
        else:
            print(manejar_errores_http(respuesta.status_code, respuesta))
    
    except Timeout:
        print("Error: La solicitud tardó demasiado.")
    except ConnectionError:
        print("Error de conexión.")
    except RequestException as e:
        print(f"Error en la solicitud: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
