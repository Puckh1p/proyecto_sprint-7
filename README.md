# 🚗 Análisis de Anuncios de Coches en EE.UU.

Esta aplicación web permite visualizar de manera interactiva información sobre anuncios de vehículos usados en Estados Unidos. Fue desarrollada como parte del Proyecto 7 utilizando **Streamlit**, **Pandas** y **Plotly**.

## 📊 Descripción del proyecto

El objetivo de este proyecto es ofrecer una interfaz sencilla donde el usuario pueda explorar gráficamente el conjunto de datos `vehicles_us.csv`, que contiene información de vehículos como:

- Precio (`price`)
- Odómetro (`odometer`)
- Tipo de combustible (`fuel`)
- Año del modelo (`model_year`)
- Estado del vehículo (`condition`)
- Transmisión (`transmission`)
- Entre otros.

## ⚙️ Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- Plotly

## 🖥️ Funcionalidades de la aplicación

- ✅ Visualización de un **histograma** de la columna `odometer`.
- ✅ Visualización de un **gráfico de dispersión** entre `odometer` y `price`.
- ✅ Interacción mediante **casillas de verificación** (`checkbox`) para mostrar u ocultar gráficos.

## 📁 Estructura del proyecto

├── app.py # Aplicación principal de Streamlit
├── requirements.txt # Dependencias necesarias
├── README.md # Este archivo
├── vehicles_us.csv # Conjunto de datos
├── .gitignore # Archivos ignorados por Git
└── notebooks/
    └── EDA.ipynb # Análisis exploratorio inicial