
import streamlit as st
import yfinance as yf
st.title ("Mi primer app en Streamlit") 

Acciones = st.selectbox(
    "Acciones",
    options=["AAPL", "MSFT", "AMZN", "NVDA"],
    help="Selecciona la acción de la cual deseas conocer la información."
)

datos = yf.download(Acciones)["Close"]
print(datos)

st.dataframe(datos)
