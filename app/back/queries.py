import pandas as pd

from back.db import engine


def get_all_customers():
    conn = engine.connect()
    df = pd.read_sql("SELECT * FROM CUSTOMER", conn)
    conn.close()
    return df
