# Registro de pruebas

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P02-T01 | Generar 48 filas. | `generar_datos()` | 48 observaciones. | 48 observaciones. | Aprobada | Prueba automatizada. |
| P02-T02 | Verificar exactamente cuatro columnas. | `generar_datos()` | 4 columnas. | 4 columnas. | Aprobada | No se agregó quinta variable. |
| P02-T03 | Verificar orden exacto de columnas. | `generar_datos()` | Orden requerido. | `Sucursal`, `Nivel_Fallos`, `Antiguedad_Bateria_Meses`, `Autonomia_Real_Km`. | Aprobada | Orden conservado. |
| P02-T04 | Comprobar reproducibilidad. | Cantidad 48, semilla 42. | DataFrames idénticos. | DataFrames idénticos. | Aprobada | Usa `pd.testing.assert_frame_equal`. |
| P02-T05 | Comprobar diferencia entre semillas. | Semillas 42 y 43. | DataFrames distintos. | DataFrames distintos. | Aprobada | No depende del estado global de NumPy. |
| P02-T06 | Rechazar menos de 30 observaciones. | Cantidad 29. | `ValueError`. | `ValueError`. | Aprobada | Mensaje claro. |
| P02-T07 | Rechazar más de 60 observaciones. | Cantidad 61. | `ValueError`. | `ValueError`. | Aprobada | Mensaje claro. |
| P02-T08 | Verificar ausencia de nulos. | `generar_datos()` | Sin nulos. | Sin nulos. | Aprobada | Control estructural. |
| P02-T09 | Validar sucursales. | `Sucursal`. | Rosario y Córdoba. | Solo categorías válidas. | Aprobada | Control cualitativo. |
| P02-T10 | Validar niveles de fallos. | `Nivel_Fallos`. | Bajo, Medio y Alto. | Solo categorías válidas. | Aprobada | Control cualitativo. |
| P02-T11 | Verificar antigüedad entera. | `Antiguedad_Bateria_Meses`. | Tipo entero. | Tipo entero. | Aprobada | Control cuantitativo. |
| P02-T12 | Validar rango de antigüedad. | `Antiguedad_Bateria_Meses`. | 1 a 48 meses. | 2 a 47 meses en archivo predeterminado. | Aprobada | Dentro del rango permitido. |
| P02-T13 | Validar rango de autonomía. | `Autonomia_Real_Km`. | 15 a 45 km. | 15.0 a 45.0 km en archivo predeterminado. | Aprobada | Dentro del rango permitido. |
| P02-T14 | Verificar variabilidad cuantitativa. | Variables X e Y. | Más de un valor único. | Variabilidad presente. | Aprobada | Control técnico. |
| P02-T15 | Verificar correlación negativa no perfecta. | Configuración 48/42. | Pearson entre -0.95 y -0.55, distinto de -1. | Pearson -0.900523. | Aprobada | Sin conclusión inferencial. |
| P02-T16 | Verificar balance de sucursales. | Cantidad 49, semilla 42. | Diferencia máxima de 1. | Diferencia máxima de 1. | Aprobada | Para 48 queda 24 y 24. |
| P02-T17 | Revisar frecuencias esperadas. | Configuración 48/42. | Ninguna menor que 1; al menos 80 % >= 5. | 100 % >= 5. | Aprobada | No implementa Chi-cuadrado definitivo. |
| P02-T18 | Escribir Excel. | Archivo temporal `.xlsx`. | Archivo creado. | Archivo creado. | Aprobada | Hoja `datos`. |
| P02-T19 | Leer Excel conservando dimensiones y columnas. | Archivo temporal `.xlsx`. | Mismas dimensiones y columnas. | Mismas dimensiones y columnas. | Aprobada | Sin columna de índice. |
| P02-T20 | Verificar nombre de hoja. | Archivo temporal `.xlsx`. | Hoja `datos`. | Hoja `datos`. | Aprobada | Control con `openpyxl`. |
| P02-T21 | Rechazar semana no positiva. | Semana 0. | `ValueError`. | `ValueError`. | Aprobada | Control de CLI/ruta. |

Validación automatizada ejecutada:

```text
.\.venv\Scripts\python.exe -m pytest -q
32 passed
```

