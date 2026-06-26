"""Aplicación principal del dashboard académico."""

import streamlit as st

from src.config import NOMBRE_PROYECTO
from src.interfaz_carga import mostrar_carga_datos


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
    "Página con enfoque inferencial y poblacional que reúne pruebas "
    "estadísticas, predicción y diagnóstico técnico del modelo cuantitativo."
)

st.info(
    "La aplicación trabaja con el archivo semanal activo y actualiza los "
    "módulos descriptivos, inferenciales, predictivos y diagnósticos al cargar "
    "una matriz válida."
)

mostrar_carga_datos()
