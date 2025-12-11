from modelos import Company
from datos import insertar_objeto


def crear_compania(nombre, slogan, negocio):
    compania = Company(
        name=nombre,
        catchPhrase=slogan,
        bs=negocio
    )
    try:
        id_compania = insertar_objeto(compania)
        return id_compania
    except Exception as error:
        print(f'[ERROR] Error al guardar la compañía: {error}')
