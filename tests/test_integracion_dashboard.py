"""Pruebas de integración final del dashboard."""

import ast
from collections.abc import Callable
from io import BytesIO
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

import src.config as config
from src.analisis_cualitativo import (
    calcular_chi_cuadrado_muestral,
    construir_tabla_contingencia,
)
from src.analisis_cuantitativo import (
    ajustar_inferencia_regresion,
    ajustar_regresion_lineal,
    calcular_ancho_intervalo,
    calcular_diagnostico_residuos,
    calcular_prediccion,
    construir_bandas_prediccion,
    construir_datos_histograma_residuos,
    construir_datos_qq,
)
from src.carga_datos import cargar_archivo_semanal
from src.config import (
    CATEGORIAS_NIVEL_FALLOS,
    CATEGORIAS_SUCURSAL,
    MUESTRA_MAXIMA,
    MUESTRA_MINIMA,
    VARIABLE_ANTIGUEDAD_BATERIA,
    VARIABLE_AUTONOMIA_REAL,
    VARIABLE_NIVEL_FALLOS,
    VARIABLE_SUCURSAL,
    VARIABLES_ESTADISTICAS,
)
from src.simulacion_datos import generar_datos
from src.validacion_datos import ErrorDatos


RUTA_DATOS_PREDETERMINADOS = Path("data/volt_ar_semana_01.xlsx")
PAGINAS = (
    Path("app.py"),
    Path("pages/1_Perfil_Gerencial.py"),
    Path("pages/2_Perfil_Analista.py"),
)


def _datos_predeterminados() -> pd.DataFrame:
    """Carga la semana predeterminada validada."""
    return cargar_archivo_semanal(
        RUTA_DATOS_PREDETERMINADOS,
        RUTA_DATOS_PREDETERMINADOS.name,
    )


def _resumen_integrado(datos: pd.DataFrame) -> dict[str, object]:
    """Calcula resultados principales de todos los módulos sobre un DataFrame."""
    tabla = construir_tabla_contingencia(datos)
    chi = calcular_chi_cuadrado_muestral(tabla)
    regresion = ajustar_regresion_lineal(datos)
    inferencia = ajustar_inferencia_regresion(datos)
    prediccion = calcular_prediccion(datos, 24)
    diagnostico = calcular_diagnostico_residuos(datos)
    datos_qq = construir_datos_qq(diagnostico.residuos)
    histograma = construir_datos_histograma_residuos(diagnostico.residuos)
    bandas = construir_bandas_prediccion(datos)
    return {
        "tabla": tabla,
        "chi": chi,
        "regresion": regresion,
        "inferencia": inferencia,
        "prediccion": prediccion,
        "diagnostico": diagnostico,
        "qq": datos_qq,
        "histograma": histograma,
        "bandas": bandas,
    }


def _excel_en_memoria(datos: pd.DataFrame, hoja: str = "datos") -> BytesIO:
    """Construye un Excel en memoria para pruebas de carga."""
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as escritor:
        datos.to_excel(escritor, sheet_name=hoja, index=False)
    buffer.seek(0)
    return buffer


def _csv_en_memoria(datos: pd.DataFrame, separador: str = ",") -> BytesIO:
    """Construye un CSV en memoria para pruebas de carga."""
    return BytesIO(datos.to_csv(index=False, sep=separador).encode("utf-8"))


