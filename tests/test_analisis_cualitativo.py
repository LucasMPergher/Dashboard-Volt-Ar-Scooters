"""Pruebas asociadas al análisis cualitativo."""

from pathlib import Path

import pandas as pd
import pytest
from scipy.stats import chi2_contingency

from src.analisis_cualitativo import (
    ETIQUETA_TOTAL,
    ErrorAnalisisCualitativo,
    agregar_marginales,
    calcular_chi_cuadrado_muestral,
    calcular_porcentajes_por_sucursal,
    comparar_p_valor_con_alpha,
    construir_tabla_contingencia,
)
from src.carga_datos import cargar_archivo_semanal
from src.config import (
    CATEGORIAS_NIVEL_FALLOS,
    CATEGORIAS_SUCURSAL,
    ESCALAS_VARIABLES,
    VARIABLE_NIVEL_FALLOS,
    VARIABLE_SUCURSAL,
)


def test_categorias_permitidas_para_sucursal() -> None:
    """Comprueba las categorías nominales previstas para sucursal."""
    assert CATEGORIAS_SUCURSAL == ("Rosario", "Córdoba")


def test_categorias_permitidas_para_nivel_de_fallos() -> None:
    """Comprueba las categorías ordinales previstas para nivel de fallos."""
    assert CATEGORIAS_NIVEL_FALLOS == ("Bajo", "Medio", "Alto")


def test_escalas_cualitativas_declaradas() -> None:
    """Verifica que las variables cualitativas tengan su escala correcta."""
    assert ESCALAS_VARIABLES[VARIABLE_SUCURSAL] == "nominal"
    assert ESCALAS_VARIABLES[VARIABLE_NIVEL_FALLOS] == "ordinal"


def _datos_cualitativos() -> pd.DataFrame:
    """Construye datos cualitativos controlados para pruebas."""
    return pd.DataFrame(
        {
            "Sucursal": [
                "Rosario",
                "Rosario",
                "Rosario",
                "Rosario",
                "Córdoba",
                "Córdoba",
                "Córdoba",
                "Córdoba",
                "Córdoba",
                "Córdoba",
            ],
            "Nivel_Fallos": [
                "Bajo",
                "Bajo",
                "Medio",
                "Alto",
                "Bajo",
                "Medio",
                "Medio",
                "Alto",
                "Alto",
                "Alto",
            ],
        }
    )


def test_construccion_correcta_tabla_contingencia() -> None:
    """Comprueba frecuencias observadas de Sucursal por Nivel_Fallos."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())

    assert tabla.loc["Rosario", "Bajo"] == 2
    assert tabla.loc["Rosario", "Medio"] == 1
    assert tabla.loc["Rosario", "Alto"] == 1
    assert tabla.loc["Córdoba", "Bajo"] == 1
    assert tabla.loc["Córdoba", "Medio"] == 2
    assert tabla.loc["Córdoba", "Alto"] == 3


def test_orden_de_filas_y_columnas() -> None:
    """Mantiene el orden canónico de categorías."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())

    assert tuple(tabla.index) == CATEGORIAS_SUCURSAL
    assert tuple(tabla.columns) == CATEGORIAS_NIVEL_FALLOS


def test_totales_marginales_correctos() -> None:
    """Agrega totales marginales sin modificar categorías base."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())
    tabla_marginal = agregar_marginales(tabla)

    assert tabla_marginal.loc["Rosario", ETIQUETA_TOTAL] == 4
    assert tabla_marginal.loc["Córdoba", ETIQUETA_TOTAL] == 6
    assert tabla_marginal.loc[ETIQUETA_TOTAL, "Bajo"] == 3
    assert tabla_marginal.loc[ETIQUETA_TOTAL, "Medio"] == 3
    assert tabla_marginal.loc[ETIQUETA_TOTAL, "Alto"] == 4
    assert tabla_marginal.loc[ETIQUETA_TOTAL, ETIQUETA_TOTAL] == 10


def test_marginales_no_alteran_tabla_usada_en_prueba() -> None:
    """La prueba ignora fila y columna Total si llegan a la función."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())
    tabla_marginal = agregar_marginales(tabla)

    resultado_base = calcular_chi_cuadrado_muestral(tabla)
    resultado_marginal = calcular_chi_cuadrado_muestral(tabla_marginal)

    assert resultado_base.estadistico == pytest.approx(resultado_marginal.estadistico)
    assert resultado_base.p_valor == pytest.approx(resultado_marginal.p_valor)


