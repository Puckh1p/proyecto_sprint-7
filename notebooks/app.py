# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Título de la app
st.header("Análisis de anuncios de coches en EE.UU.")

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla para mostrar histograma
if st.checkbox('Mostrar histograma de odómetro'):
    st.write('Histograma de la columna odómetro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Casilla para mostrar gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión precio vs odómetro'):
    st.write('Gráfico de dispersión: precio vs odómetro')
    fig2 = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    )])
    fig2.update_layout(title_text='Precio vs Odómetro')
    st.plotly_chart(fig2, use_container_width=True)
