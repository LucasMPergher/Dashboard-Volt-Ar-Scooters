"""Página analista del dashboard."""

import pandas as pd
import plotly.graph_objects as go
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
    calcular_ancho_intervalo,
    calcular_diagnostico_residuos,
    calcular_prediccion,
    concluir_prueba_pendiente,
    construir_bandas_prediccion,
    construir_datos_histograma_residuos,
    construir_datos_qq,
    construir_datos_residuos_ajustados,
    decidir_prueba_pendiente,
)
from src.config import (
    ANTIGUEDAD_MAXIMA_MESES,
    ANTIGUEDAD_MINIMA_MESES,
    AUTONOMIA_MAXIMA_KM,
    AUTONOMIA_MINIMA_KM,
    VARIABLE_ANTIGUEDAD_BATERIA,
    VARIABLE_AUTONOMIA_REAL,
    VARIABLE_NIVEL_FALLOS,
    VARIABLE_SUCURSAL,
)
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
    "La inferencia cuantitativa y la calculadora de predicción se presentan "
    "más abajo. La validación técnica de supuestos se presenta al final de "
    "esta página."
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

    st.info("La validación técnica de supuestos se presenta al final de la página.")

    st.header("Calculadora de predicción")
    st.write(
        "Esta herramienta estima la autonomía para una antigüedad de batería "
        "ingresada por el analista usando el mismo modelo lineal ajustado."
    )
    valor_x_prediccion = st.number_input(
        "Antigüedad de la batería (meses)",
        min_value=ANTIGUEDAD_MINIMA_MESES,
        max_value=ANTIGUEDAD_MAXIMA_MESES,
        value=24,
        step=1,
        key="valor_x_calculadora_prediccion",
    )

    try:
        prediccion = calcular_prediccion(
            datos_activos,
            valor_x=float(valor_x_prediccion),
            nivel_confianza=nivel_confianza,
        )
        bandas_prediccion = construir_bandas_prediccion(
            datos_activos,
            nivel_confianza=nivel_confianza,
        )
    except ErrorAnalisisCuantitativo as error:
        st.warning(str(error))
    else:
        st.caption(
            f"Nivel de confianza utilizado: {nivel_confianza_porcentaje} %. "
            f"Rango observado de X: {prediccion.minimo_x_observado:.0f} a "
            f"{prediccion.maximo_x_observado:.0f} meses."
        )

        if prediccion.es_extrapolacion:
            st.warning(
                "El valor ingresado se encuentra fuera del rango observado en "
                "la muestra. La estimación constituye una extrapolación y debe "
                "interpretarse con mayor precaución."
            )

        ancho_media = calcular_ancho_intervalo(
            prediccion.limite_inferior_media,
            prediccion.limite_superior_media,
        )
        ancho_individual = calcular_ancho_intervalo(
            prediccion.limite_inferior_individual,
            prediccion.limite_superior_individual,
        )

        columna_1, columna_2, columna_3 = st.columns(3)
        columna_1.metric(
            "Predicción puntual",
            f"{prediccion.prediccion_puntual:.2f} km",
        )
        columna_2.metric(
            "Ancho IC media",
            f"{ancho_media:.2f} km",
        )
        columna_3.metric(
            "Ancho intervalo individual",
            f"{ancho_individual:.2f} km",
        )

        st.subheader("Intervalos de predicción")
        intervalos_prediccion = pd.DataFrame(
            [
                {
                    "Intervalo": "Media esperada",
                    "Límite inferior": prediccion.limite_inferior_media,
                    "Predicción": prediccion.prediccion_puntual,
                    "Límite superior": prediccion.limite_superior_media,
                    "Confianza": f"{nivel_confianza_porcentaje} %",
                },
                {
                    "Intervalo": "Observación individual",
                    "Límite inferior": prediccion.limite_inferior_individual,
                    "Predicción": prediccion.prediccion_puntual,
                    "Límite superior": prediccion.limite_superior_individual,
                    "Confianza": f"{nivel_confianza_porcentaje} %",
                },
            ]
        )
        st.dataframe(
            intervalos_prediccion,
            use_container_width=True,
            hide_index=True,
        )

        st.write(
            "El intervalo de confianza para la media esperada describe la "
            "autonomía promedio esperada de todos los monopatines con "
            f"{prediccion.valor_x:.0f} meses de antigüedad."
        )
        st.write(
            "El intervalo de predicción individual describe la autonomía de un "
            "monopatín individual con esa antigüedad. Es más amplio porque "
            "incorpora incertidumbre sobre la media estimada y variabilidad "
            "individual alrededor de la recta."
        )

        limites_intervalos = [
            prediccion.limite_inferior_media,
            prediccion.limite_superior_media,
            prediccion.limite_inferior_individual,
            prediccion.limite_superior_individual,
        ]
        excede_rango_operativo = (
            min(limites_intervalos) < AUTONOMIA_MINIMA_KM
            or max(limites_intervalos) > AUTONOMIA_MAXIMA_KM
        )
        if excede_rango_operativo:
            st.info(
                "El intervalo estadístico excede el rango operativo utilizado "
                "en la simulación; se presenta sin recorte para conservar el "
                "resultado del modelo."
            )

        figura_prediccion = go.Figure()
        figura_prediccion.add_trace(
            go.Scatter(
                x=bandas_prediccion[VARIABLE_ANTIGUEDAD_BATERIA],
                y=bandas_prediccion["individual_superior"],
                mode="lines",
                line={"width": 0},
                name="Límite superior individual",
                showlegend=False,
            )
        )
        figura_prediccion.add_trace(
            go.Scatter(
                x=bandas_prediccion[VARIABLE_ANTIGUEDAD_BATERIA],
                y=bandas_prediccion["individual_inferior"],
                mode="lines",
                fill="tonexty",
                fillcolor="rgba(148, 163, 184, 0.22)",
                line={"width": 0},
                name="Intervalo individual",
            )
        )
        figura_prediccion.add_trace(
            go.Scatter(
                x=bandas_prediccion[VARIABLE_ANTIGUEDAD_BATERIA],
                y=bandas_prediccion["media_superior"],
                mode="lines",
                line={"width": 0},
                name="Límite superior media",
                showlegend=False,
            )
        )
        figura_prediccion.add_trace(
            go.Scatter(
                x=bandas_prediccion[VARIABLE_ANTIGUEDAD_BATERIA],
                y=bandas_prediccion["media_inferior"],
                mode="lines",
                fill="tonexty",
                fillcolor="rgba(37, 99, 235, 0.24)",
                line={"width": 0},
                name="IC media esperada",
            )
        )
        figura_prediccion.add_trace(
            go.Scatter(
                x=bandas_prediccion[VARIABLE_ANTIGUEDAD_BATERIA],
                y=bandas_prediccion["prediccion_puntual"],
                mode="lines",
                line={"color": "#111827", "width": 3},
                name="Recta del modelo",
            )
        )
        figura_prediccion.add_trace(
            go.Scatter(
                x=[prediccion.valor_x],
                y=[prediccion.prediccion_puntual],
                mode="markers",
                marker={"color": "#dc2626", "size": 11},
                name="Valor ingresado",
            )
        )
        figura_prediccion.update_layout(
            title="Predicción de autonomía según antigüedad",
            xaxis_title="Antigüedad de la batería (meses)",
            yaxis_title="Autonomía real estimada (km)",
            legend_title_text="Referencia",
        )
        st.plotly_chart(figura_prediccion, use_container_width=True)

    st.header("Validación técnica de supuestos")
    st.write(
        "Los gráficos permiten evaluar la compatibilidad de los datos con los "
        "supuestos del modelo lineal. La decisión debe considerar conjuntamente "
        "los patrones observados, el contexto y el tamaño muestral."
    )

    try:
        diagnostico = calcular_diagnostico_residuos(datos_activos)
        datos_residuos = construir_datos_residuos_ajustados(
            datos_activos,
            diagnostico,
        )
        datos_qq = construir_datos_qq(diagnostico.residuos)
        datos_histograma = construir_datos_histograma_residuos(
            diagnostico.residuos
        )
    except ErrorAnalisisCuantitativo as error:
        st.warning(str(error))
    else:
        st.subheader("Residuos frente a valores ajustados")
        figura_residuos = go.Figure()
        datos_no_atipicos = datos_residuos[~datos_residuos["Atipico_Mayor_2"]]
        datos_atipicos = datos_residuos[datos_residuos["Atipico_Mayor_2"]]

        figura_residuos.add_trace(
            go.Scatter(
                x=datos_no_atipicos["Autonomia_Ajustada_Km"],
                y=datos_no_atipicos["Residuo_Km"],
                mode="markers",
                marker={"color": "#2563eb", "size": 8},
                name="Residuos",
                customdata=datos_no_atipicos[
                    [
                        "Autonomia_Observada_Km",
                        "Residuo_Estandarizado",
                        VARIABLE_ANTIGUEDAD_BATERIA,
                        VARIABLE_SUCURSAL,
                        VARIABLE_NIVEL_FALLOS,
                    ]
                ],
                hovertemplate=(
                    "Ajustada: %{x:.2f} km<br>"
                    "Residuo: %{y:.2f} km<br>"
                    "Observada: %{customdata[0]:.2f} km<br>"
                    "Residuo estandarizado: %{customdata[1]:.2f}<br>"
                    "Antigüedad: %{customdata[2]} meses<br>"
                    "Sucursal: %{customdata[3]}<br>"
                    "Nivel de fallos: %{customdata[4]}<extra></extra>"
                ),
            )
        )
        figura_residuos.add_trace(
            go.Scatter(
                x=datos_atipicos["Autonomia_Ajustada_Km"],
                y=datos_atipicos["Residuo_Km"],
                mode="markers",
                marker={"color": "#dc2626", "size": 10, "symbol": "diamond"},
                name="|residuo estandarizado| > 2",
                customdata=datos_atipicos[
                    [
                        "Autonomia_Observada_Km",
                        "Residuo_Estandarizado",
                        VARIABLE_ANTIGUEDAD_BATERIA,
                        VARIABLE_SUCURSAL,
                        VARIABLE_NIVEL_FALLOS,
                    ]
                ],
                hovertemplate=(
                    "Ajustada: %{x:.2f} km<br>"
                    "Residuo: %{y:.2f} km<br>"
                    "Observada: %{customdata[0]:.2f} km<br>"
                    "Residuo estandarizado: %{customdata[1]:.2f}<br>"
                    "Antigüedad: %{customdata[2]} meses<br>"
                    "Sucursal: %{customdata[3]}<br>"
                    "Nivel de fallos: %{customdata[4]}<extra></extra>"
                ),
            )
        )
        figura_residuos.add_hline(
            y=0,
            line_dash="dash",
            line_color="#111827",
            annotation_text="Residuo = 0",
        )
        figura_residuos.update_layout(
            title="Residuos frente a valores ajustados",
            xaxis_title="Autonomía ajustada (km)",
            yaxis_title="Residuo (km)",
            legend_title_text="Referencia",
        )
        st.plotly_chart(figura_residuos, use_container_width=True)

        st.subheader("Linealidad")
        st.write(
            "Un patrón curvo o sistemático alrededor de cero puede indicar que "
            "la forma lineal no representa adecuadamente la relación."
        )

        st.subheader("Homocedasticidad")
        st.write(
            "Una dispersión aproximadamente constante de residuos a lo largo de "
            "los valores ajustados es compatible con varianza constante. Una "
            "forma de embudo puede indicar heterocedasticidad."
        )

        st.subheader("Q-Q Plot de residuos")
        figura_qq = go.Figure()
        figura_qq.add_trace(
            go.Scatter(
                x=datos_qq["Cuantil_Teorico"],
                y=datos_qq["Residuo_Ordenado"],
                mode="markers",
                marker={"color": "#2563eb", "size": 8},
                name="Residuos ordenados",
            )
        )
        figura_qq.add_trace(
            go.Scatter(
                x=datos_qq["Cuantil_Teorico"],
                y=datos_qq["Linea_Referencia"],
                mode="lines",
                line={"color": "#111827", "width": 2},
                name="Línea de referencia",
            )
        )
        figura_qq.update_layout(
            title="Q-Q Plot de residuos",
            xaxis_title="Cuantiles teóricos normales",
            yaxis_title="Residuos ordenados",
            legend_title_text="Referencia",
        )
        st.plotly_chart(figura_qq, use_container_width=True)
        st.write(
            "Si los puntos se aproximan razonablemente a la línea de referencia, "
            "el supuesto de normalidad de los residuos resulta compatible con "
            "los datos. Desviaciones sistemáticas, especialmente en los "
            "extremos, pueden indicar falta de normalidad."
        )

        with st.expander("Ver histograma de residuos"):
            figura_histograma = go.Figure()
            figura_histograma.add_trace(
                go.Bar(
                    x=datos_histograma["Marca_Clase"],
                    y=datos_histograma["Frecuencia"],
                    width=(
                        datos_histograma["Limite_Superior"]
                        - datos_histograma["Limite_Inferior"]
                    ),
                    marker={"color": "#60a5fa"},
                    name="Frecuencia",
                )
            )
            figura_histograma.add_vline(
                x=0,
                line_dash="dash",
                line_color="#111827",
                annotation_text="Residuo = 0",
            )
            figura_histograma.update_layout(
                title="Histograma de residuos",
                xaxis_title="Residuo (km)",
                yaxis_title="Frecuencia",
                bargap=0.05,
            )
            st.plotly_chart(figura_histograma, use_container_width=True)
            st.caption("El histograma complementa al Q-Q Plot, no lo sustituye.")

        st.subheader("Métricas diagnósticas")
        columna_1, columna_2, columna_3, columna_4 = st.columns(4)
        columna_1.metric("Media residuos", f"{diagnostico.media_residuos:.6f}")
        columna_2.metric(
            "Desvío residual",
            f"{diagnostico.desviacion_residuos:.6f}",
        )
        columna_3.metric(
            "|r est.| > 2",
            diagnostico.cantidad_residuos_atipicos_dos,
        )
        columna_4.metric(
            "|r est.| > 3",
            diagnostico.cantidad_residuos_atipicos_tres,
        )
        st.caption(
            "Los conteos de residuos estandarizados son ayudas diagnósticas y "
            "no constituyen una prueba definitiva."
        )

        st.subheader("Normalidad")
        st.write(
            "El supuesto de normalidad se refiere a los residuos o errores del "
            "modelo, no necesariamente a la distribución de X o de Y."
        )

        st.subheader("Independencia")
        st.write(
            "La independencia depende del diseño de recolección. Se asume que "
            "cada fila representa un monopatín diferente y que las observaciones "
            "no dependen entre sí."
        )