def test_chi_cuadrado_coincide_con_scipy() -> None:
    """Compara el cálculo propio con scipy.stats.chi2_contingency."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())
    esperado_chi, esperado_p, _, _ = chi2_contingency(tabla, correction=False)

    resultado = calcular_chi_cuadrado_muestral(tabla)

    assert resultado.estadistico == pytest.approx(esperado_chi)
    assert resultado.p_valor == pytest.approx(esperado_p)


def test_grados_de_libertad_correctos() -> None:
    """Para una tabla 2 x 3 los grados de libertad son 2."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )

    assert resultado.grados_libertad == 2


def test_p_valor_entre_cero_y_uno() -> None:
    """El p-valor técnico debe quedar dentro del rango probabilístico."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )

    assert 0 <= resultado.p_valor <= 1


def test_frecuencias_esperadas_misma_dimension_que_tabla_efectiva() -> None:
    """Las esperadas conservan dimensión de la tabla enviada a SciPy."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )

    assert resultado.frecuencias_esperadas.shape == resultado.tabla_observada.shape


def test_suma_frecuencias_esperadas_igual_total_observado() -> None:
    """El total esperado debe coincidir con el total observado."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )

    assert resultado.frecuencias_esperadas.to_numpy().sum() == pytest.approx(
        resultado.tabla_observada.to_numpy().sum()
    )


def test_estadistico_no_negativo() -> None:
    """El estadístico Chi-cuadrado no puede ser negativo."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )

    assert resultado.estadistico >= 0


def test_p_valor_no_depende_de_alpha() -> None:
    """Cambiar alpha solo cambia la comparación, no el p-valor calculado."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )
    p_valor_original = resultado.p_valor

    comparar_p_valor_con_alpha(resultado.p_valor, 0.01)
    comparar_p_valor_con_alpha(resultado.p_valor, 0.10)

    assert resultado.p_valor == p_valor_original


def test_manejo_de_categoria_valida_ausente() -> None:
    """Una categoría válida ausente se elimina solo para la prueba."""
    datos = _datos_cualitativos()
    datos = datos[datos["Nivel_Fallos"] != "Alto"]
    tabla = construir_tabla_contingencia(datos)

    resultado = calcular_chi_cuadrado_muestral(tabla)

    assert "Alto" in tabla.columns
    assert "Alto" not in resultado.tabla_observada.columns
    assert resultado.tabla_observada.shape == (2, 2)


def test_error_comprensible_con_una_categoria_observada() -> None:
    """Si una variable tiene una sola categoría observada, la prueba no se calcula."""
    datos = pd.DataFrame(
        {
            "Sucursal": ["Rosario", "Rosario", "Rosario"],
            "Nivel_Fallos": ["Bajo", "Medio", "Alto"],
        }
    )
    tabla = construir_tabla_contingencia(datos)

    with pytest.raises(ErrorAnalisisCualitativo, match="al menos dos categorías"):
        calcular_chi_cuadrado_muestral(tabla)


def test_porcentajes_por_sucursal_suman_cien() -> None:
    """Los porcentajes para barras apiladas suman 100 % por sucursal."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())
    porcentajes = calcular_porcentajes_por_sucursal(tabla)

    assert porcentajes.loc["Rosario"].sum() == pytest.approx(100)
    assert porcentajes.loc["Córdoba"].sum() == pytest.approx(100)


def test_calculos_funcionan_con_excel_predeterminado() -> None:
    """El Excel predeterminado alimenta correctamente el módulo cualitativo."""
    datos = cargar_archivo_semanal(
        Path("data/volt_ar_semana_01.xlsx"),
        "volt_ar_semana_01.xlsx",
    )
    tabla = construir_tabla_contingencia(datos)
    resultado = calcular_chi_cuadrado_muestral(tabla)

    assert tabla.to_numpy().sum() == len(datos)
    assert resultado.grados_libertad == 2
    assert 0 <= resultado.p_valor <= 1


def test_pagina_no_contiene_frases_inferenciales_prohibidas() -> None:
    """La página gerencial no debe mostrar conclusiones inferenciales."""
    contenido = Path("pages/1_Perfil_Gerencial.py").read_text(encoding="utf-8").lower()
    frases_prohibidas = (
        "se rechaza h",
        "no se rechaza h",
        "existe asociación poblacional",
        "las variables son independientes",
    )

    for frase in frases_prohibidas:
        assert frase not in contenido
