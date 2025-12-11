import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    from datos.conexion import crear_tablas
    crear_tablas()
    print("[OK] Base de datos inicializada correctamente.")
    
    from negocio import obtener_data_usuarios
    from auxiliares.api_data import url_users
    
    print("\nProbando descarga de usuarios...")
    obtener_data_usuarios(url_users)
    
except Exception as e:
    print(f"[ERROR] {e}")
    import traceback
    traceback.print_exc()
