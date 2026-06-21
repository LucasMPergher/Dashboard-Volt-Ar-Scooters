# Diccionario de datos

El proyecto define exactamente cuatro variables estadísticas. La columna
`ID_Monopatin` puede existir como identificador en etapas posteriores, pero no se
considera una quinta variable estadística y no forma parte del archivo simulado
de P-02.

Orden obligatorio de columnas del DataFrame y del Excel simulado:

1. `Sucursal`
2. `Nivel_Fallos`
3. `Antiguedad_Bateria_Meses`
4. `Autonomia_Real_Km`

| Nombre | Tipo | Escala | Categorías o unidad | Rango | Descripción | Función dentro del análisis |
| --- | --- | --- | --- | --- | --- | --- |
| `Sucursal` | Cualitativa | Nominal | Rosario, Córdoba | No aplica | Sucursal donde se releva el monopatín eléctrico. | Variable cualitativa para describir y contrastar distribuciones por sede. |
| `Nivel_Fallos` | Cualitativa | Ordinal | Bajo, Medio, Alto | No aplica | Nivel simulado de fallos del monopatín durante el período semanal. | Variable cualitativa ordinal para analizar asociación con la sucursal. |
| `Antiguedad_Bateria_Meses` | Cuantitativa | Razón | Meses | 1 a 48 | Antigüedad de la batería medida en meses enteros. | Variable independiente X para estudiar su relación con la autonomía real. |
| `Autonomia_Real_Km` | Cuantitativa | Razón | Kilómetros | 15 a 45 | Autonomía real simulada del monopatín, redondeada a dos decimales. | Variable dependiente Y para el futuro modelo cuantitativo. |
