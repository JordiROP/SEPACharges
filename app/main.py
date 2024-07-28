from datetime import datetime as dt
import streamlit as st

try:
    from db.db import DB
    from gui.register import register_customer
except: # noqa
    from app.db.db import DB
    from app.gui.register import register_customer

app_db = DB()
st.set_page_config(layout="wide")

img, title = st.columns([0.1, 0.9])
with img:
    st.image("app/assets/images/gimnas_puente_logo.jpg", use_column_width="always")
with title:
    st.text("")
    st.text("")
    st.title("Gimnàs Puente")

tab1, tab2, tab3, tab4 = st.tabs(["Panel Principal", "Registro", "Analiticas", "Manejo de Datos"])
with tab1:
    customers_df = app_db.get_customers()
    st.dataframe(customers_df, use_container_width=True)
with tab2:
    register_customer(app_db)
with tab3:
    st.text("under construction")
with tab4:
    st.text("under construction")



