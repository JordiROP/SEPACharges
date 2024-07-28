from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pandas as pd


class DB:
    def __init__(self):
        self.engine = create_engine('sqlite:///app/assets/data/database.db')

    def get_customers(self):
        with self.engine.connect() as conn:
            return pd.read_sql("SELECT * FROM CUSTOMER;", conn)

    def insert_customer(self, customer):
        with Session(self.engine) as session:
            try:
                session.add(customer)
                session.commit()
            except Exception as e:
                print(e)
                return False
        return True
