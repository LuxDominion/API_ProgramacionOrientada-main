from datos.conexion import sesion
from sqlalchemy import func


def obtener_listado_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos


def obtener_objeto_campo(objeto, campo, valor):
    objeto_identificado = sesion.query(objeto).filter_by(campo=valor).first()
    if objeto_identificado.isinstance(objeto):
        return objeto_identificado
