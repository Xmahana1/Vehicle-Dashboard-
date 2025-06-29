import pandas as pd
import plotly.express as px
import streamlit as st

def main():
    st.title("Cuadro de Mando - Proyecto 7")
    st.header("Exploración de datos de vehículos")

    # Carga de datos
    car_data = pd.read_csv("vehicles_us.csv")
    st.subheader("Vista previa de los primeros registros")
    st.write(car_data.head())

    # Casillas de verificación en lugar de botones
    build_hist = st.checkbox("Mostrar histograma de Kilometraje")
    build_scatter = st.checkbox("Mostrar diagrama de dispersión Kilometraje vs Precio")

    # Generar histograma si se marcó la casilla
    if build_hist:
        st.write("Creando histograma para la columna **odometer**")
        fig = px.histogram(
            car_data,
            x="odometer",
            title="Histograma de Kilometraje",
            labels={"odometer": "Kilometraje"}
        )
        st.plotly_chart(fig, use_container_width=True)

    # Generar diagrama de dispersión si se marcó la casilla
    if build_scatter:
        st.write("Creando diagrama de dispersión: **Kilometraje** vs **Precio**")
        fig2 = px.scatter(
            car_data,
            x="odometer",
            y="price",
            title="Dispersión: Kilometraje vs Precio",
            labels={"odometer": "Kilometraje", "price": "Precio ($)"}
        )
        st.plotly_chart(fig2, use_container_width=True)

if __name__ == "__main__":
    main()

