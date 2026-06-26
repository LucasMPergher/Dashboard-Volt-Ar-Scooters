"""Página gerencial del dashboard."""

import plotly.express as px
import plotly.graph_objects as go
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
from src.analisis_cuantitativo import (
    ErrorAnalisisCuantitativo,
    ajustar_regresion_lineal,
    construir_datos_recta_regresion,
    formatear_ecuacion_regresion,
    interpretar_correlacion_muestral,
    interpretar_r_cuadrado_muestral,
)
from src.config import (
    VARIABLE_ANTIGUEDAD_BATERIA,
    VARIABLE_AUTONOMIA_REAL,
    VARIABLE_NIVEL_FALLOS,
    VARIABLE_SUCURSAL,
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
    "presenta en la Página 2."
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

st.header("Análisis cuantitativo")
st.write(
    "Resumen descriptivo de la relación muestral entre la antigüedad de la "
    "batería y la autonomía real observada. La inferencia poblacional se "
    "realiza en la Página 2."
)

try:
    resultado_cuantitativo = ajustar_regresion_lineal(datos_activos)
except ErrorAnalisisCuantitativo as error:
    st.warning(str(error))
else:
    st.subheader("Dispersión y recta de regresión muestral")
    datos_recta = construir_datos_recta_regresion(
        datos_activos,
        resultado_cuantitativo,
    )

    figura_dispersion = px.scatter(
        datos_activos,
        x=VARIABLE_ANTIGUEDAD_BATERIA,
        y=VARIABLE_AUTONOMIA_REAL,
        color=VARIABLE_SUCURSAL,
        title="Autonomía real según antigüedad de batería",
        labels={
            VARIABLE_ANTIGUEDAD_BATERIA: "Antigüedad de batería (meses)",
            VARIABLE_AUTONOMIA_REAL: "Autonomía real (km)",
            VARIABLE_SUCURSAL: "Sucursal",
            VARIABLE_NIVEL_FALLOS: "Nivel de fallos",
        },
        hover_data={
            VARIABLE_SUCURSAL: True,
            VARIABLE_NIVEL_FALLOS: True,
            VARIABLE_ANTIGUEDAD_BATERIA: ":.0f",
            VARIABLE_AUTONOMIA_REAL: ":.2f",
        },
    )
    figura_dispersion.add_trace(
        go.Scatter(
            x=datos_recta[VARIABLE_ANTIGUEDAD_BATERIA],
            y=datos_recta[VARIABLE_AUTONOMIA_REAL],
            mode="lines",
            name="Recta de regresión muestral",
            line={"color": "#111827", "width": 3},
        )
    )
    figura_dispersion.update_layout(legend_title_text="Referencia")
    st.plotly_chart(figura_dispersion, use_container_width=True)

    st.subheader("Indicadores descriptivos muestrales")
    columna_1, columna_2, columna_3 = st.columns(3)
    columna_1.metric(
        "Pearson muestral",
        f"{resultado_cuantitativo.coeficiente_pearson:.4f}",
    )
    columna_2.metric(
        "R² muestral",
        f"{resultado_cuantitativo.coeficiente_determinacion:.4f}",
    )
    columna_3.metric("Observaciones", resultado_cuantitativo.cantidad)

    st.code(formatear_ecuacion_regresion(resultado_cuantitativo), language="text")
    st.write(interpretar_correlacion_muestral(
        resultado_cuantitativo.coeficiente_pearson
    ))
    st.write(interpretar_r_cuadrado_muestral(
        resultado_cuantitativo.coeficiente_determinacion
    ))
