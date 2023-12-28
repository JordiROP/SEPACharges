import pandas as pd

from back.db import engine
from back.model import Customer
from sqlalchemy.orm import Session


def get_all_customers():
    conn = engine.connect()
    df = pd.read_sql("SELECT * FROM CUSTOMER", conn)
    conn.close()
    return df


def get_customer_by_dni(dni: str) -> dict | None:
    conn = engine.connect()
    customer = pd.read_sql(f"SELECT * FROM CUSTOMER WHERE dni='{dni}'", conn).to_dict(orient='records')
    customer = None if len(customer) == 0 else customer[0]
    conn.close()
    return customer


def upsert_customer(customer: Customer):
    with Session(engine) as session:
        session.add(customer)
        session.commit()
