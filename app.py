import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Análisis de anuncios de venta de coches en EE.UU.') # título de la aplicación
st.header('Observa la cantidad de vehículos de acuerdo a la cantidad de km recorridos') # encabezado de la aplicación
     
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Construir un histograma')

st.header('Observa la relación de km recorridos vs precio') # encabezado de la aplicación

disp_button = st.button('Observa la dispersión de km recorridos vs precio') # crear un botón
     
if build_histogram: # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión de la relación de km recorridos vs precio')
         
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)