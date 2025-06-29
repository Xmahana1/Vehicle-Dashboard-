import streamlit as st
import pandas as pd
import plotly.express as px

"""
Streamlit app para visualizar datos de vehículos de vehicles_us.csv
"""

def main():
    # Título de la app
    st.title("Proyecto 7 - Streamlit App")
    st.write("¡Bienvenido a tu app de análisis de vehículos!")

    # Carga del conjunto de datos
    df = pd.read_csv("vehicles_us.csv")
    st.subheader("Vista previa de los datos de vehículos")
    st.write(df.head())

if __name__ == "__main__":
    main()
