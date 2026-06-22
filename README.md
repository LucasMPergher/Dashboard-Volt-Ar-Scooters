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
