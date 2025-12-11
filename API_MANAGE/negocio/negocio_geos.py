from modelos import Geo
from datos import insertar_objeto


def crear_geolocalizacion(latitud, longitud):
    geo = Geo(
        lat=latitud,
        lng=longitud
    )
    try:
        id_geo = insertar_objeto(geo)
        return id_geo
    except Exception as error:
        print(f'Error al guardar la geolocalización: {error}')
