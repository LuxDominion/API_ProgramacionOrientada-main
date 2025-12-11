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
        400: "[ERROR] Solicitud inválida (400). Verifique los datos enviados.",
        401: "[ERROR] No autorizado (401). Debe autenticarse.",
        403: "[ERROR] Acceso prohibido (403). No tiene permisos.",
        404: "[ERROR] Recurso no encontrado (404). Verifique el ID o URL.",
        409: "[ERROR] Conflicto (409). El recurso ya existe o hay datos inconsistentes.",
        429: "[WARNING] Demasiadas solicitudes (429). Intente más tarde.",
        500: "[ERROR] Error interno del servidor (500). Intente más tarde.",
        502: "[ERROR] Puerta de enlace defectuosa (502). Intente más tarde.",
        503: "[ERROR] Servicio no disponible (503). Intente más tarde.",
        504: "[ERROR] Tiempo de espera agotado (504). El servidor no responde.",
    }
    
    return errores.get(status_code, f"[ERROR] Error HTTP {status_code}")


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
            print(f"[OK] {tipo_recurso.capitalize()} creado exitosamente!")
            print(f"📊 Respuesta: {json.dumps(respuesta.json(), indent=2)}")
        elif respuesta.status_code == 400:
            print("[ERROR] Datos inválidos. Verifique los campos e intente de nuevo.")
            print(f"Detalles: {respuesta.text}")
        else:
            print(manejar_errores_http(respuesta.status_code, respuesta))
            print(f"📝 Respuesta: {respuesta.text}")
    
    except ValueError:
        print("[ERROR] Error: Debe ingresar valores numéricos donde corresponda.")
    except Timeout:
        print("[WARNING] Error: La solicitud tardó demasiado. El servidor no responde.")
    except ConnectionError:
        print("[WARNING] Error de conexión. Verifique su conexión a internet.")
    except RequestException as e:
        print(f"[ERROR] Error en la solicitud: {e}")
    except Exception as e:
        print(f"[ERROR] Error inesperado: {e}")


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
            print("[ERROR] El ID debe ser un número.")
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
            print(f"[OK] {tipo_recurso.capitalize()} actualizado exitosamente!")
            print(f"📊 Respuesta: {json.dumps(respuesta.json(), indent=2)}")
        elif respuesta.status_code == 404:
            print(f"[ERROR] No se encontró el {tipo_recurso.rstrip('s')} con ID {id_recurso}.")
        elif respuesta.status_code == 400:
            print("[ERROR] Datos inválidos. Verifique los campos.")
            print(f"Detalles: {respuesta.text}")
        else:
            print(manejar_errores_http(respuesta.status_code, respuesta))
            print(f"📝 Respuesta: {respuesta.text}")
    
    except Timeout:
        print("[WARNING] Error: La solicitud tardó demasiado.")
    except ConnectionError:
        print("[WARNING] Error de conexión.")
    except RequestException as e:
        print(f"[ERROR] Error en la solicitud: {e}")
    except Exception as e:
        print(f"[ERROR] Error inesperado: {e}")


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
            print("[ERROR] El ID debe ser un número.")
            return
        
        url_recurso = f"{url_base}/{id_recurso}"
        
        confirmacion = input(f"¿Está seguro de que desea eliminar el {tipo_recurso.rstrip('s')} con ID {id_recurso}? (s/n): ").lower()
        if confirmacion != 's':
            print("[WARNING] Operación cancelada.")
            return
        
        print("\n📤 Enviando solicitud DELETE...")
        respuesta = requests.delete(url_recurso, timeout=10)
        
        if respuesta.status_code in [200, 204]:
            print(f"[OK] {tipo_recurso.capitalize()} eliminado exitosamente!")
            if respuesta.content:
                print(f"📊 Respuesta: {json.dumps(respuesta.json(), indent=2)}")
        elif respuesta.status_code == 404:
            print(f"[ERROR] No se encontró el {tipo_recurso.rstrip('s')} con ID {id_recurso}.")
        else:
            print(manejar_errores_http(respuesta.status_code, respuesta))
            if respuesta.content:
                print(f"📝 Respuesta: {respuesta.text}")
    
    except Timeout:
        print("[WARNING] Error: La solicitud tardó demasiado.")
    except ConnectionError:
        print("[WARNING] Error de conexión.")
    except RequestException as e:
        print(f"[ERROR] Error en la solicitud: {e}")
    except Exception as e:
        print(f"[ERROR] Error inesperado: {e}")


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
            print("[ERROR] El ID debe ser un número.")
            return
        
        url_recurso = f"{url_base}/{id_recurso}"
        
        print("\n📥 Enviando solicitud GET...")
        respuesta = requests.get(url_recurso, timeout=10)
        
        if respuesta.status_code == 200:
            print(f"[OK] {tipo_recurso.capitalize()} obtenido exitosamente!")
            print(f"📊 Datos:\n{json.dumps(respuesta.json(), indent=2)}")
        elif respuesta.status_code == 404:
            print(f"[ERROR] No se encontró el {tipo_recurso.rstrip('s')} con ID {id_recurso}.")
        else:
            print(manejar_errores_http(respuesta.status_code, respuesta))
    
    except Timeout:
        print("[WARNING] Error: La solicitud tardó demasiado.")
    except ConnectionError:
        print("[WARNING] Error de conexión.")
    except RequestException as e:
        print(f"[ERROR] Error en la solicitud: {e}")
    except Exception as e:
        print(f"[ERROR] Error inesperado: {e}")
