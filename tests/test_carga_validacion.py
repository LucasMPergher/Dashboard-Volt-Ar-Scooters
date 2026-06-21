"""Pruebas de carga y validación de archivos semanales."""

from io import BytesIO

import numpy as np
import pandas as pd
import pytest

from src.carga_datos import (
    cargar_archivo_semanal,
    leer_archivo_csv,
    leer_archivo_excel,
)
from src.config import VARIABLES_ESTADISTICAS
from src.validacion_datos import (
    ErrorCantidadFilas,
    ErrorCategorias,
    ErrorColumnasDatos,
    ErrorFormatoArchivo,
    ErrorValoresFaltantes,
    ErrorValoresNumericos,
    validar_y_normalizar_datos,
)


def _datos_validos(cantidad: int = 48) -> pd.DataFrame:
    """Construye un DataFrame válido para pruebas de carga."""
    sucursales = ["Rosario", "Córdoba"] * ((cantidad + 1) // 2)
    niveles = ["Bajo", "Medio", "Alto"] * ((cantidad + 2) // 3)
    antiguedades = list(range(1, 49)) * ((cantidad + 47) // 48)
    autonomias = [30.5, 32.0, 28.75, 35.2] * ((cantidad + 3) // 4)

    return pd.DataFrame(
        {
            "Sucursal": sucursales[:cantidad],
            "Nivel_Fallos": niveles[:cantidad],
            "Antiguedad_Bateria_Meses": antiguedades[:cantidad],
            "Autonomia_Real_Km": autonomias[:cantidad],
        },
        columns=VARIABLES_ESTADISTICAS,
    )


def _excel_en_memoria(datos: pd.DataFrame, hoja: str = "datos") -> BytesIO:
    """Crea un archivo Excel en memoria."""
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as escritor:
        datos.to_excel(escritor, sheet_name=hoja, index=False)
    buffer.seek(0)
    return buffer


def _csv_en_memoria(datos: pd.DataFrame, separador: str = ",") -> BytesIO:
    """Crea un archivo CSV UTF-8 en memoria."""
    contenido = datos.to_csv(index=False, sep=separador).encode("utf-8")
    return BytesIO(contenido)


def test_lectura_de_excel_valido() -> None:
    """Lee un Excel válido desde la hoja datos."""
    archivo = _excel_en_memoria(_datos_validos())

    datos = leer_archivo_excel(archivo)

    assert datos.shape == (48, 4)


def test_lectura_de_csv_valido_con_coma() -> None:
    """Lee un CSV válido separado por coma."""
    archivo = _csv_en_memoria(_datos_validos(), ",")

    datos = leer_archivo_csv(archivo)

    assert datos.shape == (48, 4)


def test_lectura_de_csv_valido_con_punto_y_coma() -> None:
    """Lee un CSV válido separado por punto y coma."""
    archivo = _csv_en_memoria(_datos_validos(), ";")

    datos = leer_archivo_csv(archivo)

    assert datos.shape == (48, 4)


def test_conservacion_de_las_cuatro_columnas() -> None:
    """La carga semanal conserva exactamente las cuatro columnas."""
    archivo = _excel_en_memoria(_datos_validos())

    datos = cargar_archivo_semanal(archivo, "semana.xlsx")

    assert tuple(datos.columns) == VARIABLES_ESTADISTICAS


def test_reordenamiento_al_orden_canonico() -> None:
    """Columnas válidas en otro orden se reordenan al orden canónico."""
    datos_desordenados = _datos_validos()[
        [
            "Autonomia_Real_Km",
            "Sucursal",
            "Antiguedad_Bateria_Meses",
            "Nivel_Fallos",
        ]
    ]

    normalizados = validar_y_normalizar_datos(datos_desordenados)

    assert tuple(normalizados.columns) == VARIABLES_ESTADISTICAS


def test_excel_sin_hoja_datos() -> None:
    """Un Excel sin hoja datos debe informar las hojas encontradas."""
    archivo = _excel_en_memoria(_datos_validos(), hoja="otra_hoja")

    with pytest.raises(ErrorFormatoArchivo, match="hoja llamada 'datos'"):
        leer_archivo_excel(archivo)


def test_extension_no_admitida() -> None:
    """Solo se aceptan archivos .xlsx o .csv."""
    with pytest.raises(ErrorFormatoArchivo, match="Extensión no admitida"):
        cargar_archivo_semanal(BytesIO(b"contenido"), "datos.txt")


def test_archivo_vacio() -> None:
    """Un archivo CSV vacío debe rechazarse claramente."""
    with pytest.raises(ErrorFormatoArchivo, match="vacío"):
        cargar_archivo_semanal(BytesIO(b""), "datos.csv")


def test_columna_faltante() -> None:
    """Debe rechazarse una columna requerida faltante."""
    datos = _datos_validos().drop(columns=["Sucursal"])

    with pytest.raises(ErrorColumnasDatos, match="faltantes: Sucursal"):
        validar_y_normalizar_datos(datos)


def test_columna_adicional() -> None:
    """Debe rechazarse una columna adicional."""
    datos = _datos_validos()
    datos["Semana"] = 1

    with pytest.raises(ErrorColumnasDatos, match="adicionales: Semana"):
        validar_y_normalizar_datos(datos)


def test_columna_unnamed() -> None:
    """Debe rechazarse una columna Unnamed."""
    datos = _datos_validos()
    datos["Unnamed: 0"] = range(len(datos))

    with pytest.raises(ErrorColumnasDatos, match="Unnamed"):
        validar_y_normalizar_datos(datos)


def test_menos_de_30_filas() -> None:
    """Debe rechazarse un archivo con menos de 30 filas."""
    with pytest.raises(ErrorCantidadFilas, match="entre 30 y 60"):
        validar_y_normalizar_datos(_datos_validos(29))


def test_mas_de_60_filas() -> None:
    """Debe rechazarse un archivo con más de 60 filas."""
    with pytest.raises(ErrorCantidadFilas, match="entre 30 y 60"):
        validar_y_normalizar_datos(_datos_validos(61))


def test_valores_nulos() -> None:
    """No se permiten valores nulos."""
    datos = _datos_validos()
    datos.loc[0, "Sucursal"] = None

    with pytest.raises(ErrorValoresFaltantes, match="Sucursal"):
        validar_y_normalizar_datos(datos)


def test_sucursal_invalida() -> None:
    """No se corrigen automáticamente sucursales desconocidas."""
    datos = _datos_validos()
    datos.loc[0, "Sucursal"] = "Mendoza"

    with pytest.raises(ErrorCategorias, match="Sucursal"):
        validar_y_normalizar_datos(datos)


def test_nivel_de_fallos_invalido() -> None:
    """No se corrigen automáticamente niveles desconocidos."""
    datos = _datos_validos()
    datos.loc[0, "Nivel_Fallos"] = "Crítico"

    with pytest.raises(ErrorCategorias, match="Nivel_Fallos"):
        validar_y_normalizar_datos(datos)


def test_normalizacion_de_mayusculas_y_espacios() -> None:
    """Normaliza espacios y diferencias de mayúsculas/minúsculas."""
    datos = _datos_validos()
    datos.loc[0, "Sucursal"] = " rosario "
    datos.loc[1, "Sucursal"] = " CÓRDOBA "
    datos.loc[0, "Nivel_Fallos"] = " bajo "
    datos.loc[1, "Nivel_Fallos"] = " ALTO "

    normalizados = validar_y_normalizar_datos(datos)

    assert normalizados.loc[0, "Sucursal"] == "Rosario"
    assert normalizados.loc[1, "Sucursal"] == "Córdoba"
    assert normalizados.loc[0, "Nivel_Fallos"] == "Bajo"
    assert normalizados.loc[1, "Nivel_Fallos"] == "Alto"


def test_antiguedad_decimal_no_entera() -> None:
    """La antigüedad no acepta decimales no enteros."""
    datos = _datos_validos()
    datos["Antiguedad_Bateria_Meses"] = datos[
        "Antiguedad_Bateria_Meses"
    ].astype(object)
    datos.loc[0, "Antiguedad_Bateria_Meses"] = 10.5

    with pytest.raises(ErrorValoresNumericos, match="decimales"):
        validar_y_normalizar_datos(datos)


def test_antiguedad_fuera_de_rango() -> None:
    """La antigüedad debe estar entre 1 y 48."""
    datos = _datos_validos()
    datos.loc[0, "Antiguedad_Bateria_Meses"] = 49

    with pytest.raises(ErrorValoresNumericos, match="Antiguedad_Bateria_Meses"):
        validar_y_normalizar_datos(datos)


def test_autonomia_fuera_de_rango() -> None:
    """La autonomía debe estar entre 15 y 45."""
    datos = _datos_validos()
    datos.loc[0, "Autonomia_Real_Km"] = 46

    with pytest.raises(ErrorValoresNumericos, match="Autonomia_Real_Km"):
        validar_y_normalizar_datos(datos)


def test_valores_infinitos() -> None:
    """No se aceptan valores infinitos."""
    datos = _datos_validos()
    datos.loc[0, "Autonomia_Real_Km"] = np.inf

    with pytest.raises(ErrorValoresNumericos, match="infinitos"):
        validar_y_normalizar_datos(datos)


def test_dataframe_original_no_se_modifica() -> None:
    """La validación debe devolver una copia sin modificar el DataFrame original."""
    datos = _datos_validos()
    datos.loc[0, "Sucursal"] = " rosario "
    copia_original = datos.copy(deep=True)

    normalizados = validar_y_normalizar_datos(datos)

    pd.testing.assert_frame_equal(datos, copia_original)
    assert normalizados.loc[0, "Sucursal"] == "Rosario"


def test_archivo_invalido_no_se_considera_valido() -> None:
    """Un archivo inválido debe lanzar error y no devolver un DataFrame normalizado."""
    datos = _datos_validos()
    datos.loc[0, "Nivel_Fallos"] = "Inexistente"
    archivo = _csv_en_memoria(datos)

    with pytest.raises(ErrorCategorias):
        cargar_archivo_semanal(archivo, "datos.csv")
