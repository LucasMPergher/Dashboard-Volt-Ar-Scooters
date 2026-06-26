"""Pruebas asociadas al análisis cuantitativo gerencial."""

from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import statsmodels.api as sm

from src.analisis_cuantitativo import (
    ErrorAnalisisCuantitativo,
    ajustar_regresion_lineal,
    ajustar_inferencia_regresion,
    calcular_intervalo_correlacion_fisher,
    concluir_prueba_pendiente,
    construir_datos_recta_regresion,
    decidir_prueba_pendiente,
    formatear_ecuacion_regresion,
    interpretar_correlacion_muestral,
    interpretar_r_cuadrado_muestral,
)
from src.carga_datos import cargar_archivo_semanal
from src.config import (
    ESCALAS_VARIABLES,
    TIPOS_VARIABLES,
    VARIABLE_ANTIGUEDAD_BATERIA,
    VARIABLE_AUTONOMIA_REAL,
    VARIABLES_ESTADISTICAS,
)


def _datos_cuantitativos(
    pendiente: float = -0.5,
    intercepto: float = 45.0,
    cantidad: int = 12,
) -> pd.DataFrame:
    """Construye datos lineales controlados para pruebas."""
    x = np.arange(1, cantidad + 1, dtype=float)
    y = intercepto + pendiente * x
    return pd.DataFrame(
        {
            VARIABLE_ANTIGUEDAD_BATERIA: x,
            VARIABLE_AUTONOMIA_REAL: y,
        }
    )


def _datos_no_perfectos() -> pd.DataFrame:
    """Construye datos con relación negativa no perfecta."""
    return pd.DataFrame(
        {
            VARIABLE_ANTIGUEDAD_BATERIA: [2, 5, 8, 11, 14, 17, 20, 23],
            VARIABLE_AUTONOMIA_REAL: [44.0, 42.8, 41.0, 40.5, 37.3, 36.6, 34.0, 33.8],
        }
    )


def test_exactamente_cuatro_variables_estadisticas() -> None:
    """Comprueba que el identificador no se cuente como variable estadística."""
    assert VARIABLES_ESTADISTICAS == (
        "Sucursal",
        "Nivel_Fallos",
        "Antiguedad_Bateria_Meses",
        "Autonomia_Real_Km",
    )
    assert len(VARIABLES_ESTADISTICAS) == 4
    assert "ID_Monopatin" not in VARIABLES_ESTADISTICAS


def test_variables_cuantitativas_declaradas() -> None:
    """Verifica el tipo de las variables X e Y del análisis cuantitativo."""
    assert TIPOS_VARIABLES[VARIABLE_ANTIGUEDAD_BATERIA] == "cuantitativa"
    assert TIPOS_VARIABLES[VARIABLE_AUTONOMIA_REAL] == "cuantitativa"


def test_escalas_cuantitativas_declaradas() -> None:
    """Verifica que las variables cuantitativas usen escala de razón."""
    assert ESCALAS_VARIABLES[VARIABLE_ANTIGUEDAD_BATERIA] == "razón"
    assert ESCALAS_VARIABLES[VARIABLE_AUTONOMIA_REAL] == "razón"


def test_regresion_lineal_perfecta_negativa_calcula_pendiente() -> None:
    """La pendiente estimada coincide con datos lineales controlados."""
    resultado = ajustar_regresion_lineal(_datos_cuantitativos(pendiente=-0.52))

    assert resultado.pendiente == pytest.approx(-0.52)


def test_regresion_lineal_perfecta_calcula_intercepto() -> None:
    """El intercepto estimado coincide con datos lineales controlados."""
    resultado = ajustar_regresion_lineal(
        _datos_cuantitativos(pendiente=-0.52, intercepto=45.0)
    )

    assert resultado.intercepto == pytest.approx(45.0)


def test_regresion_lineal_positiva_calcula_pearson_uno() -> None:
    """Una relación positiva perfecta produce Pearson igual a 1."""
    resultado = ajustar_regresion_lineal(
        _datos_cuantitativos(pendiente=2.0, intercepto=5.0)
    )

    assert resultado.coeficiente_pearson == pytest.approx(1.0)


