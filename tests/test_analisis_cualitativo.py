"""Pruebas asociadas al análisis cualitativo."""

from pathlib import Path

import pandas as pd
import pytest
from scipy.stats import chi2_contingency

from src.analisis_cualitativo import (
    ETIQUETA_TOTAL,
    ErrorAnalisisCualitativo,
    agregar_marginales,
    calcular_aportes_chi_cuadrado,
    calcular_chi_cuadrado_muestral,
    calcular_diferencias_relativas,
    calcular_porcentajes_por_sucursal,
    comparar_p_valor_con_alpha,
    concluir_chi_cuadrado,
    construir_tabla_contingencia,
    construir_tabla_frecuencias_esperadas,
    decidir_chi_cuadrado,
    evaluar_robustez_chi_cuadrado,
    identificar_categorias_excluidas,
)
from src.carga_datos import cargar_archivo_semanal
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


def _datos_cualitativos() -> pd.DataFrame:
    """Construye datos cualitativos controlados para pruebas."""
    return pd.DataFrame(
        {
            "Sucursal": [
                "Rosario",
                "Rosario",
                "Rosario",
                "Rosario",
                "Córdoba",
                "Córdoba",
                "Córdoba",
                "Córdoba",
                "Córdoba",
                "Córdoba",
            ],
            "Nivel_Fallos": [
                "Bajo",
                "Bajo",
                "Medio",
                "Alto",
                "Bajo",
                "Medio",
                "Medio",
                "Alto",
                "Alto",
                "Alto",
            ],
        }
    )


def test_construccion_correcta_tabla_contingencia() -> None:
    """Comprueba frecuencias observadas de Sucursal por Nivel_Fallos."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())

    assert tabla.loc["Rosario", "Bajo"] == 2
    assert tabla.loc["Rosario", "Medio"] == 1
    assert tabla.loc["Rosario", "Alto"] == 1
    assert tabla.loc["Córdoba", "Bajo"] == 1
    assert tabla.loc["Córdoba", "Medio"] == 2
    assert tabla.loc["Córdoba", "Alto"] == 3


def test_orden_de_filas_y_columnas() -> None:
    """Mantiene el orden canónico de categorías."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())

    assert tuple(tabla.index) == CATEGORIAS_SUCURSAL
    assert tuple(tabla.columns) == CATEGORIAS_NIVEL_FALLOS


def test_totales_marginales_correctos() -> None:
    """Agrega totales marginales sin modificar categorías base."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())
    tabla_marginal = agregar_marginales(tabla)

    assert tabla_marginal.loc["Rosario", ETIQUETA_TOTAL] == 4
    assert tabla_marginal.loc["Córdoba", ETIQUETA_TOTAL] == 6
    assert tabla_marginal.loc[ETIQUETA_TOTAL, "Bajo"] == 3
    assert tabla_marginal.loc[ETIQUETA_TOTAL, "Medio"] == 3
    assert tabla_marginal.loc[ETIQUETA_TOTAL, "Alto"] == 4
    assert tabla_marginal.loc[ETIQUETA_TOTAL, ETIQUETA_TOTAL] == 10


def test_marginales_no_alteran_tabla_usada_en_prueba() -> None:
    """La prueba ignora fila y columna Total si llegan a la función."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())
    tabla_marginal = agregar_marginales(tabla)

    resultado_base = calcular_chi_cuadrado_muestral(tabla)
    resultado_marginal = calcular_chi_cuadrado_muestral(tabla_marginal)

    assert resultado_base.estadistico == pytest.approx(resultado_marginal.estadistico)
    assert resultado_base.p_valor == pytest.approx(resultado_marginal.p_valor)


def test_chi_cuadrado_coincide_con_scipy() -> None:
    """Compara el cálculo propio con scipy.stats.chi2_contingency."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())
    esperado_chi, esperado_p, _, _ = chi2_contingency(tabla, correction=False)

    resultado = calcular_chi_cuadrado_muestral(tabla)

    assert resultado.estadistico == pytest.approx(esperado_chi)
    assert resultado.p_valor == pytest.approx(esperado_p)


def test_grados_de_libertad_correctos() -> None:
    """Para una tabla 2 x 3 los grados de libertad son 2."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )

    assert resultado.grados_libertad == 2


