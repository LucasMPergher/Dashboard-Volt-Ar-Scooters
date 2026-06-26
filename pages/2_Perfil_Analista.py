"""Página analista del dashboard."""

import pandas as pd
import streamlit as st

from src.analisis_cualitativo import (
    ErrorAnalisisCualitativo,
    agregar_marginales,
    calcular_aportes_chi_cuadrado,
    calcular_chi_cuadrado_muestral,
    calcular_diferencias_relativas,
    concluir_chi_cuadrado,
    construir_tabla_contingencia,
    construir_tabla_frecuencias_esperadas,
    decidir_chi_cuadrado,
    evaluar_robustez_chi_cuadrado,
    identificar_categorias_excluidas,
)
from src.analisis_cuantitativo import (
    ErrorAnalisisCuantitativo,
    ajustar_inferencia_regresion,
    concluir_prueba_pendiente,
    decidir_prueba_pendiente,
)
from src.config import VARIABLE_ANTIGUEDAD_BATERIA, VARIABLE_AUTONOMIA_REAL
from src.interfaz_carga import (
    CLAVE_NOMBRE_ARCHIVO_ACTIVO,
    mostrar_carga_datos,
)


st.title("Perfil analista")

st.write(
    "Vista inferencial y poblacional para evaluar si los patrones observados "
    "en la muestra semanal ofrecen evidencia estadística sobre la población "
    "de monopatines de Volt-Ar Scooters."
)

datos_activos = mostrar_carga_datos()
if datos_activos is None:
    st.stop()

nombre_archivo = st.session_state.get(CLAVE_NOMBRE_ARCHIVO_ACTIVO, "Sin archivo")

st.caption(f"Archivo activo para el análisis inferencial: `{nombre_archivo}`")

st.header("Inferencia cualitativa")
st.write(
    "Se aplica una prueba Chi-cuadrado de independencia para evaluar la "
    "relación poblacional entre la sucursal y el nivel de fallos técnicos."
)
st.info(
    "La inferencia cuantitativa se presenta más abajo. Las herramientas para "
    "uso predictivo y los diagnósticos del modelo se incorporarán en una fase "
    "posterior."
)

st.subheader("Hipótesis")
st.markdown(
    """
**H₀:** La sucursal y el nivel de fallos técnicos son independientes en la
población de monopatines de Volt-Ar Scooters.

**H₁:** La sucursal y el nivel de fallos técnicos no son independientes; existe
asociación entre ambas variables en la población.
"""
)

tabla_observada_completa = construir_tabla_contingencia(datos_activos)

try:
    resultado = calcular_chi_cuadrado_muestral(tabla_observada_completa)
except ErrorAnalisisCualitativo as error:
    st.warning(str(error))
