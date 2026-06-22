"""Análisis cualitativo descriptivo y muestral."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from scipy.stats import chi2_contingency

from src.config import (
    CATEGORIAS_NIVEL_FALLOS,
    CATEGORIAS_SUCURSAL,
    VARIABLE_NIVEL_FALLOS,
    VARIABLE_SUCURSAL,
)

ETIQUETA_TOTAL = "Total"


class ErrorAnalisisCualitativo(ValueError):
    """Error controlado para análisis cualitativo no calculable."""


@dataclass(frozen=True)
class ResultadoChiCuadrado:
    """Resultado técnico del cálculo Chi-cuadrado sobre la muestra activa."""

    tabla_observada: pd.DataFrame
    frecuencias_esperadas: pd.DataFrame
    estadistico: float
    grados_libertad: int
    p_valor: float
    frecuencia_esperada_minima: float
    porcentaje_frecuencias_esperadas_mayores_igual_5: float


@dataclass(frozen=True)
class EvaluacionRobustezChiCuadrado:
    """Evaluación técnica de las frecuencias esperadas de Chi-cuadrado."""

    frecuencia_esperada_minima: float
    cantidad_menores_que_uno: int
    cantidad_menores_que_cinco: int
    porcentaje_mayores_o_iguales_a_cinco: float
    cumple_minimo_absoluto: bool
    cumple_regla_ochenta_por_ciento: bool
    es_robusta: bool


def construir_tabla_contingencia(datos: pd.DataFrame) -> pd.DataFrame:
    """Construye la tabla observada Sucursal por Nivel_Fallos en orden canónico."""
    tabla = pd.crosstab(datos[VARIABLE_SUCURSAL], datos[VARIABLE_NIVEL_FALLOS])
    tabla = tabla.reindex(
        index=CATEGORIAS_SUCURSAL,
        columns=CATEGORIAS_NIVEL_FALLOS,
        fill_value=0,
    )
    return tabla.astype(int)


def agregar_marginales(tabla: pd.DataFrame) -> pd.DataFrame:
    """Agrega totales marginales de filas y columnas para visualización."""
    tabla_con_marginales = tabla.copy()
    tabla_con_marginales[ETIQUETA_TOTAL] = tabla_con_marginales.sum(axis=1)
    total_columnas = tabla_con_marginales.sum(axis=0)
    tabla_con_marginales.loc[ETIQUETA_TOTAL] = total_columnas
    return tabla_con_marginales.astype(int)


def calcular_chi_cuadrado_muestral(
    tabla_observada: pd.DataFrame,
) -> ResultadoChiCuadrado:
    """Calcula Chi-cuadrado muestral sin marginales y sin corrección de Yates."""
    tabla_efectiva = _obtener_tabla_efectiva(tabla_observada)
    estadistico, p_valor, grados_libertad, esperadas = chi2_contingency(
        tabla_efectiva,
        correction=False,
    )
    frecuencias_esperadas_scipy = pd.DataFrame(
        esperadas,
        index=tabla_efectiva.index,
        columns=tabla_efectiva.columns,
    )
    frecuencias_esperadas = construir_tabla_frecuencias_esperadas(tabla_efectiva)
    porcentaje_robusto = float((frecuencias_esperadas >= 5).to_numpy().mean() * 100)

    if not frecuencias_esperadas.equals(frecuencias_esperadas_scipy):
        frecuencias_esperadas = frecuencias_esperadas_scipy

    return ResultadoChiCuadrado(
        tabla_observada=tabla_efectiva,
        frecuencias_esperadas=frecuencias_esperadas,
        estadistico=float(estadistico),
        grados_libertad=int(grados_libertad),
        p_valor=float(p_valor),
        frecuencia_esperada_minima=float(frecuencias_esperadas.min().min()),
        porcentaje_frecuencias_esperadas_mayores_igual_5=porcentaje_robusto,
    )


def construir_tabla_frecuencias_esperadas(
    tabla_observada: pd.DataFrame,
) -> pd.DataFrame:
    """Calcula frecuencias esperadas con la fórmula de independencia."""
    tabla = _obtener_tabla_efectiva(tabla_observada).astype(float)
    total = float(tabla.to_numpy().sum())
    if total <= 0:
        raise ErrorAnalisisCualitativo(
            "No se pueden calcular frecuencias esperadas sin observaciones."
        )

    totales_fila = tabla.sum(axis=1)
    totales_columna = tabla.sum(axis=0)
    esperadas = pd.DataFrame(index=tabla.index, columns=tabla.columns, dtype=float)

    for fila in tabla.index:
        for columna in tabla.columns:
            esperadas.loc[fila, columna] = (
                totales_fila.loc[fila] * totales_columna.loc[columna] / total
            )

    return esperadas


def calcular_diferencias_relativas(
    observadas: pd.DataFrame,
    esperadas: pd.DataFrame,
) -> pd.DataFrame:
    """Calcula diferencias relativas porcentuales: (O - E) / E * 100."""
    observadas_alineadas, esperadas_alineadas = _preparar_tablas_comparables(
        observadas,
        esperadas,
    )
    if (esperadas_alineadas <= 0).to_numpy().any():
        raise ErrorAnalisisCualitativo(
            "Las frecuencias esperadas deben ser positivas."
        )

    return (observadas_alineadas - esperadas_alineadas) / esperadas_alineadas * 100


def calcular_aportes_chi_cuadrado(
    observadas: pd.DataFrame,
    esperadas: pd.DataFrame,
) -> pd.DataFrame:
    """Calcula el aporte de cada celda al estadístico Chi-cuadrado."""
    observadas_alineadas, esperadas_alineadas = _preparar_tablas_comparables(
        observadas,
        esperadas,
    )
    if (esperadas_alineadas <= 0).to_numpy().any():
        raise ErrorAnalisisCualitativo(
            "Las frecuencias esperadas deben ser positivas."
        )

    return (observadas_alineadas - esperadas_alineadas) ** 2 / esperadas_alineadas


def evaluar_robustez_chi_cuadrado(
    frecuencias_esperadas: pd.DataFrame,
) -> EvaluacionRobustezChiCuadrado:
    """Evalúa la robustez de la aproximación Chi-cuadrado."""
    esperadas = frecuencias_esperadas.astype(float)
    cantidad_celdas = esperadas.size
    if cantidad_celdas == 0:
        raise ErrorAnalisisCualitativo(
            "No se puede evaluar robustez sin frecuencias esperadas."
        )

    cantidad_menores_que_uno = int((esperadas < 1).to_numpy().sum())
    cantidad_menores_que_cinco = int((esperadas < 5).to_numpy().sum())
    porcentaje_mayores_o_iguales_a_cinco = float(
        (esperadas >= 5).to_numpy().mean() * 100
    )
    cumple_minimo_absoluto = cantidad_menores_que_uno == 0
    cumple_regla_ochenta = porcentaje_mayores_o_iguales_a_cinco >= 80

    return EvaluacionRobustezChiCuadrado(
        frecuencia_esperada_minima=float(esperadas.min().min()),
        cantidad_menores_que_uno=cantidad_menores_que_uno,
        cantidad_menores_que_cinco=cantidad_menores_que_cinco,
        porcentaje_mayores_o_iguales_a_cinco=porcentaje_mayores_o_iguales_a_cinco,
        cumple_minimo_absoluto=cumple_minimo_absoluto,
        cumple_regla_ochenta_por_ciento=cumple_regla_ochenta,
        es_robusta=cumple_minimo_absoluto and cumple_regla_ochenta,
    )


def decidir_chi_cuadrado(p_valor: float, alpha: float) -> str:
    """Aplica la regla de decisión inferencial para Chi-cuadrado."""
    if p_valor < alpha:
        return "Se rechaza H₀."

    return "No se rechaza H₀."


def concluir_chi_cuadrado(p_valor: float, alpha: float) -> str:
    """Genera una conclusión contextual dinámica para la Página 2."""
    alpha_formateado = f"{alpha:.2f}"
    if p_valor < alpha:
        return (
            f"Con un nivel de significancia de {alpha_formateado}, se rechaza "
            "la hipótesis nula. En el escenario analizado existe evidencia "
            "estadísticamente significativa de asociación entre la sucursal y "
            "el nivel de fallos técnicos en la población de monopatines de "
            "Volt-Ar Scooters. La conclusión corresponde al escenario "
            "poblacional simulado con fines académicos."
        )

    return (
        f"Con un nivel de significancia de {alpha_formateado}, no se rechaza "
        "la hipótesis nula. Los datos disponibles no proporcionan evidencia "
        "estadística suficiente para afirmar que existe asociación entre la "
        "sucursal y el nivel de fallos técnicos en la población. La conclusión "
        "corresponde al escenario poblacional simulado con fines académicos."
    )


def identificar_categorias_excluidas(
    tabla_observada: pd.DataFrame,
    tabla_efectiva: pd.DataFrame,
) -> dict[str, list[str]]:
    """Identifica categorías válidas excluidas del cálculo por total cero."""
    tabla_base = _quitar_marginales(tabla_observada)
    filas_excluidas = [
        str(fila) for fila in tabla_base.index if fila not in tabla_efectiva.index
    ]
    columnas_excluidas = [
        str(columna)
        for columna in tabla_base.columns
        if columna not in tabla_efectiva.columns
    ]
    return {
        VARIABLE_SUCURSAL: filas_excluidas,
        VARIABLE_NIVEL_FALLOS: columnas_excluidas,
    }


def calcular_porcentajes_por_sucursal(tabla_observada: pd.DataFrame) -> pd.DataFrame:
    """Calcula porcentajes por fila para barras apiladas al 100 %."""
    tabla = _quitar_marginales(tabla_observada).astype(float)
    totales_fila = tabla.sum(axis=1).replace(0, pd.NA)
    porcentajes = tabla.div(totales_fila, axis=0).fillna(0) * 100
    return porcentajes


def construir_datos_grafico_barras(tabla_observada: pd.DataFrame) -> pd.DataFrame:
    """Convierte la tabla observada a formato largo para barras agrupadas."""
    tabla = _quitar_marginales(tabla_observada)
    datos_largos = tabla.reset_index().melt(
        id_vars=VARIABLE_SUCURSAL,
        var_name=VARIABLE_NIVEL_FALLOS,
        value_name="Frecuencia",
    )
    return datos_largos


def construir_datos_grafico_porcentajes(tabla_observada: pd.DataFrame) -> pd.DataFrame:
    """Convierte frecuencias y porcentajes por sucursal a formato largo."""
    tabla = _quitar_marginales(tabla_observada)
    porcentajes = calcular_porcentajes_por_sucursal(tabla)

    frecuencias_largas = tabla.reset_index().melt(
        id_vars=VARIABLE_SUCURSAL,
        var_name=VARIABLE_NIVEL_FALLOS,
        value_name="Frecuencia",
    )
    porcentajes_largos = porcentajes.reset_index().melt(
        id_vars=VARIABLE_SUCURSAL,
        var_name=VARIABLE_NIVEL_FALLOS,
        value_name="Porcentaje",
    )
    frecuencias_largas["Porcentaje"] = porcentajes_largos["Porcentaje"]
    return frecuencias_largas


def comparar_p_valor_con_alpha(p_valor: float, alpha: float) -> str:
    """Devuelve una comparación neutral entre p-valor y nivel de significancia."""
    if p_valor < alpha:
        return "p-valor < α"

    return "p-valor ≥ α"


def _obtener_tabla_efectiva(tabla_observada: pd.DataFrame) -> pd.DataFrame:
    """Elimina marginales y categorías con total cero antes de Chi-cuadrado."""
    tabla = _quitar_marginales(tabla_observada)
    tabla = tabla.loc[tabla.sum(axis=1) > 0, tabla.sum(axis=0) > 0]

    if tabla.shape[0] < 2 or tabla.shape[1] < 2:
        raise ErrorAnalisisCualitativo(
            "No se puede calcular Chi-cuadrado muestral: se requieren al menos "
            "dos categorías observadas en cada variable."
        )

    return tabla


def _preparar_tablas_comparables(
    observadas: pd.DataFrame,
    esperadas: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Valida y alinea tablas observadas y esperadas de igual dimensión."""
    observadas_sin_marginales = _quitar_marginales(observadas).astype(float)
    esperadas_sin_marginales = _quitar_marginales(esperadas).astype(float)

    if not observadas_sin_marginales.index.equals(esperadas_sin_marginales.index):
        raise ErrorAnalisisCualitativo(
            "Las tablas observada y esperada deben tener las mismas filas."
        )

    if not observadas_sin_marginales.columns.equals(
        esperadas_sin_marginales.columns
    ):
        raise ErrorAnalisisCualitativo(
            "Las tablas observada y esperada deben tener las mismas columnas."
        )

    return observadas_sin_marginales, esperadas_sin_marginales


def _quitar_marginales(tabla: pd.DataFrame) -> pd.DataFrame:
    """Quita fila o columna Total si están presentes."""
    resultado = tabla.copy()
    if ETIQUETA_TOTAL in resultado.index:
        resultado = resultado.drop(index=ETIQUETA_TOTAL)
    if ETIQUETA_TOTAL in resultado.columns:
        resultado = resultado.drop(columns=ETIQUETA_TOTAL)
    return resultado