def test_p_valor_entre_cero_y_uno() -> None:
    """El p-valor técnico debe quedar dentro del rango probabilístico."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )

    assert 0 <= resultado.p_valor <= 1


def test_frecuencias_esperadas_misma_dimension_que_tabla_efectiva() -> None:
    """Las esperadas conservan dimensión de la tabla enviada a SciPy."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )

    assert resultado.frecuencias_esperadas.shape == resultado.tabla_observada.shape


def test_suma_frecuencias_esperadas_igual_total_observado() -> None:
    """El total esperado debe coincidir con el total observado."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )

    assert resultado.frecuencias_esperadas.to_numpy().sum() == pytest.approx(
        resultado.tabla_observada.to_numpy().sum()
    )


def test_estadistico_no_negativo() -> None:
    """El estadístico Chi-cuadrado no puede ser negativo."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )

    assert resultado.estadistico >= 0


def test_p_valor_no_depende_de_alpha() -> None:
    """Cambiar alpha solo cambia la comparación, no el p-valor calculado."""
    resultado = calcular_chi_cuadrado_muestral(
        construir_tabla_contingencia(_datos_cualitativos())
    )
    p_valor_original = resultado.p_valor

    comparar_p_valor_con_alpha(resultado.p_valor, 0.01)
    comparar_p_valor_con_alpha(resultado.p_valor, 0.10)

    assert resultado.p_valor == p_valor_original


def test_manejo_de_categoria_valida_ausente() -> None:
    """Una categoría válida ausente se elimina solo para la prueba."""
    datos = _datos_cualitativos()
    datos = datos[datos["Nivel_Fallos"] != "Alto"]
    tabla = construir_tabla_contingencia(datos)

    resultado = calcular_chi_cuadrado_muestral(tabla)

    assert "Alto" in tabla.columns
    assert "Alto" not in resultado.tabla_observada.columns
    assert resultado.tabla_observada.shape == (2, 2)


def test_error_comprensible_con_una_categoria_observada() -> None:
    """Si una variable tiene una sola categoría observada, la prueba no se calcula."""
    datos = pd.DataFrame(
        {
            "Sucursal": ["Rosario", "Rosario", "Rosario"],
            "Nivel_Fallos": ["Bajo", "Medio", "Alto"],
        }
    )
    tabla = construir_tabla_contingencia(datos)

    with pytest.raises(ErrorAnalisisCualitativo, match="al menos dos categorías"):
        calcular_chi_cuadrado_muestral(tabla)


def test_porcentajes_por_sucursal_suman_cien() -> None:
    """Los porcentajes para barras apiladas suman 100 % por sucursal."""
    tabla = construir_tabla_contingencia(_datos_cualitativos())
    porcentajes = calcular_porcentajes_por_sucursal(tabla)

    assert porcentajes.loc["Rosario"].sum() == pytest.approx(100)
    assert porcentajes.loc["Córdoba"].sum() == pytest.approx(100)


def test_calculos_funcionan_con_excel_predeterminado() -> None:
    """El Excel predeterminado alimenta correctamente el módulo cualitativo."""
    datos = cargar_archivo_semanal(
        Path("data/volt_ar_semana_01.xlsx"),
        "volt_ar_semana_01.xlsx",
    )
    tabla = construir_tabla_contingencia(datos)
    resultado = calcular_chi_cuadrado_muestral(tabla)

    assert tabla.to_numpy().sum() == len(datos)
    assert resultado.grados_libertad == 2
    assert 0 <= resultado.p_valor <= 1


def test_pagina_no_contiene_frases_inferenciales_prohibidas() -> None:
    """La página gerencial no debe mostrar conclusiones inferenciales."""
    contenido = Path("pages/1_Perfil_Gerencial.py").read_text(encoding="utf-8").lower()
    frases_prohibidas = (
        "se rechaza h",
        "no se rechaza h",
        "existe asociación poblacional",
        "las variables son independientes",
    )

    for frase in frases_prohibidas:
        assert frase not in contenido


