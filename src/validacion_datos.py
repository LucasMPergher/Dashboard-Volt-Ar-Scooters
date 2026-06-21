"""Validaciones y normalización de la matriz semanal del dashboard."""

from collections.abc import Collection

import numpy as np
import pandas as pd

from src.config import (
    ANTIGUEDAD_MAXIMA_MESES,
    ANTIGUEDAD_MINIMA_MESES,
    AUTONOMIA_MAXIMA_KM,
    AUTONOMIA_MINIMA_KM,
    CATEGORIAS_NIVEL_FALLOS,
    CATEGORIAS_SUCURSAL,
    COLUMNA_IDENTIFICADOR,
    COLUMNAS_ESPERADAS,
    MUESTRA_MAXIMA,
    MUESTRA_MINIMA,
    VARIABLES_ESTADISTICAS,
    VARIABLE_ANTIGUEDAD_BATERIA,
    VARIABLE_AUTONOMIA_REAL,
    VARIABLE_NIVEL_FALLOS,
    VARIABLE_SUCURSAL,
)


class ErrorDatos(ValueError):
    """Error base para problemas de carga o validación de datos."""


class ErrorFormatoArchivo(ErrorDatos):
    """Error asociado al formato o lectura del archivo."""


class ErrorColumnasDatos(ErrorDatos):
    """Error asociado a columnas faltantes, adicionales o no permitidas."""


class ErrorCantidadFilas(ErrorDatos):
    """Error asociado a la cantidad de observaciones."""


class ErrorCategorias(ErrorDatos):
    """Error asociado a categorías cualitativas inválidas."""


class ErrorValoresNumericos(ErrorDatos):
    """Error asociado a valores numéricos inválidos."""


class ErrorValoresFaltantes(ErrorDatos):
    """Error asociado a valores nulos o faltantes."""


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


def validar_y_normalizar_datos(datos: pd.DataFrame) -> pd.DataFrame:
    """Devuelve una copia normalizada de la matriz semanal validada."""
    _validar_columnas(datos)
    _validar_cantidad_filas(datos)

    normalizados = datos.loc[:, VARIABLES_ESTADISTICAS].copy(deep=True)
    _validar_sin_nulos(normalizados)

    normalizados[VARIABLE_SUCURSAL] = _normalizar_categorias(
        normalizados[VARIABLE_SUCURSAL],
        CATEGORIAS_SUCURSAL,
        VARIABLE_SUCURSAL,
    )
    normalizados[VARIABLE_NIVEL_FALLOS] = _normalizar_categorias(
        normalizados[VARIABLE_NIVEL_FALLOS],
        CATEGORIAS_NIVEL_FALLOS,
        VARIABLE_NIVEL_FALLOS,
    )
    normalizados[VARIABLE_ANTIGUEDAD_BATERIA] = _normalizar_enteros_en_rango(
        normalizados[VARIABLE_ANTIGUEDAD_BATERIA],
        VARIABLE_ANTIGUEDAD_BATERIA,
        ANTIGUEDAD_MINIMA_MESES,
        ANTIGUEDAD_MAXIMA_MESES,
    )
    normalizados[VARIABLE_AUTONOMIA_REAL] = _normalizar_numeros_en_rango(
        normalizados[VARIABLE_AUTONOMIA_REAL],
        VARIABLE_AUTONOMIA_REAL,
        AUTONOMIA_MINIMA_KM,
        AUTONOMIA_MAXIMA_KM,
    )

    return normalizados


def _validar_columnas(datos: pd.DataFrame) -> None:
    """Valida que existan exactamente las cuatro columnas estadísticas."""
    columnas = tuple(str(columna) for columna in datos.columns)
    columnas_unnamed = tuple(
        columna for columna in columnas if columna.strip().lower().startswith("unnamed")
    )

    if columnas_unnamed:
        raise ErrorColumnasDatos(
            "Columnas no permitidas tipo Unnamed: "
            f"{', '.join(columnas_unnamed)}."
        )

    conjunto_recibido = set(columnas)
    conjunto_esperado = set(VARIABLES_ESTADISTICAS)
    faltantes = tuple(
        columna for columna in VARIABLES_ESTADISTICAS if columna not in conjunto_recibido
    )
    adicionales = tuple(
        columna for columna in columnas if columna not in conjunto_esperado
    )

    if faltantes or adicionales:
        partes = []
        if faltantes:
            partes.append(f"faltantes: {', '.join(faltantes)}")
        if adicionales:
            partes.append(f"adicionales: {', '.join(adicionales)}")
        raise ErrorColumnasDatos("Columnas inválidas; " + "; ".join(partes) + ".")

    if len(columnas) != len(VARIABLES_ESTADISTICAS):
        raise ErrorColumnasDatos(
            "El archivo debe contener exactamente cuatro columnas estadísticas."
        )