## Fase P-03: carga y validación

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P03-T01 | Leer Excel válido. | `BytesIO` con hoja `datos`. | DataFrame válido. | DataFrame 48 x 4. | Aprobada | Lógica desacoplada de widgets. |
| P03-T02 | Leer CSV con coma. | `BytesIO` UTF-8. | DataFrame válido. | DataFrame 48 x 4. | Aprobada | Separador detectado. |
| P03-T03 | Leer CSV con punto y coma. | `BytesIO` UTF-8. | DataFrame válido. | DataFrame 48 x 4. | Aprobada | Separador detectado. |
| P03-T04 | Conservar cuatro columnas. | Excel válido. | Cuatro columnas canónicas. | Cuatro columnas canónicas. | Aprobada | Sin quinta variable. |
| P03-T05 | Reordenar columnas. | DataFrame con columnas desordenadas. | Orden canónico. | Orden canónico. | Aprobada | No modifica el original. |
| P03-T06 | Rechazar Excel sin hoja `datos`. | Excel con otra hoja. | Error de formato. | Error con hojas encontradas. | Aprobada | No selecciona otra hoja. |
| P03-T07 | Rechazar extensión no admitida. | `datos.txt`. | Error de formato. | Error de formato. | Aprobada | Solo `.xlsx` y `.csv`. |
| P03-T08 | Rechazar archivo vacío. | CSV vacío. | Error claro. | Error claro. | Aprobada | Mensaje indica vacío/no interpretable. |
| P03-T09 | Rechazar columna faltante. | Sin `Sucursal`. | Error de columnas. | Error de columnas. | Aprobada | Informa faltante. |
| P03-T10 | Rechazar columna adicional. | Columna `Semana`. | Error de columnas. | Error de columnas. | Aprobada | Informa adicional. |
| P03-T11 | Rechazar columna `Unnamed`. | Columna `Unnamed: 0`. | Error de columnas. | Error de columnas. | Aprobada | Evita índices exportados. |
| P03-T12 | Rechazar menos de 30 filas. | 29 filas. | Error de cantidad. | Error de cantidad. | Aprobada | Rango 30-60. |
| P03-T13 | Rechazar más de 60 filas. | 61 filas. | Error de cantidad. | Error de cantidad. | Aprobada | Rango 30-60. |
| P03-T14 | Rechazar valores nulos. | Nulo en `Sucursal`. | Error de faltantes. | Error de faltantes. | Aprobada | Informa columna. |
| P03-T15 | Rechazar sucursal inválida. | `Mendoza`. | Error de categorías. | Error de categorías. | Aprobada | No corrige nombres desconocidos. |
| P03-T16 | Rechazar nivel inválido. | `Crítico`. | Error de categorías. | Error de categorías. | Aprobada | No corrige nombres desconocidos. |
| P03-T17 | Normalizar mayúsculas y espacios. | Valores con espacios/case distinto. | Categorías canónicas. | Categorías canónicas. | Aprobada | Sin ambigüedad. |
| P03-T18 | Rechazar antigüedad decimal. | `10.5`. | Error numérico. | Error numérico. | Aprobada | No acepta decimales no enteros. |
| P03-T19 | Rechazar antigüedad fuera de rango. | 49 meses. | Error numérico. | Error numérico. | Aprobada | Rango 1-48. |
| P03-T20 | Rechazar autonomía fuera de rango. | 46 km. | Error numérico. | Error numérico. | Aprobada | Rango 15-45. |
| P03-T21 | Rechazar infinitos. | `np.inf`. | Error numérico. | Error numérico. | Aprobada | No acepta infinitos. |
| P03-T22 | No modificar DataFrame original. | DataFrame con valores normalizables. | Copia normalizada. | Original intacto. | Aprobada | Validador no muta silenciosamente. |
| P03-T23 | Archivo inválido no válido. | CSV con categoría inválida. | Excepción. | Excepción. | Aprobada | No devuelve DataFrame activo. |

Validación automatizada ejecutada:

```text
.\.venv\Scripts\python.exe -m pytest -q
55 passed
```

## Fase P-03: validación manual en Streamlit

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P03-M01 | Verificar carga automática del archivo predeterminado. | `data/volt_ar_semana_01.xlsx`. | La app carga el conjunto predeterminado al iniciar. | Carga automática aprobada. | Aprobada | Validado manualmente en Streamlit. |
| P03-M02 | Cargar Excel válido con hoja `datos`. | Archivo `.xlsx` válido alternativo. | El archivo reemplaza los datos activos. | Carga aprobada. | Aprobada | Validado manualmente en Streamlit. |
| P03-M03 | Cargar CSV válido con coma. | Archivo `.csv` separado por coma. | El archivo reemplaza los datos activos. | Carga aprobada. | Aprobada | Validado manualmente en Streamlit. |
| P03-M04 | Cargar CSV válido con punto y coma. | Archivo `.csv` separado por punto y coma. | El archivo reemplaza los datos activos. | Carga aprobada. | Aprobada | Validado manualmente en Streamlit. |
| P03-M05 | Rechazar Excel sin hoja `datos`. | Archivo `.xlsx` sin hoja `datos`. | La app muestra error claro y conserva datos activos. | Rechazo aprobado. | Aprobada | Validado manualmente en Streamlit. |
| P03-M06 | Rechazar archivo con columna faltante. | Archivo sin una columna requerida. | La app muestra error claro y conserva datos activos. | Rechazo aprobado. | Aprobada | Validado manualmente en Streamlit. |
| P03-M07 | Rechazar archivo con menos de 30 filas. | Archivo con muestra insuficiente. | La app muestra error claro y conserva datos activos. | Rechazo aprobado. | Aprobada | Validado manualmente en Streamlit. |
| P03-M08 | Rechazar categoría desconocida. | Archivo con categoría no permitida. | La app muestra error claro y conserva datos activos. | Rechazo aprobado. | Aprobada | Validado manualmente en Streamlit. |
| P03-M09 | Rechazar columna adicional. | Archivo con columna extra. | La app muestra error claro y conserva datos activos. | Rechazo aprobado. | Aprobada | Validado manualmente en Streamlit. |
| P03-M10 | Conservar conjunto válido anterior tras carga inválida. | Carga válida seguida de carga inválida. | Los datos activos no se sustituyen. | Conservación aprobada. | Aprobada | Validado manualmente en Streamlit. |
| P03-M11 | Restaurar archivo predeterminado. | Botón `Volver a datos predeterminados`. | La app restaura `data/volt_ar_semana_01.xlsx`. | Botón aprobado. | Aprobada | Validado manualmente en Streamlit. |
| P03-M12 | Persistir datos activos al navegar. | Navegación entre páginas. | `st.session_state["datos_activos"]` se mantiene disponible. | Persistencia aprobada. | Aprobada | Validado manualmente en Streamlit. |