def test_regresion_lineal_negativa_calcula_pearson_menos_uno() -> None:
    """Una relación negativa perfecta produce Pearson igual a -1."""
    resultado = ajustar_regresion_lineal(_datos_cuantitativos(pendiente=-1.25))

    assert resultado.coeficiente_pearson == pytest.approx(-1.0)


def test_r_cuadrado_lineal_perfecto_es_uno() -> None:
    """Una recta exacta produce R² igual a 1."""
    resultado = ajustar_regresion_lineal(_datos_cuantitativos())

    assert resultado.coeficiente_determinacion == pytest.approx(1.0)


def test_pearson_y_r_cuadrado_quedan_en_rangos_validos() -> None:
    """Los indicadores descriptivos respetan sus rangos matemáticos."""
    resultado = ajustar_regresion_lineal(_datos_no_perfectos())

    assert -1 <= resultado.coeficiente_pearson <= 1
    assert 0 <= resultado.coeficiente_determinacion <= 1


def test_r_cuadrado_coincide_con_pearson_al_cuadrado_en_modelo_simple() -> None:
    """En regresión lineal simple con intercepto, R² coincide con r²."""
    resultado = ajustar_regresion_lineal(_datos_no_perfectos())

    assert resultado.coeficiente_determinacion == pytest.approx(
        resultado.coeficiente_pearson**2
    )


def test_valores_ajustados_y_residuos_conservan_cantidad() -> None:
    """Los vectores internos tienen una observación por fila."""
    datos = _datos_no_perfectos()
    resultado = ajustar_regresion_lineal(datos)

    assert len(resultado.valores_ajustados) == len(datos)
    assert len(resultado.residuos) == len(datos)


def test_residuos_promedian_cero_con_intercepto() -> None:
    """El modelo con intercepto deja residuos centrados en cero."""
    resultado = ajustar_regresion_lineal(_datos_no_perfectos())

    assert resultado.residuos.mean() == pytest.approx(0.0, abs=1e-12)


def test_recta_de_regresion_ordena_x_de_menor_a_mayor() -> None:
    """La recta se construye ordenada para graficarla correctamente."""
    datos = _datos_cuantitativos()
    datos = datos.sample(frac=1, random_state=7)
    resultado = ajustar_regresion_lineal(datos)
    datos_recta = construir_datos_recta_regresion(datos, resultado)

    assert datos_recta[VARIABLE_ANTIGUEDAD_BATERIA].is_monotonic_increasing


def test_recta_de_regresion_usa_coeficientes_sin_redondeo_visual() -> None:
    """Los puntos de la recta usan los coeficientes reales del modelo."""
    datos = _datos_no_perfectos()
    resultado = ajustar_regresion_lineal(datos)
    datos_recta = construir_datos_recta_regresion(datos, resultado)
    esperado = (
        resultado.intercepto
        + resultado.pendiente * datos_recta[VARIABLE_ANTIGUEDAD_BATERIA]
    )

    assert datos_recta[VARIABLE_AUTONOMIA_REAL].to_numpy() == pytest.approx(
        esperado.to_numpy()
    )


def test_ecuacion_visible_redondea_solo_la_presentacion() -> None:
    """La ecuación formateada muestra una versión legible para la interfaz."""
    resultado = ajustar_regresion_lineal(_datos_no_perfectos())
    ecuacion = formatear_ecuacion_regresion(resultado)

    assert "Autonomía estimada (km)" in ecuacion
    assert "Antigüedad (meses)" in ecuacion


def test_error_con_menos_de_tres_observaciones() -> None:
    """La regresión requiere una cantidad mínima técnica de filas."""
    datos = _datos_cuantitativos(cantidad=2)

    with pytest.raises(ErrorAnalisisCuantitativo, match="al menos tres"):
        ajustar_regresion_lineal(datos)


def test_error_con_x_sin_variabilidad() -> None:
    """No se ajusta regresión si X es constante."""
    datos = _datos_cuantitativos()
    datos[VARIABLE_ANTIGUEDAD_BATERIA] = 10

    with pytest.raises(ErrorAnalisisCuantitativo, match="variable X"):
        ajustar_regresion_lineal(datos)


