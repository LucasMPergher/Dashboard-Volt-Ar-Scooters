# Dashboard-Volt-Ar-Scooters

Dashboard académico de Estadística II para analizar semanalmente monopatines
eléctricos de Volt-Ar Scooters.

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

La calculadora de predicción se presenta más abajo. Los diagnósticos del modelo
se incorporarán en fases posteriores.

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
se recalculan cuando cambia el nivel de confianza. La página no implementa
todavía diagnósticos del modelo.

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
