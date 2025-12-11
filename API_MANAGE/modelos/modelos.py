from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street = Column(String(100), nullable=False)
    suite = Column(String(50), nullable=True)
    city = Column(String(50), nullable=True)
    zipcode = Column(String(20), nullable=True)
    geoId = Column(Integer, ForeignKey('geos.id'))


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    catchPhrase = Column(String(100), nullable=False)
    bs = Column(String(50), nullable=False)


class Geo(Base):
    __tablename__ = 'geos'
    id = Column(Integer, primary_key=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    body = Column(String(255), nullable=False)
    userId = Column(Integer, ForeignKey('users.id'))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    username = Column(String(25), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(25), nullable=True)
    website = Column(String(255), nullable=True)
    addressId = Column(Integer, ForeignKey('addresses.id'))
    companyId = Column(Integer, ForeignKey('companies.id'))


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    body = Column(String(255), nullable=False)
    postId = Column(Integer, ForeignKey('posts.id'))
    
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    correo = Column(String(255), nullable=False)
    contrasena_hash = Column(String(255), nullable=False)
    contrasena_salt = Column(String(255), nullable=False)