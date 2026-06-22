"""Página gerencial del dashboard."""

import plotly.express as px
import streamlit as st

from src.analisis_cualitativo import (
    ErrorAnalisisCualitativo,
    agregar_marginales,
    calcular_chi_cuadrado_muestral,
    comparar_p_valor_con_alpha,
    construir_datos_grafico_barras,
    construir_datos_grafico_porcentajes,
    construir_tabla_contingencia,
)
from src.interfaz_carga import (
    CLAVE_NOMBRE_ARCHIVO_ACTIVO,
    mostrar_carga_datos,
)


st.title("Perfil Gerencial")

st.write(
    "Vista descriptiva y muestral para acompañar el seguimiento semanal de la "
    "matriz de monopatines eléctricos."
)

datos_activos = mostrar_carga_datos()
if datos_activos is None:
    st.stop()

nombre_archivo = st.session_state.get(CLAVE_NOMBRE_ARCHIVO_ACTIVO, "Sin archivo")

st.caption(f"Archivo activo para el análisis cualitativo: `{nombre_archivo}`")
st.info(
    "Esta página resume la muestra semanal activa. La conclusión inferencial se "
    "presentará en la Página 2."
)

st.header("Análisis cualitativo")

tabla_observada = construir_tabla_contingencia(datos_activos)
tabla_con_marginales = agregar_marginales(tabla_observada)

st.subheader("Tabla de contingencia observada")
st.dataframe(tabla_con_marginales, use_container_width=True)

st.subheader("Frecuencia observada por sucursal")
datos_barras = construir_datos_grafico_barras(tabla_observada)
figura_barras = px.bar(
    datos_barras,
    x="Sucursal",
    y="Frecuencia",
    color="Nivel_Fallos",
    barmode="group",
    title="Nivel de fallos por sucursal",
    labels={
        "Sucursal": "Sucursal",
        "Frecuencia": "Frecuencia observada",
        "Nivel_Fallos": "Nivel de fallos",
    },
    hover_data={
        "Sucursal": True,
        "Nivel_Fallos": True,
        "Frecuencia": True,
    },
)
st.plotly_chart(figura_barras, use_container_width=True)

st.subheader("Composición porcentual por sucursal")
datos_porcentajes = construir_datos_grafico_porcentajes(tabla_observada)
figura_porcentajes = px.bar(
    datos_porcentajes,
    x="Sucursal",
    y="Porcentaje",
    color="Nivel_Fallos",
    barmode="stack",
    title="Composición porcentual del nivel de fallos por sucursal",
    labels={
        "Sucursal": "Sucursal",
        "Porcentaje": "Porcentaje dentro de la sucursal",
        "Nivel_Fallos": "Nivel de fallos",
        "Frecuencia": "Frecuencia observada",
    },
    hover_data={
        "Frecuencia": True,
        "Porcentaje": ":.2f",
    },
)
figura_porcentajes.update_yaxes(range=[0, 100], ticksuffix="%")
st.plotly_chart(figura_porcentajes, use_container_width=True)

st.subheader("Indicadores muestrales")
alpha = st.slider(
    "Nivel de significancia (α)",
    min_value=0.01,
    max_value=0.10,
    value=0.05,
    step=0.01,
)

try:
    resultado = calcular_chi_cuadrado_muestral(tabla_observada)
except ErrorAnalisisCualitativo as error:
    st.warning(str(error))
else:
    columna_1, columna_2, columna_3, columna_4 = st.columns(4)
    columna_1.metric("Chi-cuadrado muestral", f"{resultado.estadistico:.4f}")
    columna_2.metric("Grados de libertad", resultado.grados_libertad)
    columna_3.metric("p-valor", f"{resultado.p_valor:.4f}")
    columna_4.metric("α seleccionado", f"{alpha:.2f}")
    st.write(comparar_p_valor_con_alpha(resultado.p_valor, alpha))
    st.caption(
        "El p-valor se calcula únicamente a partir de los datos activos; cambiar "
        "α solo modifica la comparación mostrada."
    )
