# Dashboard-Volt-Ar-Scooters

Dashboard académico de Estadística II para analizar semanalmente monopatines
eléctricos de Volt-Ar Scooters.

## Objetivos

- Integrar una carga semanal de datos de monopatines eléctricos.
- Presentar un perfil gerencial descriptivo y muestral.
- Presentar un perfil analista con inferencia, predicción y diagnóstico técnico.
- Mantener separados los resultados muestrales de las conclusiones
  poblacionales simuladas.
- Documentar el uso de inteligencia artificial y la validación humana.

## Variables analizadas

El dashboard trabaja exactamente con cuatro variables estadísticas:

| Variable | Tipo | Escala | Rol |
| --- | --- | --- | --- |
| `Sucursal` | Cualitativa | Nominal | Sede Rosario o Córdoba. |
| `Nivel_Fallos` | Cualitativa | Ordinal | Nivel Bajo, Medio o Alto. |
| `Antiguedad_Bateria_Meses` | Cuantitativa | Razón | Variable independiente X. |
| `Autonomia_Real_Km` | Cuantitativa | Razón | Variable dependiente Y. |

`ID_Monopatin` puede existir como identificador externo, pero no forma parte de
las cuatro variables estadísticas del proyecto.

## Requisitos de Python

Se recomienda usar Python 3.11 o superior y un entorno virtual local.

Crear el entorno:

```powershell
python -m venv .venv
```

Activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Generar datos semanales simulados

La fase P-02 incorpora un generador reproducible de datos semanales. Para crear
el archivo inicial de la semana 1 con 48 observaciones y semilla 42:

```powershell
.\.venv\Scripts\python.exe -m src.simulacion_datos --cantidad 48 --semilla 42 --semana 1
```

El comando genera:

```text
data/volt_ar_semana_01.xlsx
```

El archivo contiene la hoja `datos` y exactamente cuatro columnas estadísticas,
en este orden:

1. `Sucursal`
2. `Nivel_Fallos`
3. `Antiguedad_Bateria_Meses`
4. `Autonomia_Real_Km`

La semana se identifica únicamente mediante el nombre del archivo. No se agrega
columna de ID, semana, fecha, modelo, temperatura ni otra quinta variable.

## Cargar actualización semanal

La fase P-03 permite cargar una matriz semanal desde la barra lateral de
Streamlit. Se admiten archivos `.xlsx` y `.csv`.

Para iniciar la aplicación:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Reglas principales de carga:

- Los Excel deben contener una hoja llamada `datos`.
- Los CSV deben estar codificados en UTF-8 y pueden usar coma o punto y coma.
- El archivo debe tener exactamente las cuatro columnas estadísticas requeridas.
- Si las columnas están en otro orden, se reordenan al orden canónico.
- Se rechazan columnas faltantes, columnas adicionales, columnas `Unnamed`,
  archivos vacíos, valores nulos y muestras fuera del rango 30-60.
- Los datos válidos quedan disponibles en `st.session_state["datos_activos"]`.
- El nombre del archivo activo queda disponible en
  `st.session_state["nombre_archivo_activo"]`.
- Si una carga es inválida, los datos activos anteriores no se sustituyen.

Mientras no se cargue otro archivo válido, la aplicación utiliza
`data/volt_ar_semana_01.xlsx` como archivo predeterminado.

## Formato esperado de Excel y CSV

Los archivos deben contener exactamente estas columnas, aunque la validación
puede reordenarlas al orden canónico:

```text
Sucursal,Nivel_Fallos,Antiguedad_Bateria_Meses,Autonomia_Real_Km
```

Reglas principales:

- `Sucursal`: Rosario o Córdoba.
- `Nivel_Fallos`: Bajo, Medio o Alto.
- `Antiguedad_Bateria_Meses`: entero de 1 a 48.
- `Autonomia_Real_Km`: número de 15 a 45.
- Cantidad de observaciones: entre 30 y 60.
- Excel: hoja obligatoria `datos`.
- CSV: UTF-8, separado por coma o punto y coma.
- No se admiten columnas adicionales, columnas faltantes, columnas `Unnamed`,
  valores nulos ni infinitos.

## Página gerencial: análisis cualitativo

La Página 1 incorpora un módulo descriptivo y muestral para analizar la relación
observada entre `Sucursal` y `Nivel_Fallos`.

Incluye:

- tabla de contingencia observada con totales marginales;
- gráfico de barras agrupadas;
- gráfico de barras apiladas al 100 %;
- estadístico Chi-cuadrado muestral, grados de libertad y p-valor;
- selector de nivel de significancia para una comparación neutral.

La página no presenta una conclusión inferencial. La decisión formal sobre la
población se reserva para la Página 2.

## Página gerencial: análisis cuantitativo

La Página 1 también incorpora un módulo descriptivo y muestral para analizar la
relación observada entre `Antiguedad_Bateria_Meses` y `Autonomia_Real_Km`.

Incluye:

- gráfico de dispersión interactivo con un punto por monopatín;
- recta de regresión lineal muestral global;
- ecuación de la recta con autonomía en kilómetros y antigüedad en meses;
- coeficiente de correlación de Pearson;
- coeficiente de determinación R²;
- interpretación descriptiva de la dirección e intensidad observadas en la
  muestra.

