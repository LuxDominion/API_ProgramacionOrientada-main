from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos.modelos import Base

# Usamos SQLite para mayor portabilidad
DATABASE_URL = 'sqlite:///api_manage.db'

motor_db = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=motor_db)
sesion = Session()

def crear_tablas():
    """Crea las tablas en la base de datos si no existen"""
    Base.metadata.create_all(motor_db)
    print("Tablas verificadas/creadas en SQLite.")

crear_tablas()
