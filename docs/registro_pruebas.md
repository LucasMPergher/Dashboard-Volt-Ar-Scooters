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

Validación temporal de Streamlit:

```text
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless=true --server.address=127.0.0.1 --server.port=8765 --server.runOnSave=false
Inicio controlado sin errores visibles de importación o sintaxis; el proceso fue detenido.
```
