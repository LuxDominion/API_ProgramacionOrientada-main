"""
Módulo Servicios - API Management
Incluye funciones para operaciones CRUD con la API
"""

from .api_service import (
    crear_recurso_api,
    actualizar_recurso_api,
    eliminar_recurso_api,
    obtener_recurso_api,
    manejar_errores_http,
    APIServiceError
)

__all__ = [
    'crear_recurso_api',
    'actualizar_recurso_api',
    'eliminar_recurso_api',
    'obtener_recurso_api',
    'manejar_errores_http',
    'APIServiceError'
]