def _datos_validos(cantidad: int = 48) -> pd.DataFrame:
    """Construye datos válidos para pruebas de archivos inválidos."""
    sucursales = ["Rosario", "Córdoba"] * ((cantidad + 1) // 2)
    niveles = ["Bajo", "Medio", "Alto"] * ((cantidad + 2) // 3)
    antiguedades = list(range(1, 49)) * ((cantidad + 47) // 48)
    autonomias = [30.5, 32.0, 28.75, 35.2] * ((cantidad + 3) // 4)
    return pd.DataFrame(
        {
            VARIABLE_SUCURSAL: sucursales[:cantidad],
            VARIABLE_NIVEL_FALLOS: niveles[:cantidad],
            VARIABLE_ANTIGUEDAD_BATERIA: antiguedades[:cantidad],
            VARIABLE_AUTONOMIA_REAL: autonomias[:cantidad],
        },
        columns=VARIABLES_ESTADISTICAS,
    )


def _caso_dataframe_csv(
    modificador: Callable[[pd.DataFrame], pd.DataFrame],
) -> tuple[BytesIO, str]:
    """Aplica una modificación inválida y devuelve un CSV en memoria."""
    datos = modificador(_datos_validos().copy(deep=True))
    return _csv_en_memoria(datos), "datos.csv"


def test_tabla_observada_comun_entre_paginas() -> None:
    """La Página 1 y la Página 2 parten de la misma tabla observada."""
    datos = _datos_predeterminados()
    tabla_gerencial = construir_tabla_contingencia(datos)
    tabla_analista = construir_tabla_contingencia(datos)

    pd.testing.assert_frame_equal(tabla_gerencial, tabla_analista)


def test_chi_cuadrado_comun_entre_paginas() -> None:
    """El Chi-cuadrado descriptivo y el inferencial usan el mismo cálculo."""
    datos = _datos_predeterminados()
    tabla = construir_tabla_contingencia(datos)
    resultado_gerencial = calcular_chi_cuadrado_muestral(tabla)
    resultado_analista = calcular_chi_cuadrado_muestral(tabla)

    assert resultado_gerencial.estadistico == pytest.approx(
        resultado_analista.estadistico
    )
    assert resultado_gerencial.p_valor == pytest.approx(resultado_analista.p_valor)


def test_pearson_y_r2_comunes_entre_descripcion_e_inferencia() -> None:
    """Pearson y R² coinciden entre el módulo descriptivo y el inferencial."""
    datos = _datos_predeterminados()
    regresion = ajustar_regresion_lineal(datos)
    inferencia = ajustar_inferencia_regresion(datos)

    assert regresion.coeficiente_pearson == pytest.approx(
        inferencia.coeficiente_pearson
    )
    assert regresion.coeficiente_determinacion == pytest.approx(
        inferencia.coeficiente_determinacion
    )


def test_intercepto_y_pendiente_comunes_entre_modulos() -> None:
    """Regresión, inferencia, predicción y diagnóstico reutilizan el modelo OLS."""
    datos = _datos_predeterminados()
    regresion = ajustar_regresion_lineal(datos)
    inferencia = ajustar_inferencia_regresion(datos)
    diagnostico = calcular_diagnostico_residuos(datos)

    assert regresion.intercepto == pytest.approx(inferencia.intercepto)
    assert regresion.pendiente == pytest.approx(inferencia.pendiente)
    assert diagnostico.valores_ajustados.to_numpy(dtype=float) == pytest.approx(
        regresion.valores_ajustados.to_numpy(dtype=float)
    )


def test_prediccion_puntual_coincide_con_ecuacion() -> None:
    """La calculadora usa y_hat = b0 + b1 * x0."""
    datos = _datos_predeterminados()
    regresion = ajustar_regresion_lineal(datos)
    prediccion = calcular_prediccion(datos, 24)
    esperado = regresion.intercepto + regresion.pendiente * 24

    assert prediccion.prediccion_puntual == pytest.approx(esperado)


def test_residuos_coinciden_con_observado_menos_ajustado() -> None:
    """Los residuos diagnósticos se calculan como y observado menos y ajustado."""
    datos = _datos_predeterminados()
    diagnostico = calcular_diagnostico_residuos(datos)
    esperado = (
        datos[VARIABLE_AUTONOMIA_REAL].to_numpy(dtype=float)
        - diagnostico.valores_ajustados.to_numpy(dtype=float)
    )

    assert diagnostico.residuos.to_numpy(dtype=float) == pytest.approx(esperado)


def test_intervalo_individual_mas_amplio_que_intervalo_media() -> None:
    """El intervalo individual incorpora mayor variabilidad que el de la media."""
    prediccion = calcular_prediccion(_datos_predeterminados(), 24)
    ancho_media = calcular_ancho_intervalo(
        prediccion.limite_inferior_media,
        prediccion.limite_superior_media,
    )
    ancho_individual = calcular_ancho_intervalo(
        prediccion.limite_inferior_individual,
        prediccion.limite_superior_individual,
    )

    assert ancho_individual >= ancho_media


def test_p_valores_no_dependen_de_alpha() -> None:
    """Cambiar α no recalcula los p-valores."""
    datos = _datos_predeterminados()
    tabla = construir_tabla_contingencia(datos)
    p_cualitativo_1 = calcular_chi_cuadrado_muestral(tabla).p_valor
    p_cualitativo_2 = calcular_chi_cuadrado_muestral(tabla).p_valor
    p_pendiente_1 = ajustar_inferencia_regresion(datos).p_valor_pendiente
    p_pendiente_2 = ajustar_inferencia_regresion(datos).p_valor_pendiente

    assert p_cualitativo_1 == pytest.approx(p_cualitativo_2)
    assert p_pendiente_1 == pytest.approx(p_pendiente_2)


def test_confianza_amplia_intervalos_sin_cambiar_estimadores() -> None:
    """El nivel de confianza modifica límites, no estimadores puntuales."""
    datos = _datos_predeterminados()
    resultado_90 = ajustar_inferencia_regresion(datos, nivel_confianza=0.90)
    resultado_99 = ajustar_inferencia_regresion(datos, nivel_confianza=0.99)
    ancho_90 = resultado_90.intervalo_pendiente[1] - resultado_90.intervalo_pendiente[0]
    ancho_99 = resultado_99.intervalo_pendiente[1] - resultado_99.intervalo_pendiente[0]

    assert ancho_99 > ancho_90
    assert resultado_90.intercepto == pytest.approx(resultado_99.intercepto)
    assert resultado_90.pendiente == pytest.approx(resultado_99.pendiente)


def test_dataframe_completo_alimenta_analisis_y_vista_previa_no_muta() -> None:
    """Los análisis usan 48 filas y head(10) solo genera vista previa."""
    datos = _datos_predeterminados()
    copia = datos.copy(deep=True)
    vista_previa = datos.head(10)
    resumen = _resumen_integrado(datos)

    assert len(vista_previa) == 10
    assert len(datos) == 48
    assert resumen["regresion"].cantidad == 48
    assert len(resumen["diagnostico"].residuos) == 48
    pd.testing.assert_frame_equal(datos, copia)


def test_resultados_cambian_con_otra_semana_y_restauran_predeterminado() -> None:
    """Cambiar semana modifica métricas y volver al default restaura resultados."""
    predeterminada_1 = _resumen_integrado(_datos_predeterminados())
    alternativa = _resumen_integrado(generar_datos(cantidad=48, semilla=7))
    predeterminada_2 = _resumen_integrado(_datos_predeterminados())

    assert alternativa["regresion"].pendiente != pytest.approx(
        predeterminada_1["regresion"].pendiente
    )
    assert alternativa["chi"].estadistico != pytest.approx(
        predeterminada_1["chi"].estadistico
    )
    assert predeterminada_2["regresion"].pendiente == pytest.approx(
        predeterminada_1["regresion"].pendiente
    )
    assert predeterminada_2["chi"].estadistico == pytest.approx(
        predeterminada_1["chi"].estadistico
    )


@pytest.mark.parametrize("semilla", [42, 7, 123])
def test_tres_semanas_validas_ejecutan_todos_los_analisis(semilla: int) -> None:
    """Tres matrices válidas permiten ejecutar todos los módulos."""
    datos = generar_datos(cantidad=48, semilla=semilla)
    resumen = _resumen_integrado(datos)

    assert MUESTRA_MINIMA <= len(datos) <= MUESTRA_MAXIMA
    assert tuple(datos.columns) == VARIABLES_ESTADISTICAS
    assert set(datos[VARIABLE_SUCURSAL]).issubset(CATEGORIAS_SUCURSAL)
    assert set(datos[VARIABLE_NIVEL_FALLOS]).issubset(CATEGORIAS_NIVEL_FALLOS)
    assert datos[VARIABLE_ANTIGUEDAD_BATERIA].nunique() > 1
    assert datos[VARIABLE_AUTONOMIA_REAL].nunique() > 1
    assert 0 <= resumen["chi"].p_valor <= 1
    assert -1 <= resumen["regresion"].coeficiente_pearson <= 1
    assert 0 <= resumen["regresion"].coeficiente_determinacion <= 1
    assert 0 <= resumen["inferencia"].p_valor_pendiente <= 1
    assert np.isfinite(resumen["prediccion"].prediccion_puntual)
    assert len(resumen["diagnostico"].residuos) == len(datos)
    assert len(resumen["qq"]) == len(datos)
    assert int(resumen["histograma"]["Frecuencia"].sum()) == len(datos)


@pytest.mark.parametrize(
    ("nombre", "constructor"),
    [
        ("columna faltante", lambda: _caso_dataframe_csv(lambda d: d.drop(columns=[VARIABLE_SUCURSAL]))),
        ("columna adicional", lambda: _caso_dataframe_csv(lambda d: d.assign(Semana=1))),
        ("columna Unnamed", lambda: _caso_dataframe_csv(lambda d: d.assign(**{"Unnamed: 0": range(len(d))}))),
        ("menos de 30 filas", lambda: (_csv_en_memoria(_datos_validos(29)), "datos.csv")),
        ("más de 60 filas", lambda: (_csv_en_memoria(_datos_validos(61)), "datos.csv")),
        ("sucursal desconocida", lambda: _caso_dataframe_csv(lambda d: d.assign(Sucursal="Mendoza"))),
        ("nivel desconocido", lambda: _caso_dataframe_csv(lambda d: d.assign(Nivel_Fallos="Crítico"))),
        ("valor nulo", lambda: _caso_dataframe_csv(lambda d: d.assign(
            Sucursal=d[VARIABLE_SUCURSAL].where(d.index != 0, None)
        ))),
        ("valor infinito", lambda: _caso_dataframe_csv(lambda d: d.assign(Autonomia_Real_Km=np.inf))),
        ("antigüedad menor", lambda: _caso_dataframe_csv(lambda d: d.assign(Antiguedad_Bateria_Meses=0))),
        ("antigüedad mayor", lambda: _caso_dataframe_csv(lambda d: d.assign(Antiguedad_Bateria_Meses=49))),
        ("antigüedad decimal", lambda: _caso_dataframe_csv(lambda d: d.assign(Antiguedad_Bateria_Meses=10.5))),
        ("autonomía menor", lambda: _caso_dataframe_csv(lambda d: d.assign(Autonomia_Real_Km=14.9))),
        ("autonomía mayor", lambda: _caso_dataframe_csv(lambda d: d.assign(Autonomia_Real_Km=45.1))),
        ("Excel sin hoja datos", lambda: (_excel_en_memoria(_datos_validos(), hoja="otra"), "datos.xlsx")),
        ("CSV inválido", lambda: (BytesIO(b"a,b\n1,2\n"), "datos.csv")),
        ("extensión no permitida", lambda: (BytesIO(b"contenido"), "datos.txt")),
        ("archivo vacío", lambda: (BytesIO(b""), "datos.csv")),
    ],
)
def test_archivos_invalidos_no_reemplazan_ultimo_valido(
    nombre: str,
    constructor: Callable[[], tuple[BytesIO, str]],
) -> None:
    """Los archivos inválidos se rechazan y el último DataFrame válido no cambia."""
    ultimo_valido = _datos_predeterminados()
    copia = ultimo_valido.copy(deep=True)
    origen, nombre_archivo = constructor()

    with pytest.raises(ErrorDatos):
        cargar_archivo_semanal(origen, nombre_archivo)

    pd.testing.assert_frame_equal(ultimo_valido, copia)


def test_paginas_usan_session_state_y_no_leen_archivos_directamente() -> None:
    """Las páginas dependen del componente de carga, no de lecturas directas."""
    for ruta in PAGINAS:
        contenido = ruta.read_text(encoding="utf-8")
        if ruta.name.startswith(("1_", "2_")):
            assert "mostrar_carga_datos" in contenido
            assert "datos_activos" in contenido
        assert "read_excel" not in contenido
        assert "read_csv" not in contenido
        assert "cargar_archivo_semanal" not in contenido


def test_head_solo_se_usa_en_vista_previa() -> None:
    """head() debe limitarse al componente de vista previa."""
    usos_head = {
        ruta: ruta.read_text(encoding="utf-8").count(".head(")
        for ruta in [*PAGINAS, Path("src/interfaz_carga.py")]
    }

    assert usos_head[Path("src/interfaz_carga.py")] == 1
    assert all(usos_head[ruta] == 0 for ruta in PAGINAS)


def test_constantes_variables_usadas_en_paginas_existen_e_importan() -> None:
    """Las constantes VARIABLE_* usadas por páginas deben venir de src.config."""
    constantes_config = {
        nombre for nombre in dir(config) if nombre.startswith("VARIABLE_")
    }
    for ruta in PAGINAS:
        arbol = ast.parse(ruta.read_text(encoding="utf-8"))
        usadas = {
            nodo.id
            for nodo in ast.walk(arbol)
            if isinstance(nodo, ast.Name) and nodo.id.startswith("VARIABLE_")
        }
        importadas = {
            alias.name
            for nodo in arbol.body
            if isinstance(nodo, ast.ImportFrom) and nodo.module == "src.config"
            for alias in nodo.names
            if alias.name.startswith("VARIABLE_")
        }
        assert usadas <= importadas
        assert importadas <= constantes_config


def test_widgets_de_pagina_analista_tienen_claves_unicas() -> None:
    """Los widgets con key explícita no deben duplicarse en Página 2."""
    arbol = ast.parse(Path("pages/2_Perfil_Analista.py").read_text(encoding="utf-8"))
    claves = [
        palabra_clave.value.value
        for nodo in ast.walk(arbol)
        if isinstance(nodo, ast.Call)
        for palabra_clave in nodo.keywords
        if palabra_clave.arg == "key"
        and isinstance(palabra_clave.value, ast.Constant)
        and isinstance(palabra_clave.value.value, str)
    ]

    assert len(claves) == len(set(claves))
    assert "alpha_inferencia_cualitativa" in claves
    assert "alpha_inferencia_cuantitativa" in claves


def test_pagina_gerencial_no_contiene_expresiones_inferenciales_prohibidas() -> None:
    """La Página 1 no debe emitir decisiones poblacionales."""
    contenido = Path("pages/1_Perfil_Gerencial.py").read_text(
        encoding="utf-8"
    ).lower()
    prohibidas = (
        "se rechaza h",
        "no se rechaza h",
        "se acepta h",
        "asociación poblacional",
        "existe evidencia estadísticamente significativa",
        "intervalo de confianza",
        "q-q plot",
        "histograma de residuos",
    )

    for frase in prohibidas:
        assert frase not in contenido


def test_paginas_no_usan_aceptar_h0_ni_lenguaje_causal() -> None:
    """El dashboard evita aceptar H0 y evita causalidad."""
    contenido = "\n".join(
        ruta.read_text(encoding="utf-8").lower() for ruta in PAGINAS
    )

    assert "se acepta" not in contenido
    assert "causa" not in contenido
    assert "causal" not in contenido


def test_pagina_analista_no_aprueba_supuestos_automaticamente() -> None:
    """La validación técnica no declara aprobación o invalidación automática."""
    contenido = Path("pages/2_Perfil_Analista.py").read_text(
        encoding="utf-8"
    ).lower()
    prohibidas = (
        "todos los supuestos se cumplen",
        "el modelo es válido",
        "el modelo queda invalidado",
    )

    for frase in prohibidas:
        assert frase not in contenido


def test_app_principal_describe_estado_actual_del_dashboard() -> None:
    """La portada no debe quedar redactada como estructura inicial vacía."""
    contenido = Path("app.py").read_text(encoding="utf-8")

    assert "fases posteriores" not in contenido
    assert "estructura inicial" not in contenido
    assert "módulos descriptivos, inferenciales, predictivos y diagnósticos" in contenido