## Fase P-04: módulo cualitativo gerencial

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P04-T01 | Construir tabla de contingencia. | DataFrame controlado. | Frecuencias correctas. | Frecuencias correctas. | Aprobada | `Sucursal` por `Nivel_Fallos`. |
| P04-T02 | Mantener orden de filas y columnas. | DataFrame controlado. | Rosario, Córdoba; Bajo, Medio, Alto. | Orden correcto. | Aprobada | Categorías canónicas. |
| P04-T03 | Calcular totales marginales. | Tabla observada. | Totales de filas y columnas correctos. | Totales correctos. | Aprobada | Solo para visualización. |
| P04-T04 | Evitar que marginales alteren la prueba. | Tabla con y sin marginales. | Mismo estadístico y p-valor. | Coincidencia. | Aprobada | La función descarta `Total`. |
| P04-T05 | Comparar Chi-cuadrado con SciPy. | Tabla 2 x 3. | Coincidencia con `chi2_contingency`. | Coincidencia. | Aprobada | `correction=False`. |
| P04-T06 | Verificar grados de libertad. | Tabla 2 x 3. | 2 grados. | 2 grados. | Aprobada | Fórmula implícita de SciPy. |
| P04-T07 | Verificar rango del p-valor. | Tabla 2 x 3. | Entre 0 y 1. | Entre 0 y 1. | Aprobada | Control técnico. |
| P04-T08 | Validar dimensión de esperadas. | Tabla efectiva. | Misma dimensión. | Misma dimensión. | Aprobada | Sin marginales. |
| P04-T09 | Validar suma de esperadas. | Tabla efectiva. | Igual al total observado. | Igual al total observado. | Aprobada | Control de consistencia. |
| P04-T10 | Validar estadístico no negativo. | Tabla 2 x 3. | Mayor o igual a cero. | Mayor o igual a cero. | Aprobada | Control matemático. |
| P04-T11 | Confirmar p-valor independiente de α. | Comparaciones con α distintos. | p-valor sin cambios. | p-valor sin cambios. | Aprobada | Solo cambia la comparación visual. |
| P04-T12 | Manejar categoría válida ausente. | Tabla sin `Alto`. | Cálculo con tabla efectiva 2 x 2. | Cálculo correcto. | Aprobada | No inventa observaciones. |
| P04-T13 | Informar error con una sola categoría observada. | Solo una sucursal observada. | Error comprensible. | Error comprensible. | Aprobada | No rompe Streamlit. |
| P04-T14 | Verificar porcentajes por sucursal. | Tabla observada. | Cada sucursal suma 100 %. | Suma 100 %. | Aprobada | Alimenta gráfico apilado. |
| P04-T15 | Probar Excel predeterminado. | `data/volt_ar_semana_01.xlsx`. | Cálculo cualitativo válido. | Cálculo válido. | Aprobada | Chi-cuadrado 19.170279. |
| P04-T16 | Revisar frases prohibidas en página. | `pages/1_Perfil_Gerencial.py`. | Sin conclusiones inferenciales prohibidas. | Sin frases prohibidas. | Aprobada | Página gerencial descriptiva. |

Validación automatizada ejecutada:

```text
.\.venv\Scripts\python.exe -m pytest -q
71 passed
```

## Fase P-04: validación manual de vista previa

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P04-M01 | Verificar cantidad total visible. | `data/volt_ar_semana_01.xlsx`. | La interfaz informa 48 observaciones activas. | Cantidad total visible aprobada. | Aprobada | Validado manualmente en Streamlit. |
| P04-M02 | Verificar vista previa limitada. | Archivo activo de 48 filas. | La interfaz muestra `Vista previa: 10 de 48 registros`. | Vista previa limitada aprobada. | Aprobada | `head()` se usa solo para la vista previa. |
| P04-M03 | Verificar visualización completa. | Expander `Ver base completa (48 registros)`. | El expander muestra los 48 registros completos. | Visualización completa aprobada. | Aprobada | Tabla con ancho adaptable e índice oculto. |
| P04-M04 | Verificar conservación de 48 casos en análisis. | Tabla de contingencia de Página 1. | Los totales marginales suman 48. | Conservación aprobada. | Aprobada | Los cálculos usan `st.session_state["datos_activos"]` completo. |
| P04-M05 | Verificar actualización dinámica al cambiar archivo. | Carga de otro archivo semanal válido. | Cantidad total, vista previa y expander se actualizan. | Actualización dinámica aprobada. | Aprobada | Validado manualmente en Streamlit. |

## Fase P-05: módulo cuantitativo gerencial

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P05-T01 | Ajustar regresión con datos lineales conocidos. | DataFrame controlado. | Coeficientes esperados. | Coeficientes esperados. | Aprobada | Modelo lineal con intercepto. |
| P05-T02 | Verificar pendiente positiva conocida. | Datos con pendiente 2.0. | Pearson positivo perfecto. | Pearson 1.0. | Aprobada | Control de dirección positiva. |
| P05-T03 | Verificar pendiente negativa conocida. | Datos con pendiente negativa. | Pearson negativo perfecto. | Pearson -1.0. | Aprobada | Control de dirección negativa. |
| P05-T04 | Verificar intercepto correcto. | Datos lineales con intercepto 45.0. | Intercepto 45.0. | Intercepto 45.0. | Aprobada | Sin redondeo interno. |
| P05-T05 | Verificar rango de Pearson. | Datos negativos no perfectos. | Valor entre -1 y 1. | Valor dentro de rango. | Aprobada | Control matemático. |
| P05-T06 | Verificar rango de R². | Datos negativos no perfectos. | Valor entre 0 y 1. | Valor dentro de rango. | Aprobada | Control matemático. |
| P05-T07 | Comparar R² con r². | Regresión simple con intercepto. | Coincidencia aproximada. | Coincidencia aproximada. | Aprobada | Propiedad del modelo simple. |
| P05-T08 | Conservar longitud de valores ajustados. | DataFrame controlado. | Una salida por fila. | Misma cantidad. | Aprobada | Resultado interno reutilizable. |
| P05-T09 | Conservar longitud de residuos. | DataFrame controlado. | Un residuo por fila. | Misma cantidad. | Aprobada | No se muestra en Página 1. |
| P05-T10 | Verificar media de residuos. | Modelo con intercepto. | Media aproximadamente cero. | Media aproximadamente cero. | Aprobada | Tolerancia numérica. |
| P05-T11 | Construir recta con X ordenado. | Datos desordenados. | X creciente. | X creciente. | Aprobada | Evita unir puntos observados. |
| P05-T12 | Usar coeficientes reales en la recta. | Datos negativos no perfectos. | Misma pendiente e intercepto. | Coincidencia. | Aprobada | No depende del redondeo visual. |
| P05-T13 | Rechazar X constante. | DataFrame con antigüedad fija. | Error comprensible. | Error comprensible. | Aprobada | No muestra traza técnica. |
| P05-T14 | Rechazar Y constante. | DataFrame con autonomía fija. | Error comprensible. | Error comprensible. | Aprobada | No ajusta modelo inválido. |
| P05-T15 | Rechazar valores no finitos. | Autonomía infinita. | Error comprensible. | Error comprensible. | Aprobada | Control previo al modelo. |
| P05-T16 | Interpretar sentido negativo. | Pearson -0.85. | Texto con `negativa`. | Texto correcto. | Aprobada | Referido a la muestra semanal. |
| P05-T17 | Interpretar sentido positivo. | Pearson 0.65. | Texto con `positiva`. | Texto correcto. | Aprobada | Referido a la muestra semanal. |
| P05-T18 | Clasificar rangos de intensidad. | Coeficientes 0.10, 0.30, 0.50, 0.70 y 0.90. | Muy débil, débil, moderada, fuerte y muy fuerte. | Clasificación correcta. | Aprobada | Criterio heurístico documentado. |
| P05-T19 | Interpretar R² como porcentaje. | R² 0.810942. | 81.09 % y referencia muestral. | Texto correcto. | Aprobada | Sin causalidad. |
| P05-T20 | Validar Excel predeterminado. | `data/volt_ar_semana_01.xlsx`. | 48 observaciones, pendiente y Pearson negativos. | 48 observaciones, Pearson -0.900523 y R² 0.810942. | Aprobada | Coincide con referencia de P-02. |
| P05-T21 | Revisar frases prohibidas en Página 1. | `pages/1_Perfil_Gerencial.py`. | Sin causalidad ni conclusión poblacional. | Sin frases prohibidas. | Aprobada | Página gerencial descriptiva. |
| P05-T22 | Confirmar que P-04 continúa presente. | `pages/1_Perfil_Gerencial.py`. | Módulo cualitativo conservado. | Módulo conservado. | Aprobada | No se eliminó la tabla de contingencia. |
| P05-T23 | Confirmar módulo cuantitativo visible. | `pages/1_Perfil_Gerencial.py`. | Sección, función de ajuste y recta. | Elementos presentes. | Aprobada | Integración de Página 1. |

