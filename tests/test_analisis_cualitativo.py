"""Pruebas iniciales asociadas a la configuración cualitativa."""

from src.config import (
    CATEGORIAS_NIVEL_FALLOS,
    CATEGORIAS_SUCURSAL,
    ESCALAS_VARIABLES,
    VARIABLE_NIVEL_FALLOS,
    VARIABLE_SUCURSAL,
)


def test_categorias_permitidas_para_sucursal() -> None:
    """Comprueba las categorías nominales previstas para sucursal."""
    assert CATEGORIAS_SUCURSAL == ("Rosario", "Córdoba")


def test_categorias_permitidas_para_nivel_de_fallos() -> None:
    """Comprueba las categorías ordinales previstas para nivel de fallos."""
    assert CATEGORIAS_NIVEL_FALLOS == ("Bajo", "Medio", "Alto")


def test_escalas_cualitativas_declaradas() -> None:
    """Verifica que las variables cualitativas tengan su escala correcta."""
    assert ESCALAS_VARIABLES[VARIABLE_SUCURSAL] == "nominal"
    assert ESCALAS_VARIABLES[VARIABLE_NIVEL_FALLOS] == "ordinal"