def test_error_con_y_sin_variabilidad() -> None:
    """No se ajusta regresión si Y es constante."""
    datos = _datos_cuantitativos()
    datos[VARIABLE_AUTONOMIA_REAL] = 30

    with pytest.raises(ErrorAnalisisCuantitativo, match="variable Y"):
        ajustar_regresion_lineal(datos)


def test_error_con_valores_nulos() -> None:
    """No se ajusta regresión con valores faltantes."""
    datos = _datos_cuantitativos()
    datos.loc[0, VARIABLE_AUTONOMIA_REAL] = np.nan

    with pytest.raises(ErrorAnalisisCuantitativo, match="valores nulos"):
        ajustar_regresion_lineal(datos)


def test_error_con_valores_no_finitos() -> None:
    """No se ajusta regresión con infinitos."""
    datos = _datos_cuantitativos()
    datos.loc[0, VARIABLE_AUTONOMIA_REAL] = np.inf

    with pytest.raises(ErrorAnalisisCuantitativo, match="no finitos"):
        ajustar_regresion_lineal(datos)


def test_error_con_valores_no_numericos() -> None:
    """No se ajusta regresión con texto en variables cuantitativas."""
    datos = _datos_cuantitativos()
    datos[VARIABLE_AUTONOMIA_REAL] = datos[VARIABLE_AUTONOMIA_REAL].astype(object)
    datos.loc[0, VARIABLE_AUTONOMIA_REAL] = "sin dato"

    with pytest.raises(ErrorAnalisisCuantitativo, match="numéricos"):
        ajustar_regresion_lineal(datos)


def test_interpretacion_reconoce_direccion_negativa() -> None:
    """La interpretación descriptiva nombra la dirección negativa."""
    texto = interpretar_correlacion_muestral(-0.85)

    assert "negativa" in texto
    assert "muestra semanal" in texto


def test_interpretacion_reconoce_direccion_positiva() -> None:
    """La interpretación descriptiva nombra la dirección positiva."""
    texto = interpretar_correlacion_muestral(0.65)

    assert "positiva" in texto


@pytest.mark.parametrize(
    ("coeficiente", "intensidad"),
    [
        (0.10, "muy débil"),
        (0.30, "débil"),
        (0.50, "moderada"),
        (0.70, "fuerte"),
        (0.90, "muy fuerte"),
    ],
)
def test_interpretacion_clasifica_intensidades(
    coeficiente: float,
    intensidad: str,
) -> None:
    """La clasificación cualitativa de Pearson sigue los cortes definidos."""
    texto = interpretar_correlacion_muestral(coeficiente)

    assert intensidad in texto


def test_interpretacion_r_cuadrado_muestra_porcentaje_muestral() -> None:
    """La interpretación de R² se expresa como porcentaje descriptivo."""
    texto = interpretar_r_cuadrado_muestral(0.810942)

    assert "81.09 %" in texto
    assert "muestra" in texto


def test_interpretacion_r_cuadrado_rechaza_valores_fuera_de_rango() -> None:
    """R² fuera de [0, 1] se informa como error técnico."""
    with pytest.raises(ErrorAnalisisCuantitativo, match="entre 0 y 1"):
        interpretar_r_cuadrado_muestral(1.5)


def test_excel_predeterminado_alimenta_regresion_muestral() -> None:
    """El Excel semanal predeterminado permite calcular la regresión P-05."""
    datos = cargar_archivo_semanal(
        Path("data/volt_ar_semana_01.xlsx"),
        "volt_ar_semana_01.xlsx",
    )
    resultado = ajustar_regresion_lineal(datos)

    assert len(datos) == 48
    assert resultado.cantidad == 48
    assert resultado.pendiente < 0
    assert resultado.coeficiente_pearson < 0
    assert 0.50 <= resultado.coeficiente_determinacion <= 1


def test_pagina_gerencial_conserva_modulo_cualitativo() -> None:
    """La incorporación P-05 no elimina la sección cualitativa de P-04."""
    contenido = Path("pages/1_Perfil_Gerencial.py").read_text(encoding="utf-8")

    assert "Análisis cualitativo" in contenido
    assert "construir_tabla_contingencia" in contenido


