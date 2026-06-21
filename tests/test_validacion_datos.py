"""Pruebas de validación de estructura de datos."""

from src.config import COLUMNAS_ESPERADAS, MUESTRA_MAXIMA, MUESTRA_MINIMA
from src.validacion_datos import (
    cantidad_observaciones_valida,
    obtener_columnas_esperadas,
    obtener_columnas_faltantes,
)


def test_columnas_esperadas_incluyen_identificador_y_variables() -> None:
    """Comprueba que los nombres de columnas esperados sean estables."""
    assert obtener_columnas_esperadas() == COLUMNAS_ESPERADAS


def test_columnas_faltantes_no_exige_identificador_por_defecto() -> None:
    """Verifica que el identificador no se trate como variable estadística."""
    columnas = (
        "Sucursal",
        "Nivel_Fallos",
        "Antiguedad_Bateria_Meses",
        "Autonomia_Real_Km",
    )

    assert obtener_columnas_faltantes(columnas) == ()


def test_columnas_faltantes_detecta_variables_requeridas() -> None:
    """Detecta la ausencia de columnas estadisticas requeridas."""
    columnas = ("Sucursal", "Nivel_Fallos")

    assert obtener_columnas_faltantes(columnas) == (
        "Antiguedad_Bateria_Meses",
        "Autonomia_Real_Km",
    )


def test_cantidad_observaciones_respeta_limites() -> None:
    """Valida los extremos permitidos para la muestra semanal."""
    assert cantidad_observaciones_valida(MUESTRA_MINIMA)
    assert cantidad_observaciones_valida(MUESTRA_MAXIMA)
    assert not cantidad_observaciones_valida(MUESTRA_MINIMA - 1)
    assert not cantidad_observaciones_valida(MUESTRA_MAXIMA + 1)
