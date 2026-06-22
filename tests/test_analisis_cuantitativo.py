"""Pruebas asociadas al análisis cuantitativo gerencial."""

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from src.analisis_cuantitativo import (
    ErrorAnalisisCuantitativo,
    ajustar_regresion_lineal,
    construir_datos_recta_regresion,
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