Validación automatizada ejecutada:

```text
.\.venv\Scripts\python.exe -m pytest -q
102 passed
```

Validación de sintaxis ejecutada:

```text
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
Sin errores.
```

## Fase P-10: integración final y control de requisitos

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P10-T01 | Verificar tabla observada común entre páginas. | Semana predeterminada. | Misma tabla. | Coincidencia. | Aprobada | Página 1 y Página 2 usan la misma función. |
| P10-T02 | Verificar Chi-cuadrado común. | Semana predeterminada. | Mismo estadístico y p-valor. | Coincidencia. | Aprobada | Sin cálculos divergentes. |
| P10-T03 | Verificar Pearson y R² comunes. | Semana predeterminada. | Descripción e inferencia coinciden. | Coincidencia. | Aprobada | Mismo modelo OLS. |
| P10-T04 | Verificar intercepto y pendiente comunes. | Semana predeterminada. | Regresión, inferencia y diagnóstico coinciden. | Coincidencia. | Aprobada | No se ajusta otro modelo. |
| P10-T05 | Verificar predicción puntual. | X = 24. | `b0 + b1 * x0`. | Coincidencia. | Aprobada | Calculadora coherente. |
| P10-T06 | Verificar residuos. | Semana predeterminada. | `y - y_hat`. | Coincidencia. | Aprobada | Diagnóstico coherente. |
| P10-T07 | Comparar intervalos de predicción. | X = 24. | Individual >= media. | Cumple. | Aprobada | Statsmodels. |
| P10-T08 | Confirmar p-valores independientes de α. | Repetición de cálculos. | p-valores invariantes. | Cumple. | Aprobada | α solo cambia decisión. |
| P10-T09 | Confirmar efecto del nivel de confianza. | 90 % y 99 %. | Intervalos se amplían, estimadores no cambian. | Cumple. | Aprobada | Coherente con P-07/P-08. |
| P10-T10 | Confirmar uso de 48 filas completas. | Semana predeterminada. | Análisis con 48 filas. | Cumple. | Aprobada | `head(10)` no muta datos. |
| P10-T11 | Confirmar actualización al cambiar semana. | Semilla 7. | Resultados distintos. | Cumple. | Aprobada | Sin arrastre de valores previos. |
| P10-T12 | Confirmar restauración predeterminada. | Semana 1. | Métricas originales. | Cumple. | Aprobada | Restauración conceptual validada. |
| P10-T13 | Ejecutar análisis en tres semanas válidas. | Semillas 42, 7 y 123. | Todos los módulos calculan resultados. | Cumple. | Aprobada | 48 puntos en residuos y Q-Q. |
| P10-T14 | Rechazar archivos inválidos. | 18 casos inválidos. | Excepción controlada. | Cumple. | Aprobada | Último conjunto válido no se reemplaza. |
| P10-T15 | Verificar uso de `session_state`. | Código de páginas. | Páginas usan componente de carga. | Cumple. | Aprobada | No leen Excel/CSV directamente. |
| P10-T16 | Verificar `head()` limitado a vista previa. | Código de páginas e interfaz. | Solo en `src/interfaz_carga.py`. | Cumple. | Aprobada | Los análisis usan DataFrame completo. |
| P10-T17 | Verificar constantes `VARIABLE_*`. | AST de páginas. | Importadas desde `src.config`. | Cumple. | Aprobada | Previene `NameError`. |
| P10-T18 | Verificar claves únicas de widgets. | AST de Página 2. | Sin duplicados. | Cumple. | Aprobada | α cualitativo y cuantitativo independientes. |
| P10-T19 | Verificar Página 1 sin expresiones inferenciales prohibidas. | Código de Página 1. | Sin decisiones poblacionales. | Cumple. | Aprobada | Perfil descriptivo. |
| P10-T20 | Verificar ausencia de lenguaje causal y "se acepta H0". | Código de páginas. | Ausente. | Cumple. | Aprobada | Asociación/relación, no causalidad. |
| P10-T21 | Verificar que no se aprueben supuestos automáticamente. | Código de Página 2. | Sin frases prohibidas. | Cumple. | Aprobada | Diagnóstico requiere interpretación. |
| P10-T22 | Verificar portada actualizada. | `app.py`. | Sin textos de estructura inicial. | Cumple. | Aprobada | Corrección menor P-10. |

Validación de integración ejecutada:

```text
.\.venv\Scripts\python.exe -m pytest -q tests/test_integracion_dashboard.py
40 passed
```

