"""Funciones de carga de datos para archivos Excel."""

from pathlib import Path

import pandas as pd


def cargar_excel(ruta_archivo: str | Path) -> pd.DataFrame:
    """Carga un archivo Excel para etapas futuras de validación y análisis."""
    return pd.read_excel(ruta_archivo)
