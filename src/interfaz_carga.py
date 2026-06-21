"""Componente de interfaz para cargar y mantener datos semanales activos."""

from pathlib import Path

import pandas as pd
import streamlit as st

from src.carga_datos import cargar_archivo_semanal
from src.config import VARIABLES_ESTADISTICAS
from src.validacion_datos import ErrorDatos

RUTA_DATOS_PREDETERMINADOS = Path("data/volt_ar_semana_01.xlsx")
CLAVE_DATOS_ACTIVOS = "datos_activos"
CLAVE_NOMBRE_ARCHIVO_ACTIVO = "nombre_archivo_activo"


def cargar_datos_predeterminados() -> pd.DataFrame:
    """Carga el archivo semanal predeterminado validado."""
    return cargar_archivo_semanal(
        RUTA_DATOS_PREDETERMINADOS,
        RUTA_DATOS_PREDETERMINADOS.name,
    )


def garantizar_datos_activos() -> pd.DataFrame:
    """Garantiza que exista un DataFrame activo en session_state."""
    if CLAVE_DATOS_ACTIVOS not in st.session_state:
        datos = cargar_datos_predeterminados()
        st.session_state[CLAVE_DATOS_ACTIVOS] = datos
        st.session_state[CLAVE_NOMBRE_ARCHIVO_ACTIVO] = (
            RUTA_DATOS_PREDETERMINADOS.name
        )

    return st.session_state[CLAVE_DATOS_ACTIVOS]


def mostrar_carga_datos() -> pd.DataFrame | None:
    """Renderiza el componente de carga y devuelve los datos activos."""
    with st.sidebar:
        st.header("Datos semanales")
        _mostrar_uploader()
        _mostrar_boton_predeterminado()

    try:
        datos = garantizar_datos_activos()
    except ErrorDatos as error:
        st.error(f"No se pudieron cargar los datos predeterminados: {error}")
        return None

    nombre_archivo = st.session_state.get(
        CLAVE_NOMBRE_ARCHIVO_ACTIVO,
        RUTA_DATOS_PREDETERMINADOS.name,
    )
    _mostrar_resumen_datos(datos, nombre_archivo)
    return datos


def _mostrar_uploader() -> None:
    """Muestra el uploader y actualiza datos activos solo si el archivo es válido."""
    archivo = st.file_uploader(
        "Cargar actualización semanal",
        type=["xlsx", "csv"],
        help="El archivo debe contener exactamente las cuatro variables estadísticas.",
    )

    if archivo is None:
        return

    try:
        datos = cargar_archivo_semanal(archivo, archivo.name)
    except ErrorDatos as error:
        st.error(f"Archivo inválido: {error}")
        return

    st.session_state[CLAVE_DATOS_ACTIVOS] = datos
    st.session_state[CLAVE_NOMBRE_ARCHIVO_ACTIVO] = archivo.name
    st.success(f"Archivo cargado y validado: {archivo.name}")


def _mostrar_boton_predeterminado() -> None:
    """Permite volver al archivo predeterminado."""
    if not st.button("Volver a datos predeterminados"):
        return

    try:
        datos = cargar_datos_predeterminados()
    except ErrorDatos as error:
        st.error(f"No se pudieron restaurar los datos predeterminados: {error}")
        return

    st.session_state[CLAVE_DATOS_ACTIVOS] = datos
    st.session_state[CLAVE_NOMBRE_ARCHIVO_ACTIVO] = RUTA_DATOS_PREDETERMINADOS.name
    st.success("Se restauraron los datos predeterminados.")


def _mostrar_resumen_datos(datos: pd.DataFrame, nombre_archivo: str) -> None:
    """Muestra nombre, cantidad, variables y vista previa del conjunto activo."""
    st.subheader("Datos activos")
    st.write(f"Archivo activo: `{nombre_archivo}`")
    st.write(f"Cantidad de observaciones: `{len(datos)}`")
    st.write("Variables detectadas:")
    st.write(", ".join(f"`{columna}`" for columna in VARIABLES_ESTADISTICAS))
    st.dataframe(datos.head(10), use_container_width=True)
