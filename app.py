"""Aplicación principal del dashboard académico."""

import streamlit as st

from src.config import NOMBRE_PROYECTO


st.set_page_config(
    page_title=NOMBRE_PROYECTO,
    layout="wide",
)

st.title(NOMBRE_PROYECTO)

st.write(
    "Dashboard académico de Estadística II orientado al análisis semanal de "
    "una matriz de monopatines eléctricos de Volt-Ar Scooters."
)

st.header("Páginas del dashboard")

st.subheader("1. Perfil Gerencial")
st.write(
    "Página con enfoque descriptivo y muestral para resumir la información "
    "operativa semanal sin presentar conclusiones inferenciales."
)

st.subheader("2. Perfil Analista")
st.write(
    "Página con enfoque inferencial y poblacional destinada a incorporar, en "
    "fases posteriores, pruebas estadísticas y modelos cuantitativos."
)

st.info(
    "Los módulos estadísticos completos se implementarán en fases posteriores. "
    "Esta versión solo prepara la estructura inicial del proyecto."
)
