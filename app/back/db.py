import pandas as pd
from sqlalchemy import create_engine


# engine = create_engine('sqlite:///../data/database.db')C:\Users\jordi.onrubia_blueta\PycharmProjects\SEPACharges\app\data\database.db

engine = create_engine('sqlite:///app/data/database.db')