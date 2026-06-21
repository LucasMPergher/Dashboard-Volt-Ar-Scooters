"""Configuración central del proyecto académico."""

from typing import Final


NOMBRE_PROYECTO: Final[str] = "Dashboard Volt-Ar Scooters"

COLUMNA_IDENTIFICADOR: Final[str] = "ID_Monopatin"

VARIABLE_SUCURSAL: Final[str] = "Sucursal"
VARIABLE_NIVEL_FALLOS: Final[str] = "Nivel_Fallos"
VARIABLE_ANTIGUEDAD_BATERIA: Final[str] = "Antiguedad_Bateria_Meses"
VARIABLE_AUTONOMIA_REAL: Final[str] = "Autonomia_Real_Km"

VARIABLES_ESTADISTICAS: Final[tuple[str, ...]] = (
    VARIABLE_SUCURSAL,
    VARIABLE_NIVEL_FALLOS,
    VARIABLE_ANTIGUEDAD_BATERIA,
    VARIABLE_AUTONOMIA_REAL,
)

COLUMNAS_ESPERADAS: Final[tuple[str, ...]] = (
    COLUMNA_IDENTIFICADOR,
    *VARIABLES_ESTADISTICAS,
)

CATEGORIAS_SUCURSAL: Final[tuple[str, ...]] = ("Rosario", "Córdoba")
CATEGORIAS_NIVEL_FALLOS: Final[tuple[str, ...]] = ("Bajo", "Medio", "Alto")

MUESTRA_MINIMA: Final[int] = 30
MUESTRA_MAXIMA: Final[int] = 60
MUESTRA_PREDETERMINADA: Final[int] = 48
SEMILLA_PREDETERMINADA: Final[int] = 42

ANTIGUEDAD_MINIMA_MESES: Final[int] = 1
ANTIGUEDAD_MAXIMA_MESES: Final[int] = 48
AUTONOMIA_MINIMA_KM: Final[float] = 15.0
AUTONOMIA_MAXIMA_KM: Final[float] = 45.0

PROBABILIDADES_NIVEL_FALLOS: Final[dict[str, tuple[float, float, float]]] = {
    "Rosario": (0.20, 0.35, 0.45),
    "Córdoba": (0.55, 0.35, 0.10),
}

CORRELACION_MINIMA_ESPERADA: Final[float] = -0.95
CORRELACION_MAXIMA_ESPERADA: Final[float] = -0.55

TIPOS_VARIABLES: Final[dict[str, str]] = {
    VARIABLE_SUCURSAL: "cualitativa",
    VARIABLE_NIVEL_FALLOS: "cualitativa",
    VARIABLE_ANTIGUEDAD_BATERIA: "cuantitativa",
    VARIABLE_AUTONOMIA_REAL: "cuantitativa",
}

ESCALAS_VARIABLES: Final[dict[str, str]] = {
    VARIABLE_SUCURSAL: "nominal",
    VARIABLE_NIVEL_FALLOS: "ordinal",
    VARIABLE_ANTIGUEDAD_BATERIA: "razón",
    VARIABLE_AUTONOMIA_REAL: "razón",
}
