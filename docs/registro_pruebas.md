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