def test_pagina_gerencial_contiene_modulo_cuantitativo() -> None:
    """La Página 1 incorpora el análisis cuantitativo descriptivo."""
    contenido = Path("pages/1_Perfil_Gerencial.py").read_text(encoding="utf-8")

    assert "Análisis cuantitativo" in contenido
    assert "ajustar_regresion_lineal" in contenido
    assert "Recta de regresión muestral" in contenido


def test_pagina_no_contiene_frases_causales_o_inferenciales_prohibidas() -> None:
    """La Página 1 no debe presentar causalidad ni conclusión poblacional."""
    contenido = Path("pages/1_Perfil_Gerencial.py").read_text(
        encoding="utf-8"
    ).lower()
    frases_prohibidas = (
        "x causa y",
        "la relación se cumple en toda la población",
        "existe evidencia estadísticamente significativa",
        "conclusión poblacional",
        "intervalo de confianza",
    )

    for frase in frases_prohibidas:
        assert frase not in contenido


def _ajustar_statsmodels(datos: pd.DataFrame):
    """Ajusta el modelo auxiliar usado para comparar contra Statsmodels."""
    x = datos[VARIABLE_ANTIGUEDAD_BATERIA].astype(float)
    y = datos[VARIABLE_AUTONOMIA_REAL].astype(float)
    matriz_x = sm.add_constant(x, has_constant="add")
    return sm.OLS(y, matriz_x).fit()


def test_inferencia_grados_libertad_son_n_menos_dos() -> None:
    """En regresión simple con intercepto, gl = n - 2."""
    datos = _datos_no_perfectos()
    resultado = ajustar_inferencia_regresion(datos)

    assert resultado.grados_libertad == len(datos) - 2


def test_estadistico_t_es_pendiente_sobre_error_estandar() -> None:
    """El estadístico t de la pendiente coincide con b1 / SE(b1)."""
    resultado = ajustar_inferencia_regresion(_datos_no_perfectos())

    assert resultado.estadistico_t_pendiente == pytest.approx(
        resultado.pendiente / resultado.error_estandar_pendiente
    )


def test_estadistico_t_coincide_con_formula_basada_en_pearson() -> None:
    """Valida la equivalencia entre prueba de pendiente y correlación."""
    resultado = ajustar_inferencia_regresion(_datos_no_perfectos())
    r = resultado.coeficiente_pearson
    esperado = r * np.sqrt(resultado.cantidad - 2) / np.sqrt(1 - r**2)

    assert resultado.estadistico_t_pendiente == pytest.approx(esperado)


def test_p_valor_pendiente_entre_cero_y_uno() -> None:
    """El p-valor bilateral queda dentro del rango probabilístico."""
    resultado = ajustar_inferencia_regresion(_datos_no_perfectos())

    assert 0 <= resultado.p_valor_pendiente <= 1


def test_p_valor_pendiente_coincide_con_statsmodels() -> None:
    """El p-valor se toma de Statsmodels para el mismo modelo OLS."""
    datos = _datos_no_perfectos()
    resultado = ajustar_inferencia_regresion(datos)
    modelo = _ajustar_statsmodels(datos)

    assert resultado.p_valor_pendiente == pytest.approx(
        modelo.pvalues[VARIABLE_ANTIGUEDAD_BATERIA]
    )


def test_decision_pendiente_rechazo_cuando_p_menor_alpha() -> None:
    """Si p < alpha, se rechaza H0."""
    assert decidir_prueba_pendiente(0.01, 0.05) == "Se rechaza H₀."


def test_decision_pendiente_no_rechazo_cuando_p_mayor_o_igual_alpha() -> None:
    """Si p >= alpha, no se rechaza H0."""
    assert decidir_prueba_pendiente(0.08, 0.05) == "No se rechaza H₀."
    assert decidir_prueba_pendiente(0.05, 0.05) == "No se rechaza H₀."


def test_decision_pendiente_no_utiliza_aceptar_h0() -> None:
    """La decisión nunca debe aceptar H0."""
    texto = decidir_prueba_pendiente(0.08, 0.05).lower()

    assert "acept" not in texto


def test_conclusion_contextual_negativa() -> None:
    """La conclusión de rechazo reconoce una pendiente negativa."""
    texto = concluir_prueba_pendiente(0.01, 0.05, -0.5)

    assert "se rechaza H₀" in texto
    assert "relación lineal negativa" in texto
    assert "población simulada" in texto