else:
    tabla_observada = resultado.tabla_observada
    frecuencias_esperadas = construir_tabla_frecuencias_esperadas(tabla_observada)
    diferencias_relativas = calcular_diferencias_relativas(
        tabla_observada,
        frecuencias_esperadas,
    )
    aportes = calcular_aportes_chi_cuadrado(
        tabla_observada,
        frecuencias_esperadas,
    )
    robustez = evaluar_robustez_chi_cuadrado(frecuencias_esperadas)
    categorias_excluidas = identificar_categorias_excluidas(
        tabla_observada_completa,
        tabla_observada,
    )

    st.subheader("Frecuencias observadas")
    st.write(
        "Tabla de casos observados en la muestra activa. Los marginales se "
        "muestran solo como apoyo de lectura y no forman parte del cálculo."
    )
    st.dataframe(
        agregar_marginales(tabla_observada_completa),
        use_container_width=True,
    )

    if any(categorias_excluidas.values()):
        st.warning(
            "Se excluyeron del cálculo las categorías sin observaciones: "
            f"{categorias_excluidas}."
        )

    st.subheader("Frecuencias esperadas")
    st.write(
        "Frecuencias que se esperarían bajo la hipótesis nula de independencia."
    )
    st.dataframe(
        frecuencias_esperadas.round(2),
        use_container_width=True,
    )

    st.subheader("Diferencias relativas porcentuales")
    st.write(
        "Convención utilizada: (frecuencia observada - frecuencia esperada) / "
        "frecuencia esperada × 100. Un valor positivo indica una frecuencia "
        "observada superior a la esperada bajo independencia; un valor negativo "
        "indica una frecuencia inferior."
    )
    st.dataframe(
        diferencias_relativas.round(2),
        use_container_width=True,
    )
    st.caption(
        "Una celda aislada no constituye por sí sola una prueba suficiente de "
        "asociación."
    )

    alpha = st.slider(
        "Nivel de significancia (α)",
        min_value=0.01,
        max_value=0.10,
        value=0.05,
        step=0.01,
        key="alpha_inferencia_cualitativa",
    )

    st.subheader("Resultado de la prueba")
    columna_1, columna_2, columna_3, columna_4 = st.columns(4)
    columna_1.metric("Chi-cuadrado", f"{resultado.estadistico:.6f}")
    columna_2.metric("Grados de libertad", resultado.grados_libertad)
    columna_3.metric("p-valor", f"{resultado.p_valor:.6f}")
    columna_4.metric("α seleccionado", f"{alpha:.2f}")

    decision = decidir_chi_cuadrado(resultado.p_valor, alpha)
    st.write(f"**Decisión:** {decision}")
    st.write(concluir_chi_cuadrado(resultado.p_valor, alpha))
    st.caption(
        "El p-valor se calcula a partir de la tabla observada; modificar α solo "
        "actualiza la regla de decisión."
    )

    st.subheader("Evaluación de supuestos")
    st.markdown(
        """
- **Independencia de las observaciones:** Se asume que cada fila corresponde a
  un monopatín distinto y que cada observación es independiente. Este supuesto
  depende del diseño de recolección.
- **Categorías mutuamente excluyentes:** La estructura validada respalda que
  cada monopatín pertenece a una sola sucursal y posee un único nivel de fallos.
"""
    )

    st.subheader("Robustez de la aproximación Chi-cuadrado")
    columna_1, columna_2, columna_3, columna_4 = st.columns(4)
    columna_1.metric(
        "Esperada mínima",
        f"{robustez.frecuencia_esperada_minima:.2f}",
    )
    columna_2.metric("< 1", robustez.cantidad_menores_que_uno)
    columna_3.metric("< 5", robustez.cantidad_menores_que_cinco)
    columna_4.metric(
        "≥ 5",
        f"{robustez.porcentaje_mayores_o_iguales_a_cinco:.2f} %",
    )

    if robustez.es_robusta:
        st.success(
            "La prueba cumple los criterios de robustez: ninguna frecuencia "
            "esperada es menor que 1 y al menos el 80 % es mayor o igual que 5."
        )
    else:
        st.warning(
            "La aproximación Chi-cuadrado debe interpretarse con precaución: "
            "no se cumplen todos los criterios de robustez. Puede revisarse si "
            "una combinación de categorías es metodológicamente válida, usar "
            "una prueba exacta apropiada o reportar el incumplimiento con "
            "cautela."
        )

    with st.expander("Ver aporte de cada celda al estadístico Chi-cuadrado"):
        st.write(
            "Cada celda muestra (observada - esperada)² / esperada. La suma "
            "coincide con el estadístico Chi-cuadrado."
        )
        st.dataframe(
            aportes.round(4),
            use_container_width=True,
        )
        st.caption(f"Suma de aportes: {aportes.to_numpy().sum():.6f}")

st.header("Inferencia cuantitativa")
st.write(
    "Se evalúa la pendiente poblacional de una regresión lineal simple entre "
    "la antigüedad de la batería y la autonomía real."
)

st.subheader("Modelo poblacional")
st.latex(r"Y = \beta_0 + \beta_1 X + \varepsilon")
st.write(
    f"Variable X: `{VARIABLE_ANTIGUEDAD_BATERIA}`. "
    f"Variable Y: `{VARIABLE_AUTONOMIA_REAL}`."
)

st.subheader("Hipótesis para la pendiente")
st.markdown(
    """
**H₀:** β₁ = 0. No existe relación lineal poblacional entre antigüedad y
autonomía.

**H₁:** β₁ ≠ 0. Existe una relación lineal poblacional entre antigüedad y
autonomía.
"""
)

alpha_cuantitativo = st.slider(
    "Nivel de significancia para la pendiente (α)",
    min_value=0.01,
    max_value=0.10,
    value=0.05,
    step=0.01,
    key="alpha_inferencia_cuantitativa",
)
nivel_confianza_porcentaje = st.slider(
    "Nivel de confianza para intervalos",
    min_value=90,
    max_value=99,
    value=95,
    step=1,
    key="nivel_confianza_regresion",
)
nivel_confianza = nivel_confianza_porcentaje / 100

