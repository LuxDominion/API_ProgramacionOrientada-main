# Conexión a Base de Datos

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos.modelos import Base

DATABASE_URL = 'sqlite:///api_manage.db'

motor_db = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=motor_db)
sesion = Session()

def crear_tablas():
    try:
        Base.metadata.create_all(motor_db)
        print("Base de datos lista")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")

