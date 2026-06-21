"""Validaciones básicas de estructura para los datos del dashboard."""

from collections.abc import Collection

from src.config import (
    COLUMNA_IDENTIFICADOR,
    COLUMNAS_ESPERADAS,
    MUESTRA_MAXIMA,
    MUESTRA_MINIMA,
    VARIABLES_ESTADISTICAS,
)


def obtener_columnas_esperadas(incluir_identificador: bool = True) -> tuple[str, ...]:
    """Devuelve los nombres de columnas esperados para la matriz de datos."""
    if incluir_identificador:
        return COLUMNAS_ESPERADAS

    return VARIABLES_ESTADISTICAS


def obtener_columnas_faltantes(
    columnas_disponibles: Collection[str],
    incluir_identificador: bool = False,
) -> tuple[str, ...]:
    """Identifica columnas requeridas que no aparecen en el conjunto recibido."""
    columnas_recibidas = set(columnas_disponibles)
    columnas_requeridas = obtener_columnas_esperadas(incluir_identificador)

    return tuple(
        columna for columna in columnas_requeridas if columna not in columnas_recibidas
    )


def cantidad_observaciones_valida(cantidad_observaciones: int) -> bool:
    """Indica si la cantidad de observaciones respeta los límites de la consigna."""
    return MUESTRA_MINIMA <= cantidad_observaciones <= MUESTRA_MAXIMA