try:
    resultado_regresion = ajustar_inferencia_regresion(
        datos_activos,
        nivel_confianza=nivel_confianza,
    )
except ErrorAnalisisCuantitativo as error:
    st.warning(str(error))
else:
    st.subheader("Resultado de la prueba t bilateral")
    columna_1, columna_2, columna_3, columna_4 = st.columns(4)
    columna_1.metric("n", resultado_regresion.cantidad)
    columna_2.metric("gl", resultado_regresion.grados_libertad)
    columna_3.metric("Pendiente", f"{resultado_regresion.pendiente:.6f}")
    columna_4.metric(
        "SE pendiente",
        f"{resultado_regresion.error_estandar_pendiente:.6f}",
    )

    columna_1, columna_2, columna_3, columna_4 = st.columns(4)
    columna_1.metric("t", f"{resultado_regresion.estadistico_t_pendiente:.6f}")
    columna_2.metric("p-valor", f"{resultado_regresion.p_valor_pendiente:.6g}")
    columna_3.metric("Pearson", f"{resultado_regresion.coeficiente_pearson:.6f}")
    columna_4.metric("R²", f"{resultado_regresion.coeficiente_determinacion:.6f}")

    decision_pendiente = decidir_prueba_pendiente(
        resultado_regresion.p_valor_pendiente,
        alpha_cuantitativo,
    )
    st.write(f"**Decisión:** {decision_pendiente}")
    st.write(
        concluir_prueba_pendiente(
            resultado_regresion.p_valor_pendiente,
            alpha_cuantitativo,
            resultado_regresion.pendiente,
        )
    )
    st.caption(
        "El p-valor se calcula con el modelo ajustado; modificar α solo "
        "actualiza la regla de decisión."
    )

    st.subheader("Intervalos de confianza para los parámetros")
    intervalos_parametros = pd.DataFrame(
        [
            {
                "Parámetro": "β₀",
                "Estimación": resultado_regresion.intercepto,
                "Límite inferior": resultado_regresion.intervalo_intercepto[0],
                "Límite superior": resultado_regresion.intervalo_intercepto[1],
                "Confianza": f"{nivel_confianza_porcentaje} %",
            },
            {
                "Parámetro": "β₁",
                "Estimación": resultado_regresion.pendiente,
                "Límite inferior": resultado_regresion.intervalo_pendiente[0],
                "Límite superior": resultado_regresion.intervalo_pendiente[1],
                "Confianza": f"{nivel_confianza_porcentaje} %",
            },
        ]
    )
    st.dataframe(
        intervalos_parametros,
        use_container_width=True,
        hide_index=True,
    )

    limite_inferior_pendiente, limite_superior_pendiente = (
        resultado_regresion.intervalo_pendiente
    )
    if limite_inferior_pendiente <= 0 <= limite_superior_pendiente:
        st.info(
            "El intervalo de la pendiente contiene cero; esto es coherente con "
            "no rechazar H₀ al nivel equivalente."
        )
    else:
        st.info(
            "El intervalo de la pendiente no contiene cero; esto es coherente "
            "con rechazar H₀ al nivel equivalente."
        )
    st.caption(
        "El intervalo y el p-valor son procedimientos equivalentes bajo las "
        "mismas condiciones, pero se presentan por separado."
    )

    st.subheader("Intervalo para ρ")
    if resultado_regresion.intervalo_correlacion is None:
        st.warning(
            "No se calcula el intervalo de Fisher para ρ cuando n <= 3 o cuando "
            "la correlación es perfecta."
        )
    else:
        intervalo_rho = pd.DataFrame(
            [
                {
                    "Coeficiente": "ρ",
                    "Estimación r": resultado_regresion.coeficiente_pearson,
                    "Límite inferior": resultado_regresion.intervalo_correlacion[0],
                    "Límite superior": resultado_regresion.intervalo_correlacion[1],
                    "Método": "Aproximación de Fisher",
                }
            ]
        )
        st.dataframe(
            intervalo_rho,
            use_container_width=True,
            hide_index=True,
        )

    st.info(
        "Las herramientas para uso predictivo y los diagnósticos del modelo se "
        "incorporarán en fases posteriores."
    )