def test_conclusion_contextual_positiva() -> None:
    """La conclusión de rechazo reconoce una pendiente positiva."""
    texto = concluir_prueba_pendiente(0.01, 0.05, 0.5)

    assert "relación lineal positiva" in texto


def test_conclusion_no_rechazo_correctamente_redactada() -> None:
    """La conclusión de no rechazo no afirma inexistencia definitiva."""
    texto = concluir_prueba_pendiente(0.20, 0.05, -0.5).lower()

    assert "no se rechaza" in texto
    assert "no proporcionan evidencia suficiente" in texto
    assert "se acepta" not in texto


def test_intervalo_pendiente_coincide_con_statsmodels() -> None:
    """El intervalo de la pendiente coincide con conf_int de Statsmodels."""
    datos = _datos_no_perfectos()
    resultado = ajustar_inferencia_regresion(datos, nivel_confianza=0.95)
    modelo = _ajustar_statsmodels(datos)
    intervalo = modelo.conf_int(alpha=0.05).loc[VARIABLE_ANTIGUEDAD_BATERIA]

    assert resultado.intervalo_pendiente == pytest.approx(tuple(intervalo))


def test_intervalo_intercepto_coincide_con_statsmodels() -> None:
    """El intervalo del intercepto coincide con conf_int de Statsmodels."""
    datos = _datos_no_perfectos()
    resultado = ajustar_inferencia_regresion(datos, nivel_confianza=0.95)
    modelo = _ajustar_statsmodels(datos)
    intervalo = modelo.conf_int(alpha=0.05).loc["const"]

    assert resultado.intervalo_intercepto == pytest.approx(tuple(intervalo))


def test_intervalos_se_amplian_al_aumentar_confianza() -> None:
    """Mayor confianza produce intervalos más anchos."""
    datos = _datos_no_perfectos()
    resultado_90 = ajustar_inferencia_regresion(datos, nivel_confianza=0.90)
    resultado_99 = ajustar_inferencia_regresion(datos, nivel_confianza=0.99)
    ancho_90 = resultado_90.intervalo_pendiente[1] - resultado_90.intervalo_pendiente[0]
    ancho_99 = resultado_99.intervalo_pendiente[1] - resultado_99.intervalo_pendiente[0]

    assert ancho_99 > ancho_90


def test_estimadores_no_cambian_con_nivel_confianza() -> None:
    """Cambiar confianza solo modifica los límites de los intervalos."""
    datos = _datos_no_perfectos()
    resultado_90 = ajustar_inferencia_regresion(datos, nivel_confianza=0.90)
    resultado_99 = ajustar_inferencia_regresion(datos, nivel_confianza=0.99)

    assert resultado_99.intercepto == pytest.approx(resultado_90.intercepto)
    assert resultado_99.pendiente == pytest.approx(resultado_90.pendiente)
    assert resultado_99.p_valor_pendiente == pytest.approx(
        resultado_90.p_valor_pendiente
    )


def test_p_valor_pendiente_no_cambia_con_alpha() -> None:
    """Alpha cambia la decisión, no el p-valor calculado."""
    resultado = ajustar_inferencia_regresion(_datos_no_perfectos())
    p_valor = resultado.p_valor_pendiente

    decidir_prueba_pendiente(p_valor, 0.01)
    decidir_prueba_pendiente(p_valor, 0.10)

    assert resultado.p_valor_pendiente == p_valor


def test_intervalo_fisher_queda_dentro_de_menos_uno_y_uno() -> None:
    """La aproximación de Fisher se mantiene dentro de [-1, 1]."""
    resultado = ajustar_inferencia_regresion(_datos_no_perfectos())

    assert resultado.intervalo_correlacion is not None
    limite_inferior, limite_superior = resultado.intervalo_correlacion
    assert -1 <= limite_inferior <= 1
    assert -1 <= limite_superior <= 1


def test_intervalo_fisher_contiene_r_estimado() -> None:
    """El intervalo de Fisher contiene al r muestral."""
    resultado = ajustar_inferencia_regresion(_datos_no_perfectos())

    assert resultado.intervalo_correlacion is not None
    limite_inferior, limite_superior = resultado.intervalo_correlacion
    assert limite_inferior <= resultado.coeficiente_pearson <= limite_superior


