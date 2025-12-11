from negocio import listado_users_api,eliminar_user_api,modificar_user_api,crear_user_api,obtener_data_usuarios, listado_users_db,obtener_data_publicaciones,listado_publicaciones,obtener_data_comentarios,listado_comentarios

from decouple import config
url_users = config('url_users')
url_posts = config('url_posts')
url_comments = config('url_comments')

listado_users_api(url_users)