Validación automatizada completa ejecutada:

```text
.\.venv\Scripts\python.exe -m pytest -q
244 passed
```

Resultados de tres semanas válidas:

| Semilla | n | Chi-cuadrado | p Chi-cuadrado | Pearson | R² | Pendiente | p pendiente | Predicción X=24 | Media residuos | `|r est.| > 2` | Puntos Q-Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 42 | 48 | 19.170279 | 0.000068742747 | -0.900523 | 0.810942 | -0.552768 | 2.97371341074e-18 | 31.899632 | -0.000000000000023 | 1 | 48 |
| 7 | 48 | 19.047619 | 0.000073090693 | -0.920086 | 0.846558 | -0.518881 | 2.39587404239e-20 | 31.625117 | -0.000000000000019 | 2 | 48 |
| 123 | 48 | 13.945455 | 0.000937093707 | -0.920721 | 0.847728 | -0.568801 | 2.00789672304e-20 | 32.999408 | -0.000000000000030 | 3 | 48 |

Casos inválidos verificados:

- columna faltante;
- columna adicional;
- columna `Unnamed`;
- menos de 30 filas;
- más de 60 filas;
- sucursal desconocida;
- nivel de fallos desconocido;
- valor nulo;
- valor infinito;
- antigüedad menor que 1;
- antigüedad mayor que 48;
- antigüedad decimal no entera;
- autonomía menor que 15;
- autonomía mayor que 45;
- Excel sin hoja `datos`;
- CSV con estructura inválida;
- extensión no permitida;
- archivo vacío.

Validación visual ejecutada en Streamlit:

- Página principal.
- Perfil Gerencial.
- Perfil Analista.
- Gráfico cualitativo.
- Gráfico cuantitativo.
- Inferencia cualitativa.
- Inferencia cuantitativa.
- Calculadora.
- Gráfico de residuos.
- Q-Q Plot.
- Histograma de residuos.

Resultado: navegación aprobada sin `NameError`, `KeyError`, `AttributeError`,
`ValueError` no controlado, claves duplicadas visibles, errores de importación
ni trazas técnicas. Se abrieron los expanders de base completa e histograma de
residuos.

## Fase P-09: diagnóstico de residuos y validación técnica de supuestos

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P09-T01 | Conservar cantidad de valores ajustados, residuos y residuos estandarizados. | Datos controlados. | Un valor por observación. | Coincidencia. | Aprobada | Diagnóstico completo. |
| P09-T02 | Verificar fórmula de residuo. | Datos controlados. | `observado - ajustado`. | Coincidencia. | Aprobada | Misma escala de autonomía. |
| P09-T03 | Verificar media de residuos. | Modelo con intercepto. | Media aproximadamente cero. | Coincidencia. | Aprobada | Tolerancia numérica. |
| P09-T04 | Confirmar residuos estandarizados finitos. | Datos controlados. | Todos finitos. | Cumple. | Aprobada | Calculados con Statsmodels. |
| P09-T05 | Verificar variabilidad residual positiva. | Datos no perfectos. | Desvío residual mayor que cero. | Cumple. | Aprobada | Evita diagnóstico degenerado. |
| P09-T06 | Reutilizar el mismo modelo lineal. | Datos controlados. | Ajustados coinciden con regresión previa. | Coincidencia. | Aprobada | No se ajusta otro modelo. |
| P09-T07 | Construir datos para residuos frente a ajustados. | Datos con contexto. | Misma cantidad de filas. | Coincidencia. | Aprobada | No filtra datos. |
| P09-T08 | Conservar columnas para tooltip. | Datos con contexto. | Observada, ajustada, residuo, estandarizado, X, sucursal y fallos. | Columnas presentes. | Aprobada | No agrega variables estadísticas. |
| P09-T09 | Marcar atípicos orientativos. | Diagnóstico controlado. | `|r| > 2` y `|r| > 3` detectados. | Conteos correctos. | Aprobada | No implica eliminación. |
| P09-T10 | Verificar conteos de atípicos. | Datos controlados. | Conteos iguales al cálculo manual. | Coincidencia. | Aprobada | Umbrales estrictos. |
| P09-T11 | No eliminar observaciones atípicas. | Diagnóstico controlado. | Se conservan todas las filas. | Cumple. | Aprobada | Solo se marcan puntos. |
| P09-T12 | Construir Q-Q Plot con todos los residuos. | Residuos del modelo. | Un punto por residuo. | Coincidencia. | Aprobada | Datos para Plotly. |
| P09-T13 | Ordenar cuantiles teóricos. | Q-Q Plot. | Orden creciente. | Cumple. | Aprobada | Requisito visual. |
| P09-T14 | Ordenar residuos del Q-Q Plot. | Q-Q Plot. | Orden creciente. | Cumple. | Aprobada | Salida de `probplot`. |
| P09-T15 | Verificar línea Q-Q finita. | Q-Q Plot. | Pendiente, intercepto y línea finitos. | Cumple. | Aprobada | Parámetros guardados en atributos. |
| P09-T16 | Construir histograma con todos los residuos. | Residuos del modelo. | Suma de frecuencias igual a n. | Coincidencia. | Aprobada | Histograma complementario. |
| P09-T17 | Validar intervalos del histograma. | Residuos del modelo. | Límite superior mayor que inferior. | Cumple. | Aprobada | Bins válidos. |
| P09-T18 | Rechazar residuos no finitos en histograma. | Serie con infinito. | Error comprensible. | Error comprensible. | Aprobada | Sin trazas técnicas. |
| P09-T19 | Rechazar X constante. | Datos controlados. | Error comprensible. | Error comprensible. | Aprobada | Sin variabilidad en X. |
| P09-T20 | Rechazar Y constante. | Datos controlados. | Error comprensible. | Error comprensible. | Aprobada | Sin variabilidad en Y. |
| P09-T21 | Rechazar residuos sin variabilidad. | Datos perfectamente lineales. | Error comprensible. | Error comprensible. | Aprobada | Tolerancia numérica `1e-12`. |
| P09-T22 | Validar Excel predeterminado. | `data/volt_ar_semana_01.xlsx`. | 48 residuos, media cercana a cero y desvío positivo. | Cumple. | Aprobada | Misma base semanal. |
| P09-T23 | Mostrar sección de validación técnica. | `pages/2_Perfil_Analista.py`. | Título y función presentes. | Presentes. | Aprobada | Página 2. |
| P09-T24 | Mostrar gráficos diagnósticos. | `pages/2_Perfil_Analista.py`. | Residuos-ajustados, Q-Q Plot e histograma. | Presentes. | Aprobada | Requisitos P-09. |
| P09-T25 | Incluir línea horizontal en cero. | `pages/2_Perfil_Analista.py`. | `add_hline(y=0)`. | Presente. | Aprobada | Referencia residual. |
| P09-T26 | Explicar normalidad sobre residuos. | `pages/2_Perfil_Analista.py`. | Texto referido a errores/residuos. | Presente. | Aprobada | No exige normalidad de X o Y. |
| P09-T27 | Evitar aprobación automática de supuestos. | `pages/2_Perfil_Analista.py`. | No contiene frases concluyentes prohibidas. | Cumple. | Aprobada | Interpretación prudente. |
| P09-T28 | Conservar P-06, P-07 y P-08. | `pages/2_Perfil_Analista.py`. | Inferencia cualitativa, inferencia cuantitativa y calculadora presentes. | Presentes. | Aprobada | P-09 se agrega debajo. |

