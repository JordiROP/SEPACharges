from sqlalchemy import Column, String, Boolean, Numeric, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dt

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
    street = Column(String, name="calle")
    portal = Column(String, name="portal")
    door = Column(String, name="puerta")
    cp = Column(Integer, name="cp")
    city = Column(String, name="ciudad")
    iban = Column(String, name="IBAN")
    register_date = Column(Date, name="alta")
    drop_date = Column(Date, name="baja")
    quota = Column(Numeric, name="cuota")
    active = Column(Boolean, name="activo")

    @staticmethod
    def create_empty_customer():
        return Customer(dni="", name="", surname1="", surname2="", birthdate=dt.today(), phone="", email="", street="",
                        portal="", door="", cp="", city="", iban="", register_date=dt.today(),drop_date=dt.today(),
                        quota=0.0, active=True)