def _tabla_predeterminada_observada() -> pd.DataFrame:
    """Construye la tabla observada esperada para el Excel predeterminado."""
    tabla = pd.DataFrame(
        {
            "Bajo": [3, 14],
            "Medio": [9, 10],
            "Alto": [12, 0],
        },
        index=["Rosario", "Córdoba"],
    )
    tabla.index.name = VARIABLE_SUCURSAL
    tabla.columns.name = VARIABLE_NIVEL_FALLOS
    return tabla


def _tabla_predeterminada_esperada() -> pd.DataFrame:
    """Construye la tabla esperada bajo independencia para el caso base."""
    tabla = pd.DataFrame(
        {
            "Bajo": [8.5, 8.5],
            "Medio": [9.5, 9.5],
            "Alto": [6.0, 6.0],
        },
        index=["Rosario", "Córdoba"],
    )
    tabla.index.name = VARIABLE_SUCURSAL
    tabla.columns.name = VARIABLE_NIVEL_FALLOS
    return tabla


def test_frecuencias_esperadas_correctas() -> None:
    """Calcula la tabla esperada completa para el caso predeterminado."""
    esperadas = construir_tabla_frecuencias_esperadas(
        _tabla_predeterminada_observada()
    )

    pd.testing.assert_frame_equal(esperadas, _tabla_predeterminada_esperada())


def test_formula_manual_de_una_celda_esperada() -> None:
    """Verifica Eij = total fila * total columna / N."""
    observadas = _tabla_predeterminada_observada()
    esperadas = construir_tabla_frecuencias_esperadas(observadas)
    esperado_manual = observadas.loc["Rosario"].sum() * observadas["Bajo"].sum()
    esperado_manual = esperado_manual / observadas.to_numpy().sum()

    assert esperadas.loc["Rosario", "Bajo"] == pytest.approx(esperado_manual)


def test_frecuencias_esperadas_conservan_etiquetas_y_orden() -> None:
    """La tabla esperada conserva filas y columnas de la tabla efectiva."""
    observadas = _tabla_predeterminada_observada()
    esperadas = construir_tabla_frecuencias_esperadas(observadas)

    assert list(esperadas.index) == list(observadas.index)
    assert list(esperadas.columns) == list(observadas.columns)


def test_suma_de_observadas_y_esperadas_coincide() -> None:
    """El total esperado coincide con el total observado."""
    observadas = _tabla_predeterminada_observada()
    esperadas = construir_tabla_frecuencias_esperadas(observadas)

    assert esperadas.to_numpy().sum() == pytest.approx(observadas.to_numpy().sum())


def test_diferencias_relativas_correctas() -> None:
    """Calcula diferencias relativas porcentuales para el caso base."""
    observadas = _tabla_predeterminada_observada()
    esperadas = _tabla_predeterminada_esperada()
    diferencias = calcular_diferencias_relativas(observadas, esperadas)

    assert diferencias.loc["Rosario", "Bajo"] == pytest.approx(-64.705882)
    assert diferencias.loc["Rosario", "Medio"] == pytest.approx(-5.263158)
    assert diferencias.loc["Rosario", "Alto"] == pytest.approx(100.0)
    assert diferencias.loc["Córdoba", "Bajo"] == pytest.approx(64.705882)
    assert diferencias.loc["Córdoba", "Medio"] == pytest.approx(5.263158)
    assert diferencias.loc["Córdoba", "Alto"] == pytest.approx(-100.0)


def test_diferencia_relativa_positiva_cuando_observada_supera_esperada() -> None:
    """Si O > E, la diferencia relativa porcentual es positiva."""
    diferencias = calcular_diferencias_relativas(
        pd.DataFrame([[12]], index=["A"], columns=["B"]),
        pd.DataFrame([[10.0]], index=["A"], columns=["B"]),
    )

    assert diferencias.loc["A", "B"] > 0


def test_diferencia_relativa_negativa_cuando_observada_es_menor() -> None:
    """Si O < E, la diferencia relativa porcentual es negativa."""
    diferencias = calcular_diferencias_relativas(
        pd.DataFrame([[8]], index=["A"], columns=["B"]),
        pd.DataFrame([[10.0]], index=["A"], columns=["B"]),
    )

    assert diferencias.loc["A", "B"] < 0