def test_inferencia_rechaza_n_menor_o_igual_tres() -> None:
    """La inferencia de la pendiente requiere al menos cuatro observaciones."""
    datos = _datos_cuantitativos(cantidad=3)

    with pytest.raises(ErrorAnalisisCuantitativo, match="al menos 4"):
        ajustar_inferencia_regresion(datos)


def test_intervalo_fisher_maneja_correlacion_perfecta() -> None:
    """Fisher no se calcula con r perfecto porque atanh no es finito."""
    assert calcular_intervalo_correlacion_fisher(1.0, 12, 0.95) is None
    assert calcular_intervalo_correlacion_fisher(-1.0, 12, 0.95) is None


def test_inferencia_error_con_x_constante() -> None:
    """No se ajusta inferencia si X es constante."""
    datos = _datos_cuantitativos()
    datos[VARIABLE_ANTIGUEDAD_BATERIA] = 8

    with pytest.raises(ErrorAnalisisCuantitativo, match="variable X"):
        ajustar_inferencia_regresion(datos)


def test_inferencia_error_con_y_constante() -> None:
    """No se ajusta inferencia si Y es constante."""
    datos = _datos_cuantitativos()
    datos[VARIABLE_AUTONOMIA_REAL] = 30

    with pytest.raises(ErrorAnalisisCuantitativo, match="variable Y"):
        ajustar_inferencia_regresion(datos)


def test_inferencia_excel_predeterminado_aproximado() -> None:
    """El Excel predeterminado reproduce los resultados esperados de P-07."""
    datos = cargar_archivo_semanal(
        Path("data/volt_ar_semana_01.xlsx"),
        "volt_ar_semana_01.xlsx",
    )
    resultado = ajustar_inferencia_regresion(datos)

    assert resultado.cantidad == 48
    assert resultado.grados_libertad == 46
    assert resultado.intercepto == pytest.approx(45.166071, rel=1e-6)
    assert resultado.pendiente == pytest.approx(-0.552768, rel=1e-6)
    assert resultado.coeficiente_pearson == pytest.approx(-0.900523, rel=1e-6)
    assert resultado.coeficiente_determinacion == pytest.approx(0.810942, rel=1e-6)
    assert resultado.estadistico_t_pendiente == pytest.approx(-14.0468, rel=1e-4)
    assert resultado.p_valor_pendiente == pytest.approx(2.97e-18, rel=1e-2)


def test_p06_permanece_presente_en_pagina_analista() -> None:
    """La inferencia cualitativa P-06 continúa disponible."""
    contenido = Path("pages/2_Perfil_Analista.py").read_text(encoding="utf-8")

    assert "Inferencia cualitativa" in contenido
    assert "Chi-cuadrado" in contenido
    assert "Evaluación de supuestos" in contenido


def test_p04_y_p05_siguen_funcionando_en_pagina_gerencial() -> None:
    """La fase P-07 no elimina los módulos gerenciales previos."""
    contenido = Path("pages/1_Perfil_Gerencial.py").read_text(encoding="utf-8")

    assert "Análisis cualitativo" in contenido
    assert "Análisis cuantitativo" in contenido
    assert "ajustar_regresion_lineal" in contenido


def test_pagina_analista_no_muestra_herramientas_pendientes() -> None:
    """Página 2 no implementa todavía herramientas de fases posteriores."""
    contenido = Path("pages/2_Perfil_Analista.py").read_text(
        encoding="utf-8"
    ).lower()
    frases_pendientes = (
        "q-q plot",
        "histograma de residuos",
        "intervalo de predicción individual",
        "intervalo para la media esperada",
        "calculadora de predicción",
    )

    for frase in frases_pendientes:
        assert frase not in contenido


def test_pagina_analista_no_contiene_lenguaje_causal() -> None:
    """La inferencia cuantitativa no debe afirmar causalidad."""
    contenido = Path("pages/2_Perfil_Analista.py").read_text(
        encoding="utf-8"
    ).lower()

    assert "causa" not in contenido
    assert "causal" not in contenido
