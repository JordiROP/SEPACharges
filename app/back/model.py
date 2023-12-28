from sqlalchemy import Column, String, Boolean, Numeric, Date, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = "Customer"

    dni = Column(String, primary_key=True, name="dni")
    name = Column(String, name="nombre")
    surname1 = Column(String, name="apellido1")
    surname2 = Column(String, name="apellido2")
    birthdate = Column(Date, name="fecha_nacimiento")
    phone = Column(String, name="telefono")
    email = Column(String, name="email")
    direction = Column(String, name="direccion")
    pc = Column(Integer, name="cp")
    city = Column(String, name="ciudad")
    iban = Column(String, name="IBAN")
    register_date = Column(Date, name="alta")
    drop_date = Column(Date, name="baja")
    quota = Column(Numeric, name="cuota")
    active = Column(Boolean, name="activo")
