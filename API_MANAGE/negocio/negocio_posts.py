from prettytable import PrettyTable
from modelos import Post
from datos import insertar_objeto,obtener_listado_objetos
import requests

def obtener_data_publicaciones(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data...")
        publicaciones = respuesta.json()
        contador = 0
        posts_existentes = obtener_listado_objetos(Post)
        ids_existentes = [p.id for p in posts_existentes] if posts_existentes else []
        
        for publicacion in publicaciones:
            try:
                if publicacion['id'] in ids_existentes:
                    continue
                
                crear_publicacion(
                    publicacion['title'],
                    publicacion['body'],
                    publicacion['userId']
                )
                contador += 1
            except Exception as e:
                continue
        
        print(f"[OK] {contador} publicaciones cargadas.")

    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")

def listado_publicaciones():
    tabla_publicaciones = PrettyTable()
    tabla_publicaciones.field_names = [
        'N°', 'Título', 'Contenido']
    listado_publicaciones = obtener_listado_objetos(Post)

    if listado_publicaciones:
        for publicacion in listado_publicaciones:
            tabla_publicaciones.add_row(
                [publicacion.id, publicacion.title, publicacion.body])
        tabla_publicaciones._min_width = {"N°": 5, "Título": 50,"Contenido":100}
        tabla_publicaciones._max_width = {"N°": 5, "Título": 50,"Contenido":100}
        print(tabla_publicaciones)
    else:
        print("No hay publicaciones para mostrar. Use la opción 4 para descargarlas.")

def crear_publicacion(titulo, contenido, id_usuario):
    publicacion = Post(
        title=titulo,
        body=contenido,
        userId=id_usuario
    )
    try:
        id_publicacion = insertar_objeto(publicacion)
        return id_publicacion
    except Exception as error:
        print(f'[ERROR] Error al guardar la publicación: {error}')
