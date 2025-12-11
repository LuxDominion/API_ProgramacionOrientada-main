# Lógica de Comentarios

from prettytable import PrettyTable
import requests
from datos import obtener_listado_objetos, insertar_objeto
from modelos import Comment

def obtener_data_comentarios(url):
    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            comentarios = respuesta.json()
            contador = 0
            
            comentarios_existentes = obtener_listado_objetos(Comment)
            ids_existentes = [c.id for c in comentarios_existentes] if comentarios_existentes else []
            
            for com in comentarios:
                try:
                    if com['id'] in ids_existentes:
                        continue
                    
                    crear_comentario(
                        com['name'],
                        com['email'],
                        com['body'],
                        com['postId']
                    )
                    contador += 1
                except Exception as e:
                    continue
            
            print(f"Se descargaron {contador} comentarios")
        else:
            print(f"Error: {respuesta.status_code}")
    
    except Exception as e:
        print(f"Error: {e}")

def listado_comentarios():
    try:
        comentarios = obtener_listado_objetos(Comment)
        
        if comentarios:
            tabla = PrettyTable()
            tabla.field_names = ['ID', 'Nombre', 'Email', 'Comentario', 'ID Publicación']
            
            for com in comentarios:
                tabla.add_row([
                    com.id,
                    com.name,
                    com.email,
                    com.body,
                    com.postId
                ])
            
            print(tabla)
        else:
            print("No hay comentarios guardados")
    
    except Exception as e:
        print(f"Error: {e}")

def crear_comentario(nombre, correo, contenido, id_post):
    try:
        nuevo_com = Comment(
            name=nombre,
            email=correo,
            body=contenido,
            postId=id_post
        )
        
        id_comentario = insertar_objeto(nuevo_com)
        return id_comentario
    
    except Exception as e:
        print(f"Error al guardar el comentario: {e}")
        return None

