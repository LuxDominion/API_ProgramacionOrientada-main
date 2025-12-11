from prettytable import PrettyTable
import requests
import json
from datos import obtener_listado_objetos
from modelos import Comment, Post
from datos import insertar_objeto


def obtener_data_comentarios(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data...")
        comentarios = respuesta.json()
        contador = 0
        comentarios_existentes = obtener_listado_objetos(Comment)
        ids_existentes = [c.id for c in comentarios_existentes] if comentarios_existentes else []
        
        for comentario in comentarios:
            try:
                if comentario['id'] in ids_existentes:
                    continue
                
                crear_comentario(
                    comentario['name'],
                    comentario['email'],
                    comentario['body'],
                    comentario['postId']
                )
                contador += 1
            except Exception as e:
                continue
        
        print(f"[OK] {contador} comentarios cargados.")

    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")

def listado_comentarios():
    tabla_comentarios = PrettyTable()
    tabla_comentarios.field_names = [
        'N°', 'Nombre', 'Email','Comentario','Id Publicación']
    listado_comentarios = obtener_listado_objetos(Comment)

    if listado_comentarios:
        for comentario in listado_comentarios:
            tabla_comentarios.add_row(
                [comentario.id, comentario.name, comentario.email,comentario.body,comentario.postId])
        print(tabla_comentarios)
    else:
        print("No hay comentarios para mostrar. Use la opción 6 para descargarlos.")


def crear_comentario(nombre, correo, contenido, id_post):
    comentario = Comment(
        name=nombre,
        email=correo,
        body=contenido,
        postId=id_post
    )
    try:
        id_comentario = insertar_objeto(comentario)
        return id_comentario
    except Exception as error:
        print(f'[ERROR] Error al guardar comentario: {error}')
