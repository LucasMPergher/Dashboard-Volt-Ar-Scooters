"""Generación reproducible de datos semanales simulados."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

import numpy as np
import pandas as pd

from src.config import (
    ANTIGUEDAD_MAXIMA_MESES,
    ANTIGUEDAD_MINIMA_MESES,
    AUTONOMIA_MAXIMA_KM,
    AUTONOMIA_MINIMA_KM,
    CATEGORIAS_NIVEL_FALLOS,
    CATEGORIAS_SUCURSAL,
    CORRELACION_MAXIMA_ESPERADA,
    CORRELACION_MINIMA_ESPERADA,
    MUESTRA_MAXIMA,
    MUESTRA_MINIMA,
    MUESTRA_PREDETERMINADA,
    PROBABILIDADES_NIVEL_FALLOS,
    SEMILLA_PREDETERMINADA,
    VARIABLES_ESTADISTICAS,
    VARIABLE_ANTIGUEDAD_BATERIA,
    VARIABLE_AUTONOMIA_REAL,
    VARIABLE_NIVEL_FALLOS,
    VARIABLE_SUCURSAL,
)

DESVIACION_ERROR_AUTONOMIA = 4.0


def validar_cantidad(cantidad: int) -> None:
    """Valida que la cantidad de observaciones esté entre 30 y 60."""
    if not MUESTRA_MINIMA <= cantidad <= MUESTRA_MAXIMA:
        raise ValueError(
            "La cantidad de observaciones debe estar entre "
            f"{MUESTRA_MINIMA} y {MUESTRA_MAXIMA}."
        )


def _generar_sucursales(
    cantidad: int,
    generador: np.random.Generator,
) -> list[str]:
    """Genera una lista balanceada de sucursales y mezcla su orden."""
    cantidad_rosario = cantidad // 2
    cantidad_cordoba = cantidad - cantidad_rosario
    sucursales = np.array(
        ["Rosario"] * cantidad_rosario + ["Córdoba"] * cantidad_cordoba,
        dtype=object,
    )
    generador.shuffle(sucursales)
    return sucursales.tolist()


def _generar_niveles_fallos(
    sucursales: Sequence[str],
    generador: np.random.Generator,
) -> list[str]:
    """Genera niveles de fallos con probabilidades condicionadas por sucursal."""
    niveles: list[str] = []
    for sucursal in sucursales:
        nivel = generador.choice(
            CATEGORIAS_NIVEL_FALLOS,
            p=PROBABILIDADES_NIVEL_FALLOS[sucursal],
        )
        niveles.append(str(nivel))

    return niveles


def _generar_antiguedades(
    cantidad: int,
    generador: np.random.Generator,
) -> np.ndarray:
    """Genera antigüedades enteras de batería entre 1 y 48 meses."""
    return generador.integers(
        ANTIGUEDAD_MINIMA_MESES,
        ANTIGUEDAD_MAXIMA_MESES + 1,
        size=cantidad,
    )


def _generar_autonomias(
    antiguedades: np.ndarray,
    generador: np.random.Generator,
) -> np.ndarray:
    """Genera autonomías con relación negativa y error aleatorio normal."""
    errores = generador.normal(
        loc=0.0,
        scale=DESVIACION_ERROR_AUTONOMIA,
        size=len(antiguedades),
    )
    autonomias = 45 - 0.52 * antiguedades + errores
    autonomias = np.clip(autonomias, AUTONOMIA_MINIMA_KM, AUTONOMIA_MAXIMA_KM)
    return np.round(autonomias, 2)


def generar_datos(
    cantidad: int = MUESTRA_PREDETERMINADA,
    semilla: int = SEMILLA_PREDETERMINADA,
) -> pd.DataFrame:
    """Genera un DataFrame semanal reproducible para Volt-Ar Scooters."""
    validar_cantidad(cantidad)
    generador = np.random.default_rng(semilla)

    sucursales = _generar_sucursales(cantidad, generador)
    niveles_fallos = _generar_niveles_fallos(sucursales, generador)
    antiguedades = _generar_antiguedades(cantidad, generador)
    autonomias = _generar_autonomias(antiguedades, generador)

    datos = pd.DataFrame(
        {
            VARIABLE_SUCURSAL: sucursales,
            VARIABLE_NIVEL_FALLOS: niveles_fallos,
            VARIABLE_ANTIGUEDAD_BATERIA: antiguedades.astype(int),
            VARIABLE_AUTONOMIA_REAL: autonomias.astype(float),
        },
        columns=VARIABLES_ESTADISTICAS,
    )
    validar_datos_generados(datos)
    return datos


def calcular_tabla_contingencia(datos: pd.DataFrame) -> pd.DataFrame:
    """Calcula la tabla de contingencia entre sucursal y nivel de fallos."""
    tabla = pd.crosstab(datos[VARIABLE_SUCURSAL], datos[VARIABLE_NIVEL_FALLOS])
    return tabla.reindex(
        index=CATEGORIAS_SUCURSAL,
        columns=CATEGORIAS_NIVEL_FALLOS,
        fill_value=0,
    )


def calcular_frecuencias_esperadas(datos: pd.DataFrame) -> pd.DataFrame:
    """Calcula frecuencias esperadas como control técnico del conjunto generado."""
    tabla = calcular_tabla_contingencia(datos).astype(float)
    total = tabla.to_numpy().sum()
    esperadas = np.outer(tabla.sum(axis=1), tabla.sum(axis=0)) / total
    return pd.DataFrame(esperadas, index=tabla.index, columns=tabla.columns)


def calcular_correlacion_pearson(datos: pd.DataFrame) -> float:
    """Calcula el coeficiente de Pearson entre antigüedad y autonomía."""
    return float(
        datos[VARIABLE_ANTIGUEDAD_BATERIA].corr(datos[VARIABLE_AUTONOMIA_REAL])
    )


def calcular_coeficiente_determinacion(datos: pd.DataFrame) -> float:
    """Calcula R cuadrado como control técnico de la relación lineal."""
    correlacion = calcular_correlacion_pearson(datos)
    return correlacion**2


def contar_autonomias_en_limites(datos: pd.DataFrame) -> dict[str, float]:
    """Cuenta autonomías ubicadas exactamente en los límites del rango."""
    cantidad_minima = int((datos[VARIABLE_AUTONOMIA_REAL] == AUTONOMIA_MINIMA_KM).sum())
    cantidad_maxima = int((datos[VARIABLE_AUTONOMIA_REAL] == AUTONOMIA_MAXIMA_KM).sum())
    total_limites = cantidad_minima + cantidad_maxima
    porcentaje_limites = total_limites / len(datos) * 100

    return {
        "cantidad_15": cantidad_minima,
        "cantidad_45": cantidad_maxima,
        "porcentaje_limites": porcentaje_limites,
    }


def validar_datos_generados(datos: pd.DataFrame) -> None:
    """Valida estructura, categorías, rangos y relación cuantitativa simulada."""
    validar_cantidad(len(datos))

    if tuple(datos.columns) != VARIABLES_ESTADISTICAS:
        raise ValueError("El DataFrame debe tener exactamente cuatro columnas en orden.")

    if datos.isna().any().any():
        raise ValueError("El DataFrame generado no debe contener valores nulos.")

    if not set(datos[VARIABLE_SUCURSAL]).issubset(CATEGORIAS_SUCURSAL):
        raise ValueError("El DataFrame contiene sucursales no válidas.")

    if not set(datos[VARIABLE_NIVEL_FALLOS]).issubset(CATEGORIAS_NIVEL_FALLOS):
        raise ValueError("El DataFrame contiene niveles de fallos no válidos.")

    conteos_sucursal = datos[VARIABLE_SUCURSAL].value_counts()
    if set(conteos_sucursal.index) != set(CATEGORIAS_SUCURSAL):
        raise ValueError("Deben estar presentes las dos sucursales.")

    if conteos_sucursal.max() - conteos_sucursal.min() > 1:
        raise ValueError("La distribución por sucursal debe estar balanceada.")

    if not pd.api.types.is_integer_dtype(datos[VARIABLE_ANTIGUEDAD_BATERIA]):
        raise ValueError("La antigüedad de batería debe ser entera.")

    if not datos[VARIABLE_ANTIGUEDAD_BATERIA].between(
        ANTIGUEDAD_MINIMA_MESES,
        ANTIGUEDAD_MAXIMA_MESES,
    ).all():
        raise ValueError("La antigüedad debe estar entre 1 y 48 meses.")

    if not pd.api.types.is_numeric_dtype(datos[VARIABLE_AUTONOMIA_REAL]):
        raise ValueError("La autonomía real debe ser numérica.")

    if not datos[VARIABLE_AUTONOMIA_REAL].between(
        AUTONOMIA_MINIMA_KM,
        AUTONOMIA_MAXIMA_KM,
    ).all():
        raise ValueError("La autonomía real debe estar entre 15 y 45 kilómetros.")

    if datos[VARIABLE_ANTIGUEDAD_BATERIA].nunique() <= 1:
        raise ValueError("La antigüedad debe presentar variabilidad.")

    if datos[VARIABLE_AUTONOMIA_REAL].nunique() <= 1:
        raise ValueError("La autonomía debe presentar variabilidad.")

    correlacion = calcular_correlacion_pearson(datos)
    if not -1.0 < correlacion < 0.0:
        raise ValueError("La correlación debe ser negativa y no perfecta.")


def validar_control_predeterminado(datos: pd.DataFrame) -> pd.DataFrame:
    """Valida controles cualitativos y correlación del conjunto predeterminado."""
    niveles_presentes = set(datos[VARIABLE_NIVEL_FALLOS])
    if niveles_presentes != set(CATEGORIAS_NIVEL_FALLOS):
        raise ValueError("Deben estar presentes Bajo, Medio y Alto.")

    esperadas = calcular_frecuencias_esperadas(datos)
    proporcion_mayores_igual_cinco = float((esperadas >= 5).to_numpy().mean())

    if (esperadas < 1).any().any():
        raise ValueError("Ninguna frecuencia esperada debe ser menor que 1.")

    if proporcion_mayores_igual_cinco < 0.80:
        raise ValueError(
            "Al menos el 80 % de las frecuencias esperadas debe ser mayor o igual a 5."
        )

    correlacion = calcular_correlacion_pearson(datos)
    if not CORRELACION_MINIMA_ESPERADA <= correlacion <= CORRELACION_MAXIMA_ESPERADA:
        raise ValueError(
            "La correlación predeterminada debe estar aproximadamente entre "
            f"{CORRELACION_MINIMA_ESPERADA} y {CORRELACION_MAXIMA_ESPERADA}."
        )

    return esperadas


def guardar_excel(datos: pd.DataFrame, ruta_salida: Path) -> Path:
    """Guarda los datos simulados en un Excel con hoja llamada datos."""
    validar_datos_generados(datos)
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    datos.to_excel(ruta_salida, sheet_name="datos", index=False)
    return ruta_salida


def construir_ruta_salida(semana: int, directorio: Path = Path("data")) -> Path:
    """Construye la ruta de salida usando la semana como parte del nombre."""
    if semana < 1:
        raise ValueError("La semana debe ser un entero positivo.")

    return directorio / f"volt_ar_semana_{semana:02d}.xlsx"


def crear_parser() -> argparse.ArgumentParser:
    """Crea el parser de argumentos para la interfaz de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Genera datos semanales simulados para Volt-Ar Scooters."
    )
    parser.add_argument("--cantidad", type=int, default=MUESTRA_PREDETERMINADA)
    parser.add_argument("--semilla", type=int, default=SEMILLA_PREDETERMINADA)
    parser.add_argument("--semana", type=int, required=True)
    return parser


def main(argumentos: Sequence[str] | None = None) -> int:
    """Ejecuta la generación del archivo semanal desde la terminal."""
    parser = crear_parser()
    opciones = parser.parse_args(argumentos)

    datos = generar_datos(cantidad=opciones.cantidad, semilla=opciones.semilla)
    if (
        opciones.cantidad == MUESTRA_PREDETERMINADA
        and opciones.semilla == SEMILLA_PREDETERMINADA
    ):
        validar_control_predeterminado(datos)

    ruta_salida = construir_ruta_salida(opciones.semana)
    guardar_excel(datos, ruta_salida)
    print(f"Archivo generado: {ruta_salida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
