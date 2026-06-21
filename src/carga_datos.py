"""Funciones de carga de datos semanales desde Excel o CSV."""

import csv
from pathlib import Path
from typing import BinaryIO

import pandas as pd
from pandas.errors import EmptyDataError, ParserError

from src.validacion_datos import ErrorFormatoArchivo, validar_y_normalizar_datos


def leer_archivo_excel(origen: str | Path | BinaryIO) -> pd.DataFrame:
    """Lee un archivo Excel usando obligatoriamente la hoja datos."""
    try:
        archivo_excel = pd.ExcelFile(origen)
    except ValueError as error:
        raise ErrorFormatoArchivo(
            "No se pudo interpretar el archivo Excel."
        ) from error

    if "datos" not in archivo_excel.sheet_names:
        hojas = ", ".join(archivo_excel.sheet_names)
        raise ErrorFormatoArchivo(
            "El archivo Excel debe contener una hoja llamada 'datos'. "
            f"Hojas encontradas: {hojas}."
        )

    try:
        return pd.read_excel(archivo_excel, sheet_name="datos")
    except ValueError as error:
        raise ErrorFormatoArchivo(
            "No se pudo leer la hoja 'datos' del archivo Excel."
        ) from error


def leer_archivo_csv(origen: str | Path | BinaryIO) -> pd.DataFrame:
    """Lee un CSV UTF-8 detectando separador coma o punto y coma."""
    try:
        return pd.read_csv(
            origen,
            sep=None,
            engine="python",
            encoding="utf-8-sig",
        )
    except UnicodeDecodeError as error:
        raise ErrorFormatoArchivo(
            "No se pudo leer el CSV como UTF-8."
        ) from error
    except EmptyDataError as error:
        raise ErrorFormatoArchivo("El archivo CSV está vacío.") from error
    except csv.Error as error:
        raise ErrorFormatoArchivo(
            "El archivo CSV está vacío o no tiene un separador reconocible."
        ) from error
    except ParserError as error:
        raise ErrorFormatoArchivo(
            "No se pudo interpretar el CSV con separador coma o punto y coma."
        ) from error


def cargar_archivo_semanal(
    origen: str | Path | BinaryIO,
    nombre_archivo: str,
) -> pd.DataFrame:
    """Carga y valida una matriz semanal desde Excel o CSV."""
    extension = Path(nombre_archivo).suffix.lower()

    if extension == ".xlsx":
        datos = leer_archivo_excel(origen)
    elif extension == ".csv":
        datos = leer_archivo_csv(origen)
    else:
        raise ErrorFormatoArchivo(
            "Extensión no admitida. Use archivos .xlsx o .csv."
        )

    return validar_y_normalizar_datos(datos)
