"""Pruebas iniciales asociadas a la configuración cuantitativa."""

from src.config import (
    ESCALAS_VARIABLES,
    TIPOS_VARIABLES,
    VARIABLE_ANTIGUEDAD_BATERIA,
    VARIABLE_AUTONOMIA_REAL,
    VARIABLES_ESTADISTICAS,
)


def test_exactamente_cuatro_variables_estadisticas() -> None:
    """Comprueba que el identificador no se cuente como variable estadística."""
    assert VARIABLES_ESTADISTICAS == (
        "Sucursal",
        "Nivel_Fallos",
        "Antiguedad_Bateria_Meses",
        "Autonomia_Real_Km",
    )
    assert len(VARIABLES_ESTADISTICAS) == 4
    assert "ID_Monopatin" not in VARIABLES_ESTADISTICAS


def test_variables_cuantitativas_declaradas() -> None:
    """Verifica el tipo de las variables X e Y del análisis cuantitativo."""
    assert TIPOS_VARIABLES[VARIABLE_ANTIGUEDAD_BATERIA] == "cuantitativa"
    assert TIPOS_VARIABLES[VARIABLE_AUTONOMIA_REAL] == "cuantitativa"


def test_escalas_cuantitativas_declaradas() -> None:
    """Verifica que las variables cuantitativas usen escala de razón."""
    assert ESCALAS_VARIABLES[VARIABLE_ANTIGUEDAD_BATERIA] == "razón"
    assert ESCALAS_VARIABLES[VARIABLE_AUTONOMIA_REAL] == "razón"