Validación automatizada ejecutada:

```text
.\.venv\Scripts\python.exe -m pytest -q
203 passed
```

Validación de sintaxis ejecutada:

```text
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
Sin errores.
```

### Corrección posterior a la revisión manual

Durante la navegación manual a la sección "Residuos frente a valores ajustados"
se detectó un `NameError`. La página utilizaba `VARIABLE_SUCURSAL` y
`VARIABLE_NIVEL_FALLOS` en el tooltip del gráfico de residuos, pero no las
importaba desde `src.config`.

El inicio del servidor Streamlit no había detectado el problema porque la página
específica todavía no había sido ejecutada mediante navegación. Se agregaron
ambos imports canónicos. No se modificaron cálculos, residuos, gráficos ni
resultados estadísticos.

Se agregó el test `test_pagina_analista_importa_constantes_variables_usadas`,
basado en AST, para verificar que las constantes `VARIABLE_*` utilizadas por la
página existan y sean importadas desde `src.config`.

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P09-M01 | Navegar completamente a la Página 2. | Streamlit, `Perfil Analista`. | La página se ejecuta sin errores. | Navegación aprobada. | Aprobada | Validado luego de corregir imports. |
| P09-M02 | Renderizar residuos frente a valores ajustados. | Datos activos predeterminados. | Gráfico visible sin `NameError`. | Renderizado aprobado. | Aprobada | Usa el mismo modelo P-09. |
| P09-M03 | Renderizar Q-Q Plot. | Residuos del modelo. | Gráfico visible sin errores. | Renderizado aprobado. | Aprobada | Se conserva la línea de referencia. |
| P09-M04 | Renderizar histograma. | Residuos del modelo. | Histograma disponible en la sección. | Renderizado aprobado. | Aprobada | Complementario al Q-Q Plot. |
| P09-M05 | Verificar tooltips con variables de contexto. | Gráfico de residuos. | Tooltips con autonomía observada, ajustada, residuo, residuo estandarizado, antigüedad, sucursal y nivel de fallos. | Variables de contexto presentes. | Aprobada | Requiere imports canónicos. |
| P09-M06 | Confirmar ausencia del `NameError`. | `Perfil Analista`. | Sin error por constantes no definidas. | Sin `NameError`. | Aprobada | Corrección validada manualmente. |
| P09-M07 | Ejecutar pruebas automatizadas posteriores. | Pytest completo. | 204 pruebas aprobadas. | `204 passed`. | Aprobada | Incluye test AST preventivo. |

Validación automatizada posterior a la corrección:

```text
.\.venv\Scripts\python.exe -m pytest -q
204 passed
```

## Fase P-08: calculadora de predicción

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P08-T01 | Verificar predicción puntual. | Datos controlados. | `b0 + b1 * x0`. | Coincidencia. | Aprobada | Usa el mismo modelo OLS. |
| P08-T02 | Comparar con `get_prediction`. | Datos controlados. | Coincidencia completa. | Coincidencia. | Aprobada | Statsmodels como referencia. |
| P08-T03 | Asignar intervalo de media. | `summary_frame`. | Usa `mean_ci_lower` y `mean_ci_upper`. | Correcto. | Aprobada | Sin intercambio de columnas. |
| P08-T04 | Asignar intervalo individual. | `summary_frame`. | Usa `obs_ci_lower` y `obs_ci_upper`. | Correcto. | Aprobada | Sin intercambio de columnas. |
| P08-T05 | Comparar amplitudes. | Datos controlados. | Individual >= media. | Cumple. | Aprobada | Condición estadística. |
| P08-T06 | Verificar predicción dentro del IC media. | Datos controlados. | Predicción contenida. | Contenida. | Aprobada | Control de consistencia. |
| P08-T07 | Verificar predicción dentro del intervalo individual. | Datos controlados. | Predicción contenida. | Contenida. | Aprobada | Control de consistencia. |
| P08-T08 | Ampliar intervalos con mayor confianza. | 90 % y 99 %. | Ambos se amplían. | Cumple. | Aprobada | Predicción no cambia. |
| P08-T09 | Mantener predicción puntual. | 90 % y 99 %. | Misma predicción. | Coincidencia. | Aprobada | Solo cambian límites. |
| P08-T10 | Detectar interpolación. | Valor dentro del rango observado. | `es_extrapolacion=False`. | Correcto. | Aprobada | Rango observado dinámico. |
| P08-T11 | Detectar extrapolación inferior. | X = 1 con mínimo observado mayor. | Extrapolación. | Correcto. | Aprobada | No bloquea el cálculo. |
| P08-T12 | Detectar extrapolación superior. | X = 48 con máximo observado menor. | Extrapolación. | Correcto. | Aprobada | No bloquea el cálculo. |
| P08-T13 | Aceptar rango operativo. | X = 1 y X = 48. | Valores aceptados. | Aceptados. | Aprobada | Rango 1-48. |
| P08-T14 | Rechazar valor menor que 1. | X = 0. | Error comprensible. | Error comprensible. | Aprobada | Control operativo. |
| P08-T15 | Rechazar valor mayor que 48. | X = 49. | Error comprensible. | Error comprensible. | Aprobada | Control operativo. |
| P08-T16 | Rechazar valor no finito. | X infinito. | Error comprensible. | Error comprensible. | Aprobada | Control numérico. |
| P08-T17 | No recortar intervalos. | Excel predeterminado, X = 48. | Límite individual puede quedar bajo 15. | Se conserva sin recorte. | Aprobada | Respeta resultado del modelo. |
| P08-T18 | Validar Excel predeterminado. | X = 24. | Predicción aproximada 31.90 km. | 31.899631598222 km. | Aprobada | Interpolación. |
| P08-T19 | Confirmar P-06 y P-07 presentes. | `pages/2_Perfil_Analista.py`. | Secciones conservadas. | Conservadas. | Aprobada | No se eliminó inferencia. |
| P08-T20 | Confirmar diagnósticos ausentes. | `pages/2_Perfil_Analista.py`. | Sin gráficos de diagnóstico. | Ausentes. | Aprobada | Fases posteriores. |
| P08-T21 | Confirmar ausencia de lenguaje causal. | `pages/2_Perfil_Analista.py`. | Sin causalidad. | Sin causalidad. | Aprobada | Estimación, no causalidad. |
| P08-T22 | Construir bandas para gráfico. | Datos controlados. | Columnas de recta, media e individual. | Correcto. | Aprobada | Mismo modelo y confianza. |

