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
    frecuencias_esperadas = pd.DataFrame(
        esperadas,
        index=tabla_efectiva.index,
        columns=tabla_efectiva.columns,
    )
    porcentaje_robusto = float((frecuencias_esperadas >= 5).to_numpy().mean() * 100)

    return ResultadoChiCuadrado(
        tabla_observada=tabla_efectiva,
        frecuencias_esperadas=frecuencias_esperadas,
        estadistico=float(estadistico),
        grados_libertad=int(grados_libertad),
        p_valor=float(p_valor),
        frecuencia_esperada_minima=float(frecuencias_esperadas.min().min()),
        porcentaje_frecuencias_esperadas_mayores_igual_5=porcentaje_robusto,
    )


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


def _quitar_marginales(tabla: pd.DataFrame) -> pd.DataFrame:
    """Quita fila o columna Total si están presentes."""
    resultado = tabla.copy()
    if ETIQUETA_TOTAL in resultado.index:
        resultado = resultado.drop(index=ETIQUETA_TOTAL)
    if ETIQUETA_TOTAL in resultado.columns:
        resultado = resultado.drop(columns=ETIQUETA_TOTAL)
    return resultado