def _validar_cantidad_filas(datos: pd.DataFrame) -> None:
    """Valida que el archivo tenga entre 30 y 60 filas."""
    cantidad = len(datos)
    if cantidad == 0:
        raise ErrorCantidadFilas("El archivo no contiene filas de datos.")

    if not cantidad_observaciones_valida(cantidad):
        raise ErrorCantidadFilas(
            "La cantidad de filas debe estar entre "
            f"{MUESTRA_MINIMA} y {MUESTRA_MAXIMA}; se recibieron {cantidad}."
        )


def _validar_sin_nulos(datos: pd.DataFrame) -> None:
    """Valida ausencia de valores nulos e informa columna y filas."""
    mascara = datos.isna()
    if not mascara.any().any():
        return

    detalles = []
    for columna in datos.columns:
        filas = _filas_afectadas(mascara.index[mascara[columna]].tolist())
        if filas:
            detalles.append(f"{columna} en filas {filas}")

    raise ErrorValoresFaltantes(
        "No se permiten valores nulos: " + "; ".join(detalles) + "."
    )


def _normalizar_categorias(
    serie: pd.Series,
    categorias_validas: tuple[str, ...],
    columna: str,
) -> pd.Series:
    """Normaliza espacios y mayúsculas en categorías no ambiguas."""
    mapa = {categoria.casefold(): categoria for categoria in categorias_validas}
    normalizados = serie.astype("string").str.strip()
    claves = normalizados.str.casefold()
    invalidos = ~claves.isin(mapa)

    if invalidos.any():
        filas = _filas_afectadas(serie.index[invalidos].tolist())
        valores = tuple(str(valor) for valor in normalizados[invalidos].unique())
        raise ErrorCategorias(
            f"Columna {columna}: categorías inválidas {valores} en filas {filas}."
        )

    return claves.map(mapa).astype(object)


def _normalizar_enteros_en_rango(
    serie: pd.Series,
    columna: str,
    minimo: int,
    maximo: int,
) -> pd.Series:
    """Convierte una serie a enteros y valida rango sin aceptar decimales."""
    numeros = pd.to_numeric(serie, errors="coerce")
    _validar_numeros_convertibles(numeros, serie, columna)

    finitos = np.isfinite(numeros.to_numpy(dtype=float))
    if not finitos.all():
        filas = _filas_afectadas(serie.index[~finitos].tolist())
        raise ErrorValoresNumericos(
            f"Columna {columna}: no se aceptan valores infinitos en filas {filas}."
        )

    no_enteros = numeros % 1 != 0
    if no_enteros.any():
        filas = _filas_afectadas(serie.index[no_enteros].tolist())
        raise ErrorValoresNumericos(
            f"Columna {columna}: no se aceptan decimales no enteros en filas {filas}."
        )

    fuera_rango = ~numeros.between(minimo, maximo)
    if fuera_rango.any():
        filas = _filas_afectadas(serie.index[fuera_rango].tolist())
        raise ErrorValoresNumericos(
            f"Columna {columna}: valores fuera de rango {minimo}-{maximo} "
            f"en filas {filas}."
        )

    return numeros.astype("int64")


def _normalizar_numeros_en_rango(
    serie: pd.Series,
    columna: str,
    minimo: float,
    maximo: float,
) -> pd.Series:
    """Convierte una serie a números reales y valida valores finitos en rango."""
    numeros = pd.to_numeric(serie, errors="coerce")
    _validar_numeros_convertibles(numeros, serie, columna)

    finitos = np.isfinite(numeros.to_numpy(dtype=float))
    if not finitos.all():
        filas = _filas_afectadas(serie.index[~finitos].tolist())
        raise ErrorValoresNumericos(
            f"Columna {columna}: no se aceptan valores infinitos en filas {filas}."
        )

    fuera_rango = ~numeros.between(minimo, maximo)
    if fuera_rango.any():
        filas = _filas_afectadas(serie.index[fuera_rango].tolist())
        raise ErrorValoresNumericos(
            f"Columna {columna}: valores fuera de rango {minimo:g}-{maximo:g} "
            f"en filas {filas}."
        )

    return numeros.astype("float64")


def _validar_numeros_convertibles(
    numeros: pd.Series,
    serie_original: pd.Series,
    columna: str,
) -> None:
    """Informa valores que no pudieron convertirse a número."""
    no_convertibles = numeros.isna()
    if no_convertibles.any():
        filas = _filas_afectadas(serie_original.index[no_convertibles].tolist())
        raise ErrorValoresNumericos(
            f"Columna {columna}: valores no numéricos en filas {filas}."
        )


def _filas_afectadas(indices: list[object]) -> list[int]:
    """Convierte índices a números de fila de datos, comenzando en 1."""
    filas: list[int] = []
    for indice in indices:
        if isinstance(indice, (int, np.integer)):
            filas.append(int(indice) + 1)
        else:
            filas.append(len(filas) + 1)
    return filas