def test_diferencia_relativa_cero_cuando_observada_e_esperada_coinciden() -> None:
    """Si O = E, la diferencia relativa porcentual es cero."""
    diferencias = calcular_diferencias_relativas(
        pd.DataFrame([[10]], index=["A"], columns=["B"]),
        pd.DataFrame([[10.0]], index=["A"], columns=["B"]),
    )

    assert diferencias.loc["A", "B"] == pytest.approx(0)


def test_aportes_por_celda_correctos() -> None:
    """Calcula el aporte individual de una celda a Chi-cuadrado."""
    aportes = calcular_aportes_chi_cuadrado(
        _tabla_predeterminada_observada(),
        _tabla_predeterminada_esperada(),
    )

    assert aportes.loc["Rosario", "Bajo"] == pytest.approx((3 - 8.5) ** 2 / 8.5)


def test_suma_de_aportes_igual_chi_cuadrado() -> None:
    """La suma de aportes coincide con el estadístico Chi-cuadrado."""
    observadas = _tabla_predeterminada_observada()
    esperadas = _tabla_predeterminada_esperada()
    aportes = calcular_aportes_chi_cuadrado(observadas, esperadas)
    resultado = calcular_chi_cuadrado_muestral(observadas)

    assert aportes.to_numpy().sum() == pytest.approx(resultado.estadistico)


def test_evaluacion_de_robustez_completamente_cumplida() -> None:
    """El caso predeterminado cumple los criterios de robustez."""
    robustez = evaluar_robustez_chi_cuadrado(_tabla_predeterminada_esperada())

    assert robustez.frecuencia_esperada_minima == pytest.approx(6.0)
    assert robustez.cantidad_menores_que_uno == 0
    assert robustez.porcentaje_mayores_o_iguales_a_cinco == pytest.approx(100.0)
    assert robustez.es_robusta is True


def test_robustez_incumple_por_esperada_menor_que_uno() -> None:
    """Una frecuencia esperada menor que 1 invalida el criterio absoluto."""
    esperadas = pd.DataFrame([[0.5, 20.0], [10.0, 15.0]])
    robustez = evaluar_robustez_chi_cuadrado(esperadas)

    assert robustez.cantidad_menores_que_uno == 1
    assert robustez.cumple_minimo_absoluto is False
    assert robustez.es_robusta is False


def test_robustez_incumple_regla_del_ochenta_por_ciento() -> None:
    """Si menos del 80 % de esperadas es >= 5, la prueba no es robusta."""
    esperadas = pd.DataFrame(
        [[4.0, 4.0, 4.0, 4.0, 20.0], [4.0, 4.0, 4.0, 4.0, 20.0]]
    )
    robustez = evaluar_robustez_chi_cuadrado(esperadas)

    assert robustez.cantidad_menores_que_uno == 0
    assert robustez.porcentaje_mayores_o_iguales_a_cinco == pytest.approx(20.0)
    assert robustez.cumple_regla_ochenta_por_ciento is False
    assert robustez.es_robusta is False


def test_p_valor_inferencial_no_depende_de_alpha() -> None:
    """El p-valor calculado permanece fijo frente a distintos alpha."""
    resultado = calcular_chi_cuadrado_muestral(_tabla_predeterminada_observada())
    p_valor_original = resultado.p_valor

    decidir_chi_cuadrado(resultado.p_valor, 0.01)
    decidir_chi_cuadrado(resultado.p_valor, 0.10)

    assert resultado.p_valor == p_valor_original


def test_decision_rechazo_cuando_p_valor_menor_que_alpha() -> None:
    """Si p < alpha, se rechaza H0."""
    assert decidir_chi_cuadrado(0.01, 0.05) == "Se rechaza H₀."


def test_decision_no_rechazo_cuando_p_valor_mayor_o_igual_que_alpha() -> None:
    """Si p >= alpha, no se rechaza H0."""
    assert decidir_chi_cuadrado(0.08, 0.05) == "No se rechaza H₀."
    assert decidir_chi_cuadrado(0.05, 0.05) == "No se rechaza H₀."


