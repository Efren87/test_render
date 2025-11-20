import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv')
st.title("Análisis Descriptivo de Vehículos")
st.text("Este es un análisis descriptivo de un conjunto de datos de vehículos.")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df["Price"], bins=30, kde=True, color="blue", ax=ax)
ax.set_xlabel("Precio")
ax.set_ylabel("Frecuencia")
ax.set_title("Distribución de Precios de los Vehículos")
ax.grid()
st.pyplot(fig)

if st.button("Haz clic aquí"):
    st.dataframe(df.head())