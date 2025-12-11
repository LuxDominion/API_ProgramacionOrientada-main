# Lógica de Publicaciones

from prettytable import PrettyTable
from modelos import Post
from datos import insertar_objeto, obtener_listado_objetos
import requests

def obtener_data_publicaciones(url):
    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            publicaciones = respuesta.json()
            contador = 0
            
            posts_existentes = obtener_listado_objetos(Post)
            ids_existentes = [p.id for p in posts_existentes] if posts_existentes else []
            
            for pub in publicaciones:
                try:
                    if pub['id'] in ids_existentes:
                        continue
                    
                    crear_publicacion(
                        pub['title'],
                        pub['body'],
                        pub['userId']
                    )
                    contador += 1
                except Exception as e:
                    continue
            
            print(f"Se descargaron {contador} publicaciones")
        else:
            print(f"Error: {respuesta.status_code}")
    
    except Exception as e:
        print(f"Error: {e}")

def listado_publicaciones():
    try:
        publicaciones = obtener_listado_objetos(Post)
        
        if publicaciones:
            tabla = PrettyTable()
            tabla.field_names = ['ID', 'Título', 'Contenido']
            
            for pub in publicaciones:
                tabla.add_row([pub.id, pub.title, pub.body])
            
            print(tabla)
        else:
            print("No hay publicaciones guardadas")
    
    except Exception as e:
        print(f"Error: {e}")

def crear_publicacion(titulo, contenido, id_usuario):
    try:
        nueva_pub = Post(
            title=titulo,
            body=contenido,
            userId=id_usuario
        )
        
        id_pub = insertar_objeto(nueva_pub)
        return id_pub
    
    except Exception as e:
        print(f"Error al guardar la publicación: {e}")
        return None

