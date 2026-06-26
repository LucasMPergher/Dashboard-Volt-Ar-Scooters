"""Análisis cuantitativo descriptivo y muestral."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import norm, pearsonr

from src.config import (
    ANTIGUEDAD_MAXIMA_MESES,
    ANTIGUEDAD_MINIMA_MESES,
    VARIABLE_ANTIGUEDAD_BATERIA,
    VARIABLE_AUTONOMIA_REAL,
)


class ErrorAnalisisCuantitativo(ValueError):
    """Error controlado para análisis cuantitativo no calculable."""


@dataclass(frozen=True)
class ResultadoRegresionMuestral:
    """Resultado descriptivo de una regresión lineal muestral."""

    cantidad: int
    intercepto: float
    pendiente: float
    coeficiente_pearson: float
    coeficiente_determinacion: float
    valores_ajustados: pd.Series
    residuos: pd.Series


@dataclass(frozen=True)
class ResultadoInferenciaRegresion:
    """Resultado inferencial de la regresión lineal simple."""

    cantidad: int
    grados_libertad: int
    intercepto: float
    pendiente: float
    error_estandar_intercepto: float
    error_estandar_pendiente: float
    estadistico_t_pendiente: float
    p_valor_pendiente: float
    coeficiente_pearson: float
    coeficiente_determinacion: float
    intervalo_intercepto: tuple[float, float]
    intervalo_pendiente: tuple[float, float]
    intervalo_correlacion: tuple[float, float] | None
    nivel_confianza: float


@dataclass(frozen=True)
class ResultadoPrediccion:
    """Resultado de predicción para un valor de antigüedad."""

    valor_x: float
    prediccion_puntual: float
    limite_inferior_media: float
    limite_superior_media: float
    limite_inferior_individual: float
    limite_superior_individual: float
    nivel_confianza: float
    es_extrapolacion: bool
    minimo_x_observado: float
    maximo_x_observado: float


def ajustar_regresion_lineal(
    datos: pd.DataFrame,
    columna_x: str = VARIABLE_ANTIGUEDAD_BATERIA,
    columna_y: str = VARIABLE_AUTONOMIA_REAL,
) -> ResultadoRegresionMuestral:
    """Ajusta una regresión lineal muestral con intercepto."""
    x, y, modelo = _ajustar_modelo_ols(datos, columna_x, columna_y)
    coeficiente_pearson = float(pearsonr(x, y).statistic)
    coeficiente_determinacion = float(modelo.rsquared)

    valores_ajustados = pd.Series(
        modelo.fittedvalues,
        index=datos.index,
        name="Autonomia_Ajustada_Km",
    )
    residuos = pd.Series(
        modelo.resid,
        index=datos.index,
        name="Residuo_Km",
    )

    return ResultadoRegresionMuestral(
        cantidad=len(datos),
        intercepto=float(modelo.params["const"]),
        pendiente=float(modelo.params[columna_x]),
        coeficiente_pearson=coeficiente_pearson,
        coeficiente_determinacion=coeficiente_determinacion,
        valores_ajustados=valores_ajustados,
        residuos=residuos,
    )


def ajustar_inferencia_regresion(
    datos: pd.DataFrame,
    nivel_confianza: float = 0.95,
    columna_x: str = VARIABLE_ANTIGUEDAD_BATERIA,
    columna_y: str = VARIABLE_AUTONOMIA_REAL,
) -> ResultadoInferenciaRegresion:
    """Ajusta la regresión y devuelve resultados inferenciales."""
    _validar_nivel_confianza(nivel_confianza)
    x, y, modelo = _ajustar_modelo_ols(
        datos,
        columna_x,
        columna_y,
        cantidad_minima=4,
    )
    cantidad = len(datos)
    grados_libertad = int(modelo.df_resid)
    if grados_libertad <= 0:
        raise ErrorAnalisisCuantitativo(
            "La regresión requiere grados de libertad positivos."
        )

    coeficiente_pearson = float(pearsonr(x, y).statistic)
    alpha_intervalo = 1 - nivel_confianza
    intervalos = modelo.conf_int(alpha=alpha_intervalo)

    return ResultadoInferenciaRegresion(
        cantidad=cantidad,
        grados_libertad=grados_libertad,
        intercepto=float(modelo.params["const"]),
        pendiente=float(modelo.params[columna_x]),
        error_estandar_intercepto=float(modelo.bse["const"]),
        error_estandar_pendiente=float(modelo.bse[columna_x]),
        estadistico_t_pendiente=float(modelo.tvalues[columna_x]),
        p_valor_pendiente=float(modelo.pvalues[columna_x]),
        coeficiente_pearson=coeficiente_pearson,
        coeficiente_determinacion=float(modelo.rsquared),
        intervalo_intercepto=(
            float(intervalos.loc["const", 0]),
            float(intervalos.loc["const", 1]),
        ),
        intervalo_pendiente=(
            float(intervalos.loc[columna_x, 0]),
            float(intervalos.loc[columna_x, 1]),
        ),
        intervalo_correlacion=calcular_intervalo_correlacion_fisher(
            coeficiente_pearson,
            cantidad,
            nivel_confianza,
        ),
        nivel_confianza=nivel_confianza,
    )


def calcular_prediccion(
    datos: pd.DataFrame,
    valor_x: float,
    nivel_confianza: float = 0.95,
    columna_x: str = VARIABLE_ANTIGUEDAD_BATERIA,
    columna_y: str = VARIABLE_AUTONOMIA_REAL,
) -> ResultadoPrediccion:
    """Calcula predicción puntual e intervalos para un valor de X."""
    _validar_nivel_confianza(nivel_confianza)
    valor_x_validado = _validar_valor_x_operativo(valor_x)
    x, _, modelo = _ajustar_modelo_ols(
        datos,
        columna_x,
        columna_y,
        cantidad_minima=4,
    )
    minimo_x_observado = float(x.min())
    maximo_x_observado = float(x.max())
    nuevos_datos = _construir_exog_prediccion(valor_x_validado, columna_x)
    resumen = modelo.get_prediction(nuevos_datos).summary_frame(
        alpha=1 - nivel_confianza
    )
    fila = resumen.iloc[0]

    return ResultadoPrediccion(
        valor_x=valor_x_validado,
        prediccion_puntual=float(fila["mean"]),
        limite_inferior_media=float(fila["mean_ci_lower"]),
        limite_superior_media=float(fila["mean_ci_upper"]),
        limite_inferior_individual=float(fila["obs_ci_lower"]),
        limite_superior_individual=float(fila["obs_ci_upper"]),
        nivel_confianza=nivel_confianza,
        es_extrapolacion=not minimo_x_observado
        <= valor_x_validado
        <= maximo_x_observado,
        minimo_x_observado=minimo_x_observado,
        maximo_x_observado=maximo_x_observado,
    )


def construir_bandas_prediccion(
    datos: pd.DataFrame,
    nivel_confianza: float = 0.95,
    columna_x: str = VARIABLE_ANTIGUEDAD_BATERIA,
    columna_y: str = VARIABLE_AUTONOMIA_REAL,
    cantidad_puntos: int = 100,
) -> pd.DataFrame:
    """Construye recta e intervalos para graficar la predicción."""
    _validar_nivel_confianza(nivel_confianza)
    if cantidad_puntos < 2:
        raise ErrorAnalisisCuantitativo(
            "Se requieren al menos dos puntos para graficar la predicción."
        )

    x, _, modelo = _ajustar_modelo_ols(
        datos,
        columna_x,
        columna_y,
        cantidad_minima=4,
    )
    valores_x = np.linspace(float(x.min()), float(x.max()), cantidad_puntos)
    nuevos_datos = pd.DataFrame(
        {
            "const": np.ones(cantidad_puntos),
            columna_x: valores_x,
        }
    )
    resumen = modelo.get_prediction(nuevos_datos).summary_frame(
        alpha=1 - nivel_confianza
    )
    return pd.DataFrame(
        {
            columna_x: valores_x,
            "prediccion_puntual": resumen["mean"].to_numpy(dtype=float),
            "media_inferior": resumen["mean_ci_lower"].to_numpy(dtype=float),
            "media_superior": resumen["mean_ci_upper"].to_numpy(dtype=float),
            "individual_inferior": resumen["obs_ci_lower"].to_numpy(dtype=float),
            "individual_superior": resumen["obs_ci_upper"].to_numpy(dtype=float),
        }
    )


def calcular_ancho_intervalo(limite_inferior: float, limite_superior: float) -> float:
    """Calcula el ancho de un intervalo."""
    return float(limite_superior - limite_inferior)


def calcular_intervalo_correlacion_fisher(
    coeficiente_pearson: float,
    cantidad: int,
    nivel_confianza: float = 0.95,
) -> tuple[float, float] | None:
    """Calcula un intervalo para rho mediante la aproximación de Fisher."""
    _validar_pearson(coeficiente_pearson)
    _validar_nivel_confianza(nivel_confianza)
    if cantidad <= 3:
        return None

    if abs(coeficiente_pearson) >= 1:
        return None

    error_estandar_z = 1 / np.sqrt(cantidad - 3)
    z_observado = np.arctanh(coeficiente_pearson)
    z_critico = norm.ppf(1 - (1 - nivel_confianza) / 2)
    limite_inferior = np.tanh(z_observado - z_critico * error_estandar_z)
    limite_superior = np.tanh(z_observado + z_critico * error_estandar_z)
    return (
        float(np.clip(limite_inferior, -1, 1)),
        float(np.clip(limite_superior, -1, 1)),
    )


def decidir_prueba_pendiente(p_valor: float, alpha: float) -> str:
    """Aplica la regla de decisión bilateral para la pendiente."""
    if p_valor < alpha:
        return "Se rechaza H₀."

    return "No se rechaza H₀."


def concluir_prueba_pendiente(
    p_valor: float,
    alpha: float,
    pendiente: float,
) -> str:
    """Genera una conclusión inferencial contextual para la pendiente."""
    alpha_formateado = f"{alpha:.2f}"
    if p_valor < alpha:
        sentido = "negativa" if pendiente < 0 else "positiva"
        return (
            f"Con un nivel de significancia de {alpha_formateado}, se rechaza "
            "H₀. Existe evidencia estadísticamente significativa de una "
            f"relación lineal {sentido} entre la antigüedad de la batería y la "
            "autonomía real en la población simulada de monopatines Volt-Ar. "
            "La conclusión corresponde al escenario poblacional simulado con "
            "fines académicos."
        )

    return (
        f"Con un nivel de significancia de {alpha_formateado}, no se rechaza "
        "H₀. Los datos no proporcionan evidencia suficiente para afirmar que "
        "exista una relación lineal poblacional entre la antigüedad y la "
        "autonomía. La conclusión corresponde al escenario poblacional "
        "simulado con fines académicos."
    )


def interpretar_correlacion_muestral(coeficiente: float) -> str:
    """Interpreta Pearson de forma descriptiva para la muestra semanal."""
    _validar_pearson(coeficiente)
    magnitud = abs(coeficiente)
    intensidad = _clasificar_intensidad_correlacion(magnitud)

    if magnitud < 1e-12:
        return (
            "En la muestra semanal no se observa una dirección lineal apreciable."
        )

    sentido = "positiva" if coeficiente > 0 else "negativa"
    return (
        "En la muestra semanal se observa una relación lineal "
        f"{sentido} {intensidad}."
    )


def interpretar_r_cuadrado_muestral(coeficiente_determinacion: float) -> str:
    """Interpreta R² como porcentaje descriptivo de variabilidad muestral."""
    _validar_r_cuadrado(coeficiente_determinacion)
    porcentaje = coeficiente_determinacion * 100
    return (
        "En la muestra, el modelo lineal con la antigüedad explica "
        f"aproximadamente el {porcentaje:.2f} % de la variabilidad observada "
        "en la autonomía."
    )


def construir_datos_recta_regresion(
    datos: pd.DataFrame,
    resultado: ResultadoRegresionMuestral,
    columna_x: str = VARIABLE_ANTIGUEDAD_BATERIA,
    columna_y: str = VARIABLE_AUTONOMIA_REAL,
) -> pd.DataFrame:
    """Construye puntos ordenados de la recta usando el modelo ajustado."""
    valores_x = pd.Series(pd.to_numeric(datos[columna_x], errors="raise")).sort_values()
    valores_x = valores_x.drop_duplicates().reset_index(drop=True)
    valores_y = resultado.intercepto + resultado.pendiente * valores_x

    return pd.DataFrame(
        {
            columna_x: valores_x,
            columna_y: valores_y,
        }
    )


def formatear_ecuacion_regresion(
    resultado: ResultadoRegresionMuestral,
) -> str:
    """Formatea la ecuación muestral visible con unidades implícitas."""
    signo = "+" if resultado.pendiente >= 0 else "-"
    pendiente_abs = abs(resultado.pendiente)
    return (
        "Autonomía estimada (km) = "
        f"{resultado.intercepto:.2f} {signo} {pendiente_abs:.2f} × "
        "Antigüedad (meses)"
    )


def _preparar_series_numericas(
    datos: pd.DataFrame,
    columna_x: str,
    columna_y: str,
    cantidad_minima: int = 3,
) -> tuple[pd.Series, pd.Series]:
    """Valida y convierte las series necesarias para ajustar el modelo."""
    columnas_faltantes = [
        columna for columna in (columna_x, columna_y) if columna not in datos.columns
    ]
    if columnas_faltantes:
        detalle = ", ".join(columnas_faltantes)
        raise ErrorAnalisisCuantitativo(
            f"Faltan columnas cuantitativas requeridas: {detalle}."
        )

    if len(datos) < cantidad_minima:
        cantidad_texto = "tres" if cantidad_minima == 3 else str(cantidad_minima)
        raise ErrorAnalisisCuantitativo(
            "Se requieren al menos "
            f"{cantidad_texto} observaciones para ajustar la regresión."
        )

    if datos[[columna_x, columna_y]].isna().any().any():
        raise ErrorAnalisisCuantitativo(
            "No se puede ajustar la regresión con valores nulos."
        )

    try:
        x = pd.to_numeric(datos[columna_x], errors="raise").astype(float)
        y = pd.to_numeric(datos[columna_y], errors="raise").astype(float)
    except (TypeError, ValueError) as error:
        raise ErrorAnalisisCuantitativo(
            "Las variables cuantitativas deben contener valores numéricos."
        ) from error

    if not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ErrorAnalisisCuantitativo(
            "No se puede ajustar la regresión con valores no finitos."
        )

    if x.nunique() <= 1:
        raise ErrorAnalisisCuantitativo(
            "No se puede ajustar la regresión: la variable X no tiene variabilidad."
        )

    if y.nunique() <= 1:
        raise ErrorAnalisisCuantitativo(
            "No se puede ajustar la regresión: la variable Y no tiene variabilidad."
        )

    x.name = columna_x
    y.name = columna_y
    return x, y


def _ajustar_modelo_ols(
    datos: pd.DataFrame,
    columna_x: str,
    columna_y: str,
    cantidad_minima: int = 3,
):
    """Valida los datos y ajusta un único modelo OLS con intercepto."""
    x, y = _preparar_series_numericas(
        datos,
        columna_x,
        columna_y,
        cantidad_minima=cantidad_minima,
    )
    matriz_x = sm.add_constant(x, has_constant="add")
    modelo = sm.OLS(y, matriz_x).fit()
    return x, y, modelo


def _validar_valor_x_operativo(valor_x: float) -> float:
    """Valida que el valor de X esté dentro del rango operativo."""
    try:
        valor = float(valor_x)
    except (TypeError, ValueError) as error:
        raise ErrorAnalisisCuantitativo(
            "La antigüedad ingresada debe ser numérica."
        ) from error

    if not np.isfinite(valor):
        raise ErrorAnalisisCuantitativo(
            "La antigüedad ingresada debe ser finita."
        )

    if valor < ANTIGUEDAD_MINIMA_MESES or valor > ANTIGUEDAD_MAXIMA_MESES:
        raise ErrorAnalisisCuantitativo(
            "La antigüedad debe estar entre "
            f"{ANTIGUEDAD_MINIMA_MESES} y {ANTIGUEDAD_MAXIMA_MESES} meses."
        )

    return valor


def _construir_exog_prediccion(valor_x: float, columna_x: str) -> pd.DataFrame:
    """Construye la matriz exógena para una predicción individual."""
    return pd.DataFrame(
        {
            "const": [1.0],
            columna_x: [valor_x],
        }
    )


def _clasificar_intensidad_correlacion(magnitud: float) -> str:
    """Clasifica la intensidad de |r| con un criterio heurístico documentado."""
    if magnitud < 0.20:
        return "muy débil"
    if magnitud < 0.40:
        return "débil"
    if magnitud < 0.60:
        return "moderada"
    if magnitud < 0.80:
        return "fuerte"
    return "muy fuerte"


def _validar_pearson(coeficiente: float) -> None:
    """Valida que Pearson esté entre -1 y 1."""
    if not -1 <= coeficiente <= 1:
        raise ErrorAnalisisCuantitativo(
            "El coeficiente de Pearson debe estar entre -1 y 1."
        )


def _validar_r_cuadrado(coeficiente_determinacion: float) -> None:
    """Valida que R² esté entre 0 y 1."""
    if not 0 <= coeficiente_determinacion <= 1:
        raise ErrorAnalisisCuantitativo(
            "El coeficiente de determinación debe estar entre 0 y 1."
        )


def _validar_nivel_confianza(nivel_confianza: float) -> None:
    """Valida que el nivel de confianza sea una proporción válida."""
    if not 0 < nivel_confianza < 1:
        raise ErrorAnalisisCuantitativo(
            "El nivel de confianza debe estar entre 0 y 1."
        )