Validación automatizada ejecutada:

```text
.\.venv\Scripts\python.exe -m pytest -q
175 passed
```

Validación de sintaxis ejecutada:

```text
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
Sin errores.
```

## Fase P-07: inferencia cuantitativa

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P07-T01 | Verificar grados de libertad. | DataFrame controlado. | `gl = n - 2`. | Coincidencia. | Aprobada | Regresión simple con intercepto. |
| P07-T02 | Verificar estadístico t. | Resultado inferencial. | `t = b1 / SE(b1)`. | Coincidencia. | Aprobada | Control matemático. |
| P07-T03 | Comparar t con fórmula basada en Pearson. | Datos no perfectos. | Coincidencia. | Coincidencia. | Aprobada | Equivalencia en regresión simple. |
| P07-T04 | Verificar rango del p-valor. | Datos no perfectos. | Entre 0 y 1. | Dentro de rango. | Aprobada | P-valor bilateral. |
| P07-T05 | Comparar p-valor con Statsmodels. | Mismo modelo OLS. | Coincidencia. | Coincidencia. | Aprobada | Statsmodels como fuente principal. |
| P07-T06 | Decidir rechazo. | p 0.01, α 0.05. | Se rechaza H0. | Se rechaza H0. | Aprobada | Regla `p < α`. |
| P07-T07 | Decidir no rechazo. | p 0.08 y p 0.05 con α 0.05. | No se rechaza H0. | No se rechaza H0. | Aprobada | Regla `p >= α`. |
| P07-T08 | Evitar "aceptar H0". | Texto de decisión. | No contiene aceptar. | No contiene aceptar. | Aprobada | Respeta consigna. |
| P07-T09 | Conclusión contextual negativa. | Pendiente negativa. | Relación lineal negativa. | Texto correcto. | Aprobada | Escenario simulado. |
| P07-T10 | Conclusión contextual positiva. | Pendiente positiva. | Relación lineal positiva. | Texto correcto. | Aprobada | Sentido dinámico. |
| P07-T11 | Conclusión de no rechazo. | p 0.20. | No afirma evidencia suficiente. | Texto correcto. | Aprobada | No acepta H0. |
| P07-T12 | Comparar IC de pendiente con Statsmodels. | 95 %. | Coincidencia. | Coincidencia. | Aprobada | `conf_int`. |
| P07-T13 | Comparar IC de intercepto con Statsmodels. | 95 %. | Coincidencia. | Coincidencia. | Aprobada | `conf_int`. |
| P07-T14 | Verificar ampliación de intervalos. | 90 % y 99 %. | 99 % más ancho. | Más ancho. | Aprobada | Mayor confianza. |
| P07-T15 | Verificar estimadores constantes. | 90 % y 99 %. | Estimadores y p-valor iguales. | Iguales. | Aprobada | Solo cambian límites. |
| P07-T16 | Confirmar p-valor independiente de α. | α 0.01 y 0.10. | p-valor sin cambios. | Sin cambios. | Aprobada | Solo cambia decisión. |
| P07-T17 | Validar límites de Fisher. | Datos no perfectos. | Intervalo dentro de [-1, 1]. | Dentro de rango. | Aprobada | Aproximación de Fisher. |
| P07-T18 | Verificar que Fisher contiene r. | Datos no perfectos. | r dentro del intervalo. | Contenido. | Aprobada | Control de consistencia. |
| P07-T19 | Manejar `n <= 3`. | Tres observaciones. | Error comprensible. | Error comprensible. | Aprobada | Inferencia requiere al menos cuatro. |
| P07-T20 | Manejar correlación perfecta. | r = ±1. | Fisher no calculable. | `None`. | Aprobada | Resultado controlado. |
| P07-T21 | Error con X constante. | DataFrame controlado. | Error comprensible. | Error comprensible. | Aprobada | Sin variabilidad. |
| P07-T22 | Error con Y constante. | DataFrame controlado. | Error comprensible. | Error comprensible. | Aprobada | Sin variabilidad. |
| P07-T23 | Validar Excel predeterminado. | `data/volt_ar_semana_01.xlsx`. | n 48, gl 46, t -14.0468, p 2.97e-18. | Coincidencia. | Aprobada | Reproduce P-07 esperado. |
| P07-T24 | Confirmar P-06 presente. | `pages/2_Perfil_Analista.py`. | Inferencia cualitativa conservada. | Conservada. | Aprobada | No se elimina P-06. |
| P07-T25 | Confirmar P-04 y P-05 presentes. | `pages/1_Perfil_Gerencial.py`. | Módulos gerenciales conservados. | Conservados. | Aprobada | Sin cambios funcionales. |
| P07-T26 | Confirmar herramientas pendientes ausentes. | `pages/2_Perfil_Analista.py`. | Sin Q-Q, histograma, predicción individual ni calculadora. | Ausentes. | Aprobada | Fases posteriores. |
| P07-T27 | Confirmar ausencia de lenguaje causal. | `pages/2_Perfil_Analista.py`. | No contiene lenguaje causal. | Aprobada. | Aprobada | Se habla de relación lineal. |

