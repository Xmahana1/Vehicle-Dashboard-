# Proyecto_7: Cuadro de Mando de Vehículos

## Descripción
Este proyecto consiste en una **aplicación web interactiva** desarrollada con **Streamlit**, que permite explorar y visualizar un conjunto de datos de anuncios de venta de vehículos en Estados Unidos. El objetivo es ofrecer un panel de control sencillo e intuitivo para el análisis inicial de los datos, sin necesidad de programar.

## Funcionalidad
- **Vista previa de datos**: muestra las primeras filas del CSV (`vehicles_us.csv`) para familiarizarse con las columnas y el contenido.
- **Histograma de Kilometraje**: construye un histograma interactivo de la columna `odometer` para analizar la distribución de kilometraje de los vehículos.
- **Diagrama de dispersión Kilometraje vs Precio**: genera un scatter plot que relaciona el kilometraje (`odometer`) con el precio (`price`).
- **Selección dinámica**: mediante casillas de verificación (`st.checkbox`), el usuario decide qué gráficos ver en cada momento.

## Requisitos
- Python 3.11+
- Conda (o virtualenv)
- Librerías:
  ```text
  pandas
  plotly
  streamlit
## 🚀 Demo en vivo

Nuestra aplicación está desplegada en Render.  
Visítala aquí: [https://proyecto-7-s87p.onrender.com/]
(https://proyecto-7-s87p.onrender.com/)
