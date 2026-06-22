"""Análisis cuantitativo descriptivo y muestral."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import pearsonr

from src.config import VARIABLE_ANTIGUEDAD_BATERIA, VARIABLE_AUTONOMIA_REAL


class ErrorAnalisisCuantitativo(ValueError):
    """Error controlado para análisis cuantitativo no calculable."""


@dataclass(frozen=True)
class ResultadoRegresionMuestral:
    """Resultado descriptivo de una regresión lineal muestral."""

    cantidad: int
    intercepto: float
    pendiente: float
    coeficiente_pearson: float
    coeficiente_determinacion: float
    valores_ajustados: pd.Series
    residuos: pd.Series


def ajustar_regresion_lineal(
    datos: pd.DataFrame,
    columna_x: str = VARIABLE_ANTIGUEDAD_BATERIA,
    columna_y: str = VARIABLE_AUTONOMIA_REAL,
) -> ResultadoRegresionMuestral:
    """Ajusta una regresión lineal muestral con intercepto."""
    x, y = _preparar_series_numericas(datos, columna_x, columna_y)
    matriz_x = sm.add_constant(x, has_constant="add")
    modelo = sm.OLS(y, matriz_x).fit()
    coeficiente_pearson = float(pearsonr(x, y).statistic)
    coeficiente_determinacion = float(modelo.rsquared)

    valores_ajustados = pd.Series(
        modelo.fittedvalues,
        index=datos.index,
        name="Autonomia_Ajustada_Km",
    )
    residuos = pd.Series(
        modelo.resid,
        index=datos.index,
        name="Residuo_Km",
    )

    return ResultadoRegresionMuestral(
        cantidad=len(datos),
        intercepto=float(modelo.params["const"]),
        pendiente=float(modelo.params[columna_x]),
        coeficiente_pearson=coeficiente_pearson,
        coeficiente_determinacion=coeficiente_determinacion,
        valores_ajustados=valores_ajustados,
        residuos=residuos,
    )


def interpretar_correlacion_muestral(coeficiente: float) -> str:
    """Interpreta Pearson de forma descriptiva para la muestra semanal."""
    _validar_pearson(coeficiente)
    magnitud = abs(coeficiente)
    intensidad = _clasificar_intensidad_correlacion(magnitud)

    if magnitud < 1e-12:
        return (
            "En la muestra semanal no se observa una dirección lineal apreciable."
        )

    sentido = "positiva" if coeficiente > 0 else "negativa"
    return (
        "En la muestra semanal se observa una relación lineal "
        f"{sentido} {intensidad}."
    )


def interpretar_r_cuadrado_muestral(coeficiente_determinacion: float) -> str:
    """Interpreta R² como porcentaje descriptivo de variabilidad muestral."""
    _validar_r_cuadrado(coeficiente_determinacion)
    porcentaje = coeficiente_determinacion * 100
    return (
        "En la muestra, el modelo lineal con la antigüedad explica "
        f"aproximadamente el {porcentaje:.2f} % de la variabilidad observada "
        "en la autonomía."
    )


def construir_datos_recta_regresion(
    datos: pd.DataFrame,
    resultado: ResultadoRegresionMuestral,
    columna_x: str = VARIABLE_ANTIGUEDAD_BATERIA,
    columna_y: str = VARIABLE_AUTONOMIA_REAL,
) -> pd.DataFrame:
    """Construye puntos ordenados de la recta usando el modelo ajustado."""
    valores_x = pd.Series(pd.to_numeric(datos[columna_x], errors="raise")).sort_values()
    valores_x = valores_x.drop_duplicates().reset_index(drop=True)
    valores_y = resultado.intercepto + resultado.pendiente * valores_x

    return pd.DataFrame(
        {
            columna_x: valores_x,
            columna_y: valores_y,
        }
    )


def formatear_ecuacion_regresion(
    resultado: ResultadoRegresionMuestral,
) -> str:
    """Formatea la ecuación muestral visible con unidades implícitas."""
    signo = "+" if resultado.pendiente >= 0 else "-"
    pendiente_abs = abs(resultado.pendiente)
    return (
        "Autonomía estimada (km) = "
        f"{resultado.intercepto:.2f} {signo} {pendiente_abs:.2f} × "
        "Antigüedad (meses)"
    )


def _preparar_series_numericas(
    datos: pd.DataFrame,
    columna_x: str,
    columna_y: str,
) -> tuple[pd.Series, pd.Series]:
    """Valida y convierte las series necesarias para ajustar el modelo."""
    columnas_faltantes = [
        columna for columna in (columna_x, columna_y) if columna not in datos.columns
    ]
    if columnas_faltantes:
        detalle = ", ".join(columnas_faltantes)
        raise ErrorAnalisisCuantitativo(
            f"Faltan columnas cuantitativas requeridas: {detalle}."
        )

    if len(datos) < 3:
        raise ErrorAnalisisCuantitativo(
            "Se requieren al menos tres observaciones para ajustar la regresión."
        )

    if datos[[columna_x, columna_y]].isna().any().any():
        raise ErrorAnalisisCuantitativo(
            "No se puede ajustar la regresión con valores nulos."
        )

    try:
        x = pd.to_numeric(datos[columna_x], errors="raise").astype(float)
        y = pd.to_numeric(datos[columna_y], errors="raise").astype(float)
    except (TypeError, ValueError) as error:
        raise ErrorAnalisisCuantitativo(
            "Las variables cuantitativas deben contener valores numéricos."
        ) from error

    if not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ErrorAnalisisCuantitativo(
            "No se puede ajustar la regresión con valores no finitos."
        )

    if x.nunique() <= 1:
        raise ErrorAnalisisCuantitativo(
            "No se puede ajustar la regresión: la variable X no tiene variabilidad."
        )

    if y.nunique() <= 1:
        raise ErrorAnalisisCuantitativo(
            "No se puede ajustar la regresión: la variable Y no tiene variabilidad."
        )

    x.name = columna_x
    y.name = columna_y
    return x, y


def _clasificar_intensidad_correlacion(magnitud: float) -> str:
    """Clasifica la intensidad de |r| con un criterio heurístico documentado."""
    if magnitud < 0.20:
        return "muy débil"
    if magnitud < 0.40:
        return "débil"
    if magnitud < 0.60:
        return "moderada"
    if magnitud < 0.80:
        return "fuerte"
    return "muy fuerte"


def _validar_pearson(coeficiente: float) -> None:
    """Valida que Pearson esté entre -1 y 1."""
    if not -1 <= coeficiente <= 1:
        raise ErrorAnalisisCuantitativo(
            "El coeficiente de Pearson debe estar entre -1 y 1."
        )


def _validar_r_cuadrado(coeficiente_determinacion: float) -> None:
    """Valida que R² esté entre 0 y 1."""
    if not 0 <= coeficiente_determinacion <= 1:
        raise ErrorAnalisisCuantitativo(
            "El coeficiente de determinación debe estar entre 0 y 1."
        )