Validación automatizada ejecutada:

```text
.\.venv\Scripts\python.exe -m pytest -q
154 passed
```

Validación de sintaxis ejecutada:

```text
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
Sin errores.
```

Validación temporal de Streamlit:

```text
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless=true --server.address=127.0.0.1 --server.port=8765 --server.runOnSave=false
Inicio controlado sin errores visibles de importación o sintaxis; el proceso fue detenido.
```

## Fase P-06: inferencia cualitativa

| Código de prueba | Objetivo | Datos utilizados | Resultado esperado | Resultado obtenido | Estado | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| P06-T01 | Calcular frecuencias esperadas. | Tabla predeterminada. | `[[8.5, 9.5, 6.0], [8.5, 9.5, 6.0]]`. | Coincidencia. | Aprobada | Fórmula de independencia. |
| P06-T02 | Verificar fórmula manual de una celda. | Rosario-Bajo. | `24 * 17 / 48 = 8.5`. | 8.5. | Aprobada | Control de Eij. |
| P06-T03 | Conservar etiquetas y orden. | Tabla efectiva. | Rosario, Córdoba; Bajo, Medio, Alto. | Orden conservado. | Aprobada | Mantiene estructura P-04. |
| P06-T04 | Igualar suma observada y esperada. | Tabla predeterminada. | Total 48. | Total 48. | Aprobada | Control de consistencia. |
| P06-T05 | Calcular diferencias relativas. | Observadas y esperadas predeterminadas. | Porcentajes esperados. | Coincidencia. | Aprobada | Convención `(O - E) / E * 100`. |
| P06-T06 | Verificar signo positivo. | O > E. | Diferencia positiva. | Positiva. | Aprobada | Interpretación por celda. |
| P06-T07 | Verificar signo negativo. | O < E. | Diferencia negativa. | Negativa. | Aprobada | Interpretación por celda. |
| P06-T08 | Verificar diferencia cero. | O = E. | 0 %. | 0 %. | Aprobada | Caso neutro. |
| P06-T09 | Calcular aportes por celda. | Observadas y esperadas predeterminadas. | `(O - E)^2 / E`. | Coincidencia. | Aprobada | Complemento técnico. |
| P06-T10 | Sumar aportes. | Tabla predeterminada. | Suma igual a Chi-cuadrado. | 19.170279. | Aprobada | Coincide con el estadístico. |
| P06-T11 | Evaluar robustez cumplida. | Esperadas predeterminadas. | Mínima 6, 100 % >= 5. | Robusta. | Aprobada | Criterios cumplidos. |
| P06-T12 | Detectar esperada menor que 1. | Tabla esperada controlada. | Incumplimiento absoluto. | Incumplimiento detectado. | Aprobada | No bloquea cálculo. |
| P06-T13 | Detectar incumplimiento del 80 %. | Tabla esperada controlada. | No robusta. | No robusta. | Aprobada | Porcentaje >= 5 insuficiente. |
| P06-T14 | Confirmar p-valor independiente de α. | α 0.01 y 0.10. | p-valor sin cambios. | Sin cambios. | Aprobada | Solo cambia decisión. |
| P06-T15 | Decidir rechazo. | p 0.01, α 0.05. | Se rechaza H0. | Se rechaza H0. | Aprobada | Regla `p < α`. |
| P06-T16 | Decidir no rechazo. | p 0.08 y p 0.05 con α 0.05. | No se rechaza H0. | No se rechaza H0. | Aprobada | Regla `p >= α`. |
| P06-T17 | Evitar "aceptar H0". | Texto de decisión. | No contiene aceptar. | No contiene aceptar. | Aprobada | Respeta consigna. |
| P06-T18 | Conclusión de rechazo contextualizada. | p 0.01, α 0.05. | Asociación y escenario simulado. | Texto correcto. | Aprobada | Conclusión poblacional simulada. |
| P06-T19 | Conclusión de no rechazo cautelosa. | p 0.08, α 0.05. | No afirma independencia definitiva. | Texto correcto. | Aprobada | Evita conclusión categórica. |
| P06-T20 | Validar resultado predeterminado. | `data/volt_ar_semana_01.xlsx`. | Chi-cuadrado 19.170279, gl 2, p 0.000068742747. | Coincidencia. | Aprobada | Reproduce la referencia esperada. |
| P06-T21 | Manejar categoría ausente. | Tabla sin `Alto`. | Exclusión informada. | `Alto` excluida. | Aprobada | No inventa frecuencias. |
| P06-T22 | Error con una sola categoría efectiva. | Tabla degenerada. | Error comprensible. | Error comprensible. | Aprobada | No muestra traza técnica. |
| P06-T23 | Verificar hipótesis en Página 2. | `pages/2_Perfil_Analista.py`. | Contiene H0 y H1. | Contiene H0 y H1. | Aprobada | Con símbolos H₀ y H₁. |
| P06-T24 | Verificar independencia como supuesto de diseño. | `pages/2_Perfil_Analista.py`. | Aclaración visible. | Aclaración presente. | Aprobada | No se marca como comprobada. |
| P06-T25 | Confirmar P-04 y P-05 presentes. | `pages/1_Perfil_Gerencial.py`. | Módulos gerenciales conservados. | Conservados. | Aprobada | No se modificó funcionalidad gerencial. |

Validación automatizada ejecutada:

```text
.\.venv\Scripts\python.exe -m pytest -q
127 passed
```

Validación de sintaxis ejecutada:

```text
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
Sin errores.
```
