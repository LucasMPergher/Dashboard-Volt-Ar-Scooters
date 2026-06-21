# Diccionario de datos

El proyecto define exactamente cuatro variables estadísticas. La columna
`ID_Monopatin` puede existir como identificador, pero no se considera una quinta
variable estadística.

| Nombre | Tipo | Escala | Categorías o unidad | Descripción | Función dentro del análisis |
| --- | --- | --- | --- | --- | --- |
| `Sucursal` | Cualitativa | Nominal | Rosario, Córdoba | Sucursal donde se releva el monopatín eléctrico. | Variable cualitativa para describir y contrastar distribuciones por sede. |
| `Nivel_Fallos` | Cualitativa | Ordinal | Bajo, Medio, Alto | Nivel observado de fallos del monopatín durante el período semanal. | Variable cualitativa ordinal para analizar asociación con la sucursal. |
| `Antiguedad_Bateria_Meses` | Cuantitativa | Razón | Meses | Antigüedad de la batería medida en meses. | Variable independiente X para estudiar su relación con la autonomía real. |
| `Autonomia_Real_Km` | Cuantitativa | Razón | Kilómetros | Autonomía real observada del monopatín medida en kilómetros. | Variable dependiente Y para el futuro modelo cuantitativo. |