La recta del gráfico y los KPI utilizan el mismo modelo ajustado. Esta página no
presenta causalidad, intervalos, predicciones ni conclusiones sobre la
población; esos elementos quedan reservados para la Página 2.

## Página analista: inferencia cualitativa

La Página 2 incorpora la prueba Chi-cuadrado de independencia para evaluar la
asociación poblacional entre `Sucursal` y `Nivel_Fallos`.

Incluye:

- hipótesis nula y alternativa;
- frecuencias observadas y esperadas;
- diferencias relativas porcentuales con la convención `(O - E) / E * 100`;
- aporte de cada celda al estadístico Chi-cuadrado;
- estadístico Chi-cuadrado, grados de libertad y p-valor;
- selector de nivel de significancia para actualizar la decisión;
- conclusión contextual para el escenario poblacional simulado;
- evaluación de supuestos y robustez de frecuencias esperadas.

La inferencia cuantitativa, la calculadora de predicción y la validación
técnica de supuestos se presentan más abajo.

## Página analista: inferencia cuantitativa

La Página 2 incorpora la prueba bilateral para la pendiente poblacional de la
regresión lineal simple entre `Antiguedad_Bateria_Meses` y `Autonomia_Real_Km`.

Incluye:

- modelo poblacional `Y = β₀ + β₁X + ε`;
- hipótesis `H₀: β₁ = 0` y `H₁: β₁ ≠ 0`;
- pendiente estimada, error estándar, estadístico t, grados de libertad y
  p-valor;
- selector de nivel de significancia para actualizar la decisión;
- conclusión contextual para el escenario poblacional simulado;
- intervalos de confianza dinámicos para `β₀` y `β₁`;
- intervalo para `ρ` mediante la aproximación de Fisher.

El p-valor no cambia al modificar `α`; solo cambia la decisión. Los intervalos
se recalculan cuando cambia el nivel de confianza. Los diagnósticos del modelo
se presentan en la sección de validación técnica de supuestos.

## Página analista: calculadora de predicción

La Página 2 incorpora una calculadora técnica para estimar la autonomía a partir
de una antigüedad de batería ingresada por el analista.

Incluye:

- predicción puntual de autonomía;
- intervalo de confianza para la autonomía promedio esperada;
- intervalo de predicción para un monopatín individual;
- advertencia cuando el valor ingresado implica extrapolación;
- comparación de amplitudes entre ambos intervalos;
- gráfico técnico con recta del modelo, bandas y marcador del valor ingresado.

El intervalo individual es más amplio que el intervalo para la media esperada
porque incorpora la incertidumbre sobre la media y la variabilidad individual
alrededor de la recta. Los intervalos estadísticos no se recortan al rango
operativo de la simulación.

## Página analista: validación técnica de supuestos

La Página 2 incorpora una sección de diagnóstico de residuos para evaluar la
compatibilidad técnica del modelo lineal con los supuestos principales.

Incluye:

- gráfico de residuos frente a valores ajustados;
- Q-Q Plot de residuos con línea de referencia normal;
- histograma de residuos como complemento;
- media y desviación estándar de residuos;
- conteos orientativos de residuos estandarizados con `|r| > 2` y `|r| > 3`;
- aclaraciones sobre linealidad, homocedasticidad, normalidad de errores e
  independencia de observaciones.

Los conteos de residuos estandarizados no eliminan observaciones ni constituyen
una prueba definitiva. Los gráficos requieren interpretación conjunta con el
contexto y el diseño de recolección.

## Ejecutar pruebas

Validar sintaxis:

```powershell
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
```

Ejecutar toda la suite:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Ejecutar solo integración:

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_integracion_dashboard.py
```

## Estructura de carpetas

```text
Dashboard-Volt-Ar-Scooters/
├── app.py
├── pages/
├── src/
├── tests/
├── data/
└── docs/
```

- `pages/`: páginas de Streamlit.
- `src/`: carga, validación, simulación y análisis estadístico.
- `tests/`: pruebas automatizadas unitarias e integrales.
- `data/`: archivo semanal predeterminado.
- `docs/`: documentación metodológica, prompts, registro de pruebas y matriz de
  cumplimiento.

## Limitaciones

- Los datos semanales son simulados con fines académicos.
- Las conclusiones poblacionales corresponden al escenario simulado.
- La aplicación no implementa autenticación, base de datos ni API externa.
- Los diagnósticos de residuos requieren interpretación humana; no aprueban ni
  invalidan automáticamente el modelo.
- La independencia de observaciones depende del diseño de recolección y no puede
  verificarse completamente con los gráficos.

## Uso de inteligencia artificial

El proyecto documenta el uso de IA en `docs/prompts.md`. La IA se utiliza como
asistente de programación, documentación y revisión, pero los integrantes deben
comprender, revisar y probar todo el código y los resultados antes de
incorporarlos al trabajo académico.

## Validación humana

La validación humana queda registrada en `docs/registro_pruebas.md`. Los
resultados estadísticos no deben aceptarse únicamente por ser generados por el
dashboard; deben revisarse con criterio teórico, técnico y metodológico.