def test_decision_no_utiliza_aceptar_h0() -> None:
    """La decisión no debe usar la expresión aceptar H0."""
    texto = decidir_chi_cuadrado(0.08, 0.05).lower()

    assert "acept" not in texto


def test_conclusion_de_rechazo_contextualizada() -> None:
    """La conclusión de rechazo menciona asociación y escenario simulado."""
    texto = concluir_chi_cuadrado(0.01, 0.05)

    assert "se rechaza la hipótesis nula" in texto
    assert "asociación" in texto
    assert "escenario poblacional simulado" in texto


def test_conclusion_de_no_rechazo_no_afirma_independencia_definitiva() -> None:
    """La conclusión de no rechazo no afirma independencia como verdad final."""
    texto = concluir_chi_cuadrado(0.08, 0.05).lower()

    assert "no se rechaza la hipótesis nula" in texto
    assert "no proporcionan evidencia estadística suficiente" in texto
    assert "son independientes" not in texto


def test_resultado_predeterminado_esperado() -> None:
    """El Excel predeterminado reproduce el resultado esperado de P-06."""
    datos = cargar_archivo_semanal(
        Path("data/volt_ar_semana_01.xlsx"),
        "volt_ar_semana_01.xlsx",
    )
    observadas = construir_tabla_contingencia(datos)
    resultado = calcular_chi_cuadrado_muestral(observadas)
    robustez = evaluar_robustez_chi_cuadrado(resultado.frecuencias_esperadas)

    pd.testing.assert_frame_equal(observadas, _tabla_predeterminada_observada())
    pd.testing.assert_frame_equal(
        resultado.frecuencias_esperadas,
        _tabla_predeterminada_esperada(),
    )
    assert resultado.estadistico == pytest.approx(19.170279, rel=1e-6)
    assert resultado.grados_libertad == 2
    assert resultado.p_valor == pytest.approx(6.874274743165537e-05)
    assert robustez.es_robusta is True


def test_manejo_inferencial_de_categoria_ausente() -> None:
    """Una categoría válida ausente se informa y se excluye del cálculo."""
    tabla = pd.DataFrame(
        {
            "Bajo": [10, 8],
            "Medio": [5, 7],
            "Alto": [0, 0],
        },
        index=["Rosario", "Córdoba"],
    )
    resultado = calcular_chi_cuadrado_muestral(tabla)
    excluidas = identificar_categorias_excluidas(tabla, resultado.tabla_observada)

    assert "Alto" in excluidas[VARIABLE_NIVEL_FALLOS]
    assert "Alto" not in resultado.tabla_observada.columns


def test_error_inferencial_cuando_queda_una_sola_categoria_por_variable() -> None:
    """La prueba falla si la tabla efectiva queda en una sola categoría."""
    tabla = pd.DataFrame(
        {
            "Bajo": [10, 0],
            "Medio": [0, 0],
            "Alto": [0, 0],
        },
        index=["Rosario", "Córdoba"],
    )

    with pytest.raises(ErrorAnalisisCualitativo, match="al menos dos categorías"):
        calcular_chi_cuadrado_muestral(tabla)


def test_pagina_analista_contiene_hipotesis() -> None:
    """La Página 2 debe mostrar H0 y H1."""
    contenido = Path("pages/2_Perfil_Analista.py").read_text(encoding="utf-8")

    assert "H₀" in contenido
    assert "H₁" in contenido


def test_pagina_analista_muestra_independencia_como_supuesto_de_diseno() -> None:
    """La independencia de observaciones se presenta como supuesto de diseño."""
    contenido = Path("pages/2_Perfil_Analista.py").read_text(
        encoding="utf-8"
    ).lower()

    assert "se asume que cada fila corresponde" in contenido
    assert "depende del diseño de recolección" in contenido


def test_p04_y_p05_permanecen_presentes_en_pagina_gerencial() -> None:
    """La fase P-06 no elimina los módulos gerenciales ya implementados."""
    contenido = Path("pages/1_Perfil_Gerencial.py").read_text(encoding="utf-8")

    assert "Análisis cualitativo" in contenido
    assert "Análisis cuantitativo" in contenido
    assert "ajustar_regresion_lineal" in contenido
