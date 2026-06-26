# Registro de prompts y uso de inteligencia artificial

La inteligencia artificial se utiliza en este proyecto como asistente de
programación, documentación y revisión. Los integrantes deben comprender,
verificar y probar todo el código generado antes de incorporarlo al trabajo.
Los resultados estadísticos no serán aceptados sin validación teórica y técnica.
Se documentarán tanto los resultados exitosos como los errores y correcciones.

| Código | Fecha | Herramienta | Etapa | Objetivo | Resultado | Validación | Commit |
| ------ | ----- | ----------- | ----- | -------- | --------- | ---------- | ------ |
| P-00 | 2026-06-21 | Codex | Inspección del repositorio | Verificar repositorio, rama activa, remoto y estado del árbol de trabajo antes de realizar modificaciones. | Se confirmó el repositorio `Dashboard-Volt-Ar-Scooters`, la rama `setup-inicial`, el remoto correcto y el árbol de trabajo limpio. | `git branch --show-current`; `git remote -v`; `git status`. | No aplica, porque no se modificaron archivos. |
| P-01 | 2026-06-21 | Codex | Configuración inicial del proyecto | Crear la estructura inicial del dashboard académico con Python y Streamlit. | Se creó la estructura de carpetas, portada, páginas de Streamlit, configuración de cuatro variables estadísticas, documentos metodológicos y pruebas iniciales reales. | Compilación Python correcta; `10 passed` con Pytest; Streamlit inició localmente; `git diff --check` sin errores; `.venv` ignorado por Git. | Propuesto: `chore: crear estructura inicial del dashboard`. |
| P-02 | 2026-06-21 | Codex | Simulación de datos | Implementar un generador reproducible de datos semanales simulados y crear `data/volt_ar_semana_01.xlsx`. | Se implementó el simulador, la CLI, las validaciones técnicas, las pruebas automatizadas y el archivo Excel inicial. | Compilación Python correcta; `32 passed` con Pytest; CLI generó el Excel; métricas revisadas con Pandas; `git diff --check` sin errores. | Propuesto: `feat: agregar simulacion reproducible de datos semanales`. |
| P-03 | 2026-06-21 | Codex | Carga y validación | Implementar carga dinámica de archivos semanales y validar su estructura antes de usarlos en el dashboard. | Se implementó carga de `.xlsx` y `.csv`, validación/normalización, componente Streamlit con `session_state` y pruebas automatizadas. | Compilación Python correcta; `55 passed` con Pytest; Streamlit inició localmente; `git diff --check` sin errores. | Propuesto: `feat: agregar carga y validacion de datos semanales`. |
| P-04 | 2026-06-21 | Codex | Módulo cualitativo gerencial | Implementar el análisis cualitativo descriptivo y muestral de la Página 1. | Se implementó tabla de contingencia, marginales, gráficos, Chi-cuadrado muestral y métricas sin conclusión inferencial. | Compilación Python correcta; `71 passed` con Pytest; Streamlit inició localmente; `git diff --check` sin errores. | Propuesto: `feat: agregar modulo cualitativo gerencial`. |
| P-05 | 2026-06-21 | Codex | Módulo cuantitativo gerencial | Implementar el análisis cuantitativo descriptivo y muestral de la Página 1. | Se implementó regresión lineal muestral, Pearson, R², recta de regresión, ecuación e interpretaciones descriptivas. | Compilación Python correcta; `102 passed` con Pytest; Streamlit inició localmente. | Propuesto: `feat: agregar modulo cuantitativo gerencial`. |
| P-06 | 2026-06-21 | Codex | Inferencia cualitativa | Implementar la prueba Chi-cuadrado de independencia en la Página 2. | Se implementaron hipótesis, frecuencias esperadas, diferencias relativas, aportes por celda, decisión, conclusión y robustez. | Compilación Python correcta; `127 passed` con Pytest; Streamlit inició localmente. | Propuesto: `feat: agregar inferencia cualitativa`. |
| P-07 | 2026-06-26 | Codex | Inferencia cuantitativa | Implementar la prueba t bilateral para la pendiente poblacional y los intervalos de confianza en la Página 2. | Se implementaron inferencia de regresión, decisión, conclusión, IC para β₀/β₁ e intervalo de Fisher para ρ. | Compilación Python correcta; `154 passed` con Pytest. | Propuesto: `feat: agregar inferencia cuantitativa`. |
| P-08 | 2026-06-26 | Codex | Calculadora de predicción | Implementar la calculadora técnica de autonomía con intervalo para media e intervalo individual. | Se implementó predicción con Statsmodels, extrapolación, amplitudes, gráfico técnico y documentación. | Compilación Python correcta; `175 passed` con Pytest. | Propuesto: `feat: agregar calculadora de prediccion`. |
| P-09 | 2026-06-26 | Codex | Diagnóstico de residuos | Implementar gráficos y métricas de diagnóstico residual para validar técnicamente supuestos del modelo lineal en la Página 2. | Se implementaron residuos, residuos estandarizados, gráfico residuos-ajustados, Q-Q Plot, histograma, textos prudentes y pruebas P-09. | Compilación Python correcta; `203 passed` con Pytest. | Propuesto: `feat: agregar diagnostico de residuos`. |
| P-10 | 2026-06-26 | Codex | Integración final | Revisar el dashboard completo, agregar pruebas de integración, matriz de cumplimiento y documentación final. | Se agregaron pruebas integrales, matriz de cumplimiento, documentación final y correcciones menores de textos de integración. | Integración aislada: `40 passed`; suite completa: `244 passed`. | Propuesto: `chore: completar integracion y control de calidad`. |

## P-00 — Inspección del repositorio

### Objetivo

Verificar el repositorio, la rama activa, el remoto y el estado del árbol de
trabajo antes de realizar modificaciones.

### Prompt enviado

```text
[Pegar aquí el prompt completo enviado a Codex]
```

### Respuesta relevante del agente

Se confirmó que el repositorio correspondía a `Dashboard-Volt-Ar-Scooters`, que
la rama activa era `setup-inicial`, que el remoto `origin` apuntaba al
repositorio correcto de GitHub y que el árbol de trabajo estaba limpio.

### Problemas encontrados

- Error inicial del sandbox de Windows: `CreateProcessAsUserW failed: 1920`.
- Advertencia no fatal de PowerShell relacionada con `PSReadLine`.
- Se comprobó que no era necesario disponer de `package.json`, porque el
  proyecto utiliza Python.

### Decisiones humanas

Se aceptó que el nombre oficial del repositorio fuera
`Dashboard-Volt-Ar-Scooters`. La diferencia con una denominación previa no se
consideró un problema para continuar.

### Validación

- `git branch --show-current`
- `git remote -v`
- `git status`

## P-01 — Configuración inicial del proyecto

### Objetivo

Crear la estructura inicial del dashboard académico con Python y Streamlit,
manteniendo separadas la interfaz y la lógica estadística.

### Prompt enviado

```text
[Pegar aquí el prompt completo enviado a Codex]
```

### Respuesta relevante del agente

Se creó la estructura de carpetas del proyecto, la portada `app.py`, las páginas
`1_Perfil_Gerencial.py` y `2_Perfil_Analista.py`, la configuración central de
variables, documentos metodológicos y pruebas iniciales reales. Se declararon
exactamente cuatro variables estadísticas y se dejó `ID_Monopatin` como
identificador opcional, sin tratarlo como quinta variable.

### Problemas encontrados

- En la primera ejecución no estaban instalados `pytest` ni `streamlit`.
- Se creó un entorno virtual `.venv` y se instalaron las dependencias.

### Decisiones humanas

Se aprobó la revisión técnica de la fase inicial. Se indicó que el archivo
`docs/prompts.md` debía completarse para poder usarse como anexo académico.

### Validación

- Compilación de archivos Python correcta.
- `10 passed` con Pytest.
- Streamlit inició correctamente en modo local.
- `git diff --check` no encontró errores.
- `.venv` quedó ignorado por Git.

## P-02 — Simulación de datos

### Fecha

2026-06-21.

### Herramienta

Codex.

### Etapa

Simulación de datos.

### Objetivo

Implementar un generador reproducible de datos simulados para Volt-Ar Scooters,
crear `data/volt_ar_semana_01.xlsx` y validar técnicamente el conjunto generado
sin implementar todavía análisis inferenciales ni páginas funcionales.

### Prompt completo

````text
Trabaja exclusivamente en la rama actual `feat/simulacion-datos`.

Antes de comenzar:

1. Lee `AGENTS.md`.
2. Inspecciona `src/config.py`, `src/simulacion_datos.py`, los tests existentes y la documentación.
3. Ejecuta `git status --short --branch`.
4. Presenta un plan breve.
5. No cambies de rama.
6. No realices commit, push, merge ni Pull Request.

# Fase P-02: simulación reproducible de datos semanales

## Objetivo

Implementar un generador reproducible de datos simulados para Volt-Ar Scooters y crear el archivo inicial:

`data/volt_ar_semana_01.xlsx`

Esta fase debe limitarse a la simulación, validación técnica del conjunto generado y documentación.

No implementes todavía:

* Carga interactiva de Excel en Streamlit.
* Página gerencial funcional.
* Página analista funcional.
* Módulo definitivo de Chi-cuadrado.
* Regresión en la interfaz.
* Intervalos de confianza.
* Predicciones.
* Conclusiones inferenciales.

# Unidad de análisis

Cada fila debe representar un monopatín eléctrico observado durante una semana.

# Estructura obligatoria

El DataFrame y el Excel deben contener exactamente estas cuatro columnas estadísticas, en este orden:

1. `Sucursal`
2. `Nivel_Fallos`
3. `Antiguedad_Bateria_Meses`
4. `Autonomia_Real_Km`

No agregues:

* ID.
* Semana.
* Fecha.
* Modelo.
* Temperatura.
* Ninguna quinta columna.

La semana se identificará únicamente mediante el nombre del archivo.

# Cantidad de observaciones

El generador debe:

* aceptar entre 30 y 60 observaciones;
* usar 48 observaciones por defecto;
* lanzar `ValueError` si la cantidad es menor que 30 o mayor que 60.

# Reproducibilidad

Debe aceptar una semilla aleatoria:

```python
semilla: int = 42
```

Dos ejecuciones con la misma cantidad y la misma semilla deben producir exactamente el mismo DataFrame.

Usa preferentemente:

```python
numpy.random.default_rng(semilla)
```

No dependas del estado aleatorio global de NumPy.

# Variable Sucursal

Categorías válidas:

* `Rosario`
* `Córdoba`

La distribución debe ser aproximadamente equilibrada.

Para una cantidad par, ambas sucursales deben tener la misma cantidad de casos.

Para una cantidad impar, la diferencia no debe superar una observación.

La lista resultante puede mezclarse usando el generador aleatorio.

# Variable Nivel_Fallos

Categorías válidas:

* `Bajo`
* `Medio`
* `Alto`

Debe generarse condicionalmente según la sucursal para crear una asociación lógica intencional.

Probabilidades iniciales:

## Rosario

* Bajo: 0.20
* Medio: 0.35
* Alto: 0.45

## Córdoba

* Bajo: 0.55
* Medio: 0.35
* Alto: 0.10

No asignes manualmente las categorías fila por fila.

No modifiques observaciones individuales para forzar un p-valor específico.

# Variable Antiguedad_Bateria_Meses

Debe cumplir:

* tipo numérico entero;
* valores entre 1 y 48 meses;
* variabilidad suficiente;
* generación aleatoria reproducible;
* no depender directamente de `Nivel_Fallos`.

# Variable Autonomia_Real_Km

Debe presentar una relación lineal negativa, lógica y no perfecta con la antigüedad.

Utiliza como modelo inicial:

```python
autonomia = 45 - 0.52 * antiguedad + error_aleatorio
```

El error debe provenir de una distribución normal.

Usa inicialmente una desviación estándar cercana a:

```python
desviacion_error = 4.0
```

Requisitos:

* tipo numérico continuo;
* redondeo a dos decimales;
* valores razonables entre 15 y 45 km;
* correlación de Pearson negativa;
* correlación no perfecta;
* para 48 casos y semilla 42, Pearson debe quedar aproximadamente entre -0.95 y -0.55;
* no deben ajustarse manualmente filas para conseguir significancia.

Puedes utilizar límites para mantener valores plausibles, pero debes controlar cuántos datos quedan exactamente en 15 o 45 km.

Reporta:

* cantidad de valores exactamente iguales a 15;
* cantidad de valores exactamente iguales a 45;
* porcentaje conjunto de observaciones ubicadas en los límites.

Si la concentración en los límites es excesiva, ajusta la fórmula o dispersión de manera general y documentada, no caso por caso.

# Implementación

Completa `src/simulacion_datos.py`.

Debe incluir como mínimo funcionalidad equivalente a:

```python
def generar_datos(
    cantidad: int = 48,
    semilla: int = 42,
) -> pandas.DataFrame:
    ...
```

```python
def validar_datos_generados(
    datos: pandas.DataFrame,
) -> None:
    ...
```

```python
def guardar_excel(
    datos: pandas.DataFrame,
    ruta_salida: pathlib.Path,
) -> pathlib.Path:
    ...
```

Las funciones deben:

* tener anotaciones de tipos;
* incluir docstrings;
* tener responsabilidades separadas;
* reutilizar las constantes existentes de `src/config.py`;
* evitar duplicar nombres de columnas, categorías y límites ya declarados.

Modifica `src/config.py` únicamente si falta alguna constante necesaria y explica la modificación.

# Interfaz de línea de comandos

Debe ser posible ejecutar:

```powershell
.\.venv\Scripts\python.exe -m src.simulacion_datos --cantidad 48 --semilla 42 --semana 1
```

El comando debe crear:

```text
data/volt_ar_semana_01.xlsx
```

La hoja del Excel debe llamarse:

```text
datos
```

La carpeta de destino debe crearse automáticamente si no existe.

La semana debe validarse como un entero positivo.

# Validaciones obligatorias

El conjunto generado debe comprobar:

* entre 30 y 60 filas;
* exactamente cuatro columnas;
* orden exacto de columnas;
* ausencia de valores nulos;
* sucursales válidas;
* niveles de fallos válidos;
* antigüedad entera entre 1 y 48;
* autonomía numérica entre 15 y 45;
* variabilidad en antigüedad;
* variabilidad en autonomía;
* correlación negativa;
* correlación distinta de -1;
* presencia de ambas sucursales;
* presencia de las tres categorías de fallos para la configuración predeterminada.

No mezcles todavía estas funciones con la futura validación de archivos subidos por el usuario.

# Control cualitativo del archivo predeterminado

Para 48 observaciones y semilla 42:

1. Construye una tabla de contingencia entre `Sucursal` y `Nivel_Fallos`.
2. Calcula las frecuencias esperadas como control técnico.
3. Verifica:

   * ninguna frecuencia esperada menor que 1;
   * al menos el 80 % de las frecuencias esperadas igual o mayor que 5.

Esta comprobación no constituye todavía el módulo definitivo de Chi-cuadrado.

No escribas conclusiones estadísticas en la interfaz.

# Pruebas automatizadas

Crea:

```text
tests/test_simulacion_datos.py
```

Incluye como mínimo pruebas para:

1. Generación de 48 filas.
2. Exactamente cuatro columnas.
3. Orden exacto de columnas.
4. Reproducibilidad con la misma semilla.
5. Resultados distintos con semillas diferentes.
6. Rechazo de menos de 30 observaciones.
7. Rechazo de más de 60 observaciones.
8. Ausencia de valores nulos.
9. Sucursales válidas.
10. Niveles de fallos válidos.
11. Antigüedad entera.
12. Rango de antigüedad.
13. Rango de autonomía.
14. Variabilidad de las variables cuantitativas.
15. Correlación negativa y no perfecta.
16. Balance entre sucursales.
17. Robustez de las frecuencias esperadas del conjunto predeterminado.
18. Escritura correcta del Excel.
19. Lectura del Excel conservando dimensiones y columnas.
20. Nombre de hoja `datos`.
21. Rechazo de una semana no positiva en la interfaz de línea de comandos o función responsable.

No uses pruebas vacías ni `assert True`.

Evita pruebas excesivamente frágiles que dependan de una fila concreta, salvo la prueba de reproducibilidad con la misma semilla.

# Archivo de ejemplo

Genera y conserva:

```text
data/volt_ar_semana_01.xlsx
```

Debe contener:

* 48 filas;
* cuatro columnas;
* hoja `datos`;
* ninguna columna de índice exportada.

# Documentación

Actualiza únicamente lo relacionado con esta fase:

* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/diccionario_datos.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

## README

Agrega instrucciones para generar una semana mediante la terminal.

## decisiones_metodologicas.md

Documenta:

* elección de 48 observaciones;
* balance entre sucursales;
* probabilidades condicionales del nivel de fallos;
* fórmula de autonomía;
* distribución y desviación del error;
* motivo de utilizar error aleatorio;
* relación negativa esperada;
* uso del nombre del archivo para representar la semana;
* criterio de reproducibilidad mediante semilla;
* control de valores en los límites 15 y 45.

## diccionario_datos.md

Confirma:

* nombres exactos;
* orden de columnas;
* tipo de variable;
* escala;
* categorías;
* unidades;
* rangos;
* función en el análisis.

## registro_pruebas.md

Registra las pruebas ejecutadas y sus resultados reales.

## prompts.md

Conserva íntegramente P-00 y P-01.

Agrega P-02 con:

* fecha;
* herramienta: Codex;
* etapa: simulación de datos;
* objetivo;
* prompt completo;
* archivos modificados;
* resultado;
* problemas encontrados;
* correcciones humanas;
* validaciones;
* commit propuesto.

Registra también el incidente de la primera rama P-02:

* la primera rama había sido creada desde un `main` que todavía no contenía P-01;
* se detectó el problema antes de realizar el commit;
* el Pull Request de P-01 fue fusionado;
* la rama fue recreada correctamente desde el `main` actualizado;
* la implementación se realizó finalmente sobre la base correcta.

No elimines ni reemplaces los registros anteriores.

# Archivos que pueden cambiar

Los cambios deberían limitarse principalmente a:

* `src/simulacion_datos.py`
* `tests/test_simulacion_datos.py`
* `data/volt_ar_semana_01.xlsx`
* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/diccionario_datos.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

Modifica `src/config.py` solamente si resulta necesario.

No modifiques:

* `app.py`;
* las páginas de Streamlit;
* `src/analisis_cualitativo.py`;
* `src/analisis_cuantitativo.py`;
* las pruebas no relacionadas con esta fase;

salvo que detectes un error real, en cuyo caso debes detenerte y explicarlo antes de realizar cambios adicionales.

# Validaciones finales

Usa exclusivamente:

```text
.\.venv\Scripts\python.exe
```

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
```

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

```powershell
.\.venv\Scripts\python.exe -m src.simulacion_datos --cantidad 48 --semilla 42 --semana 1
```

Después abre el Excel con Pandas y reporta:

* dimensiones;
* nombres y orden de columnas;
* tipos;
* valores nulos;
* cantidad por sucursal;
* cantidad por nivel de fallos;
* tabla de contingencia;
* frecuencias esperadas;
* porcentaje de esperadas mayores o iguales a 5;
* mínimo y máximo de antigüedad;
* mínimo y máximo de autonomía;
* media y desviación estándar de ambas variables cuantitativas;
* Pearson;
* R²;
* cantidad de autonomías iguales a 15;
* cantidad de autonomías iguales a 45;
* porcentaje conjunto en los límites.

Ejecuta también:

```powershell
git diff --check
```

```powershell
git status --short
```

# Estado de Git esperado

Los archivos de P-01 ya están trackeados y no deben aparecer nuevamente como archivos nuevos.

El estado final debería mostrar únicamente cambios de P-02, similares a:

```text
M README.md
M docs/decisiones_metodologicas.md
M docs/diccionario_datos.md
M docs/prompts.md
M docs/registro_pruebas.md
M src/simulacion_datos.py
?? tests/test_simulacion_datos.py
?? data/volt_ar_semana_01.xlsx
```

Puede haber pequeñas diferencias justificadas, pero no deben aparecer nuevamente como nuevos:

* `AGENTS.md`
* `app.py`
* `pages/`
* todo `src/`
* todo `tests/`

# Informe final

Al terminar, informa:

1. Plan aplicado.
2. Archivos creados.
3. Archivos modificados.
4. Fórmula final utilizada.
5. Probabilidades cualitativas utilizadas.
6. Resultado total de Pytest.
7. Métricas del archivo generado.
8. Tabla de contingencia.
9. Frecuencias esperadas.
10. Pearson y R².
11. Cantidad de valores en los límites.
12. Advertencias o decisiones metodológicas.
13. Resultado de `git diff --check`.
14. Estado final de Git.
15. Mensaje de commit propuesto.

No realices commit, push, merge ni Pull Request.

Detente al finalizar y espera mi revisión.
````

### Archivos modificados

- `README.md`
- `docs/decisiones_metodologicas.md`
- `docs/diccionario_datos.md`
- `docs/prompts.md`
- `docs/registro_pruebas.md`
- `src/config.py`
- `src/simulacion_datos.py`
- `tests/test_simulacion_datos.py`
- `data/volt_ar_semana_01.xlsx`

### Resultado

Se implementó el generador reproducible, se generó el archivo Excel inicial con
48 observaciones, cuatro columnas estadísticas y hoja `datos`, y se agregaron
pruebas automatizadas para validar la fase.

### Problemas encontrados

- La primera rama P-02 había sido creada desde un `main` que todavía no contenía
  P-01. Se detectó el problema antes de realizar el commit.
- El Pull Request de P-01 fue fusionado y la rama fue recreada correctamente
  desde el `main` actualizado.
- La implementación final de P-02 se realizó sobre la base correcta, con los
  archivos de P-01 ya trackeados.
- Fue necesario ampliar `src/config.py` con constantes de simulación para evitar
  duplicar nombres, rangos, probabilidades y valores predeterminados.

### Correcciones humanas

La rama fue recreada desde `main` actualizado antes de reaplicar P-02. No se
registraron correcciones manuales sobre los resultados generados.

### Validaciones

- `.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests`
- `.\.venv\Scripts\python.exe -m pytest -q`
- `.\.venv\Scripts\python.exe -m src.simulacion_datos --cantidad 48 --semilla 42 --semana 1`
- Revisión del Excel con Pandas.
- `git diff --check`
- `git status --short`

### Commit propuesto

```text
feat: agregar simulacion reproducible de datos semanales
```

## P-03 — Carga y validación

### Fecha

2026-06-21.

### Herramienta

Codex.

### Etapa

Carga y validación de la actualización semanal.

### Objetivo

Implementar el mecanismo de carga dinámica de archivos semanales, validar su
estructura y mantener el conjunto activo para las páginas del dashboard sin
implementar todavía análisis estadísticos.

### Prompt completo

````text
Trabaja exclusivamente en la rama `feat/carga-validacion`.

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Confirma la rama activa.
3. Ejecuta `git status --short --branch`.
4. Inspecciona:

   * `src/config.py`
   * `src/carga_datos.py`
   * `src/validacion_datos.py`
   * `app.py`
   * las páginas de Streamlit;
   * los tests;
   * la documentación.
5. Presenta un plan breve.
6. No realices commit, push, merge ni Pull Request.

# Fase P-03: carga y validación de la actualización semanal

## Objetivo

Implementar el mecanismo de carga dinámica de archivos semanales y validar su estructura antes de utilizarlos en el dashboard.

La aplicación debe aceptar una nueva matriz de datos, validarla y mantenerla como conjunto activo para las dos páginas.

No implementes todavía:

* Tabla de contingencia definitiva.
* Prueba Chi-cuadrado.
* Correlación.
* Regresión.
* Gráficos estadísticos.
* Intervalos.
* Predicciones.
* Conclusiones inferenciales.

## Formatos admitidos

Aceptar:

* `.xlsx`
* `.csv`

Para Excel, utilizar preferentemente la hoja `datos`.

Si el archivo Excel no contiene una hoja llamada `datos`, devolver un mensaje claro indicando las hojas encontradas. No seleccionar silenciosamente otra hoja.

Para CSV:

* detectar correctamente UTF-8;
* admitir separador coma o punto y coma cuando sea posible;
* informar un error claro cuando no pueda interpretarse.

## Estructura requerida

Los datos deben contener exactamente estas cuatro columnas:

1. `Sucursal`
2. `Nivel_Fallos`
3. `Antiguedad_Bateria_Meses`
4. `Autonomia_Real_Km`

Si están en otro orden pero contienen exactamente el mismo conjunto, reordenarlas al orden canónico.

Rechazar:

* columnas faltantes;
* columnas adicionales;
* columnas `Unnamed`;
* archivos vacíos;
* menos de 30 filas;
* más de 60 filas.

## Validaciones de contenido

### Sucursal

Valores admitidos:

* Rosario
* Córdoba

Eliminar espacios al inicio y al final.

Normalizar diferencias de mayúsculas y minúsculas cuando no exista ambigüedad.

No inventar ni corregir automáticamente nombres desconocidos.

### Nivel_Fallos

Valores admitidos:

* Bajo
* Medio
* Alto

Eliminar espacios y normalizar mayúsculas y minúsculas.

### Antiguedad_Bateria_Meses

* Debe ser convertible a entero.
* Valores entre 1 y 48.
* No aceptar decimales no enteros.
* No aceptar infinitos.

### Autonomia_Real_Km

* Debe ser convertible a número.
* Valores entre 15 y 45.
* No aceptar infinitos.

### Controles generales

* No permitir valores nulos.
* No exigir que las filas sean únicas, porque sin un identificador dos monopatines pueden tener valores coincidentes.
* No aplicar todavía pruebas estadísticas.
* No modificar valores numéricos válidos.
* Los mensajes de error deben indicar columna, problema y, cuando resulte posible, filas afectadas.

## Arquitectura

Completa principalmente:

* `src/carga_datos.py`
* `src/validacion_datos.py`

Implementa funciones pequeñas, tipadas y documentadas, equivalentes a:

```python
def leer_archivo_excel(origen: str | Path | BinaryIO) -> pandas.DataFrame:
    ...
```

```python
def leer_archivo_csv(origen: str | Path | BinaryIO) -> pandas.DataFrame:
    ...
```

```python
def cargar_archivo_semanal(
    origen: str | Path | BinaryIO,
    nombre_archivo: str,
) -> pandas.DataFrame:
    ...
```

```python
def validar_y_normalizar_datos(
    datos: pandas.DataFrame,
) -> pandas.DataFrame:
    ...
```

La función de validación debe devolver una copia normalizada y no modificar silenciosamente el DataFrame original.

Crea excepciones específicas o una estructura clara para distinguir:

* Error de formato.
* Error de columnas.
* Error de cantidad de filas.
* Error de categorías.
* Error de valores numéricos.
* Error de valores faltantes.

Evita duplicar constantes ya existentes en `src/config.py`.

## Integración Streamlit

Implementa un componente reutilizable de carga, manteniendo separada la interfaz de la lógica.

Puedes crear un módulo como:

`src/interfaz_carga.py`

El componente debe:

1. Mostrar un `file_uploader` en la barra lateral.
2. Aceptar Excel o CSV.
3. Utilizar `data/volt_ar_semana_01.xlsx` como datos predeterminados cuando todavía no se haya cargado otro archivo.
4. Almacenar el DataFrame validado en:

```python
st.session_state["datos_activos"]
```

5. Almacenar el nombre del archivo en:

```python
st.session_state["nombre_archivo_activo"]
```

6. No sustituir los datos activos cuando un nuevo archivo sea inválido.
7. Mostrar confirmación cuando la carga sea válida.
8. Mostrar errores comprensibles cuando sea inválida.
9. Mostrar:

   * nombre del archivo activo;
   * cantidad de observaciones;
   * cuatro variables detectadas;
   * una vista previa de hasta diez filas.
10. Permitir volver al archivo predeterminado mediante un botón.

Integra el componente en `app.py` y deja los datos disponibles para las dos páginas.

Si Streamlit multipágina no comparte automáticamente la inicialización al acceder directamente a una página, implementa una función reutilizable que garantice la carga del conjunto predeterminado sin duplicar código.

## Comportamiento dinámico

Cuando el usuario carga un archivo válido:

* deben reemplazarse los datos activos;
* la vista previa debe actualizarse;
* cualquier futura página que consulte `datos_activos` debe recibir el nuevo DataFrame.

Todavía no implementes los cálculos estadísticos que utilizarán esos datos.

## Pruebas

Crea pruebas para:

1. Lectura de un Excel válido.
2. Lectura de un CSV válido con coma.
3. Lectura de un CSV válido con punto y coma.
4. Conservación de las cuatro columnas.
5. Reordenamiento al orden canónico.
6. Archivo Excel sin hoja `datos`.
7. Extensión no admitida.
8. Archivo vacío.
9. Columna faltante.
10. Columna adicional.
11. Columna `Unnamed`.
12. Menos de 30 filas.
13. Más de 60 filas.
14. Valores nulos.
15. Sucursal inválida.
16. Nivel de fallos inválido.
17. Normalización de mayúsculas y espacios.
18. Antigüedad decimal no entera.
19. Antigüedad fuera de rango.
20. Autonomía fuera de rango.
21. Valores infinitos.
22. El DataFrame original no debe modificarse.
23. Un archivo inválido no debe considerarse válido.

No realices tests frágiles sobre widgets visuales. Prueba la lógica desacoplada mediante `BytesIO`, archivos temporales y DataFrames.

## Documentación

Actualiza:

* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

En `docs/prompts.md`, conserva P-00, P-01 y P-02 y agrega P-03 con el prompt completo.

Documenta:

* formatos admitidos;
* reglas de validación;
* comportamiento del archivo predeterminado;
* utilización de `session_state`;
* tratamiento de errores;
* decisión de no eliminar duplicados;
* actualización automática al cargar otra semana.

## Validaciones finales

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
```

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless=true --server.address=127.0.0.1 --server.port=8765 --server.runOnSave=false
```

Verifica que Streamlit inicie y luego detén el proceso.

Ejecuta también:

```powershell
git diff --check
git status --short
```

## Revisión manual solicitada

Informa cómo probar manualmente:

1. El Excel predeterminado.
2. Un Excel válido alternativo.
3. Un CSV válido.
4. Un archivo sin una columna.
5. Un archivo con menos de 30 filas.
6. Un archivo con categorías inválidas.
7. El botón para volver a los datos predeterminados.

## Restricciones

* No implementes análisis estadísticos.
* No agregues datos nuevos aparte del archivo predeterminado existente.
* No realices commit.
* No hagas push.
* No cambies de rama.
* No crees Pull Request.
* No elimines documentación anterior.

## Informe final

Reporta:

1. Plan aplicado.
2. Archivos creados.
3. Archivos modificados.
4. Funciones implementadas.
5. Reglas de normalización.
6. Total de pruebas aprobadas.
7. Resultado del inicio de Streamlit.
8. Casos manuales pendientes de probar.
9. Advertencias.
10. Estado de Git.
11. Mensaje de commit propuesto.

Detente y espera mi revisión.
````

### Archivos modificados

- `README.md`
- `app.py`
- `docs/decisiones_metodologicas.md`
- `docs/prompts.md`
- `docs/registro_pruebas.md`
- `src/carga_datos.py`
- `src/interfaz_carga.py`
- `src/validacion_datos.py`
- `tests/test_carga_validacion.py`

### Resultado

Se implementó la lectura de Excel y CSV, la validación y normalización de la
matriz semanal, las excepciones específicas de validación, el componente
reutilizable de carga en Streamlit y las pruebas automatizadas de P-03.

### Problemas encontrados

- El primer ajuste de CSV no capturaba `_csv.Error` para archivos vacíos; se
  corrigió para devolver `ErrorFormatoArchivo`.
- Una prueba intentaba escribir `10.5` en una columna `int64` antes de llegar al
  validador; se ajustó la prueba para representar el caso de entrada decimal.
- Se modificó `app.py` porque la consigna pedía integrar allí el componente de
  carga, aunque los cambios se mantuvieron fuera de las páginas.

### Correcciones humanas

No se registraron correcciones humanas sobre la implementación final.

### Validaciones

- `.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests`
- `.\.venv\Scripts\python.exe -m pytest -q`
- Inicio temporal de Streamlit en `http://127.0.0.1:8765`
- `git diff --check`
- `git status --short`

### Commit propuesto

```text
feat: agregar carga y validacion de datos semanales
```

## P-04 — Módulo cualitativo gerencial

### Fecha

2026-06-21.

### Herramienta

Codex.

### Etapa

Módulo cualitativo descriptivo y muestral.

### Objetivo

Implementar el módulo cualitativo de la Página 1 para perfil gerencial, usando
`Sucursal` como variable de filas y `Nivel_Fallos` como variable de columnas,
sin formular conclusiones inferenciales sobre la población.

### Prompt completo

````text
Trabaja exclusivamente en la rama `feat/modulo-cualitativo-gerencial`.

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Confirma la rama activa.
3. Verifica que el árbol de trabajo esté limpio.
4. Inspecciona:

   * `src/analisis_cualitativo.py`
   * `src/interfaz_carga.py`
   * `src/config.py`
   * `pages/1_Perfil_Gerencial.py`
   * los tests existentes;
   * la documentación.
5. Presenta un plan breve.
6. No realices commit, push, merge ni Pull Request.

# Fase P-04: módulo cualitativo descriptivo y muestral

## Objetivo

Implementar el módulo cualitativo de la Página 1 del dashboard para un perfil gerencial.

El análisis utilizará:

* Variable de filas: `Sucursal`.
* Variable de columnas: `Nivel_Fallos`.

La página tendrá enfoque descriptivo y muestral.

No debe incluir conclusiones inferenciales sobre la población.

## Fuente de datos

La página debe utilizar el DataFrame activo almacenado en:

```python
st.session_state["datos_activos"]
```

Debe garantizar que existan datos activos incluso cuando el usuario acceda directamente a la página.

Reutiliza las funciones de `src/interfaz_carga.py`.

No dupliques la lógica de lectura ni validación.

Debe mostrarse:

* nombre del archivo activo;
* cantidad de observaciones;
* posibilidad de cargar otro archivo semanal desde la barra lateral;
* posibilidad de volver al archivo predeterminado.

## Lógica estadística

Completa `src/analisis_cualitativo.py` con funciones tipadas, documentadas y separadas de Streamlit.

Implementa funcionalidad equivalente a:

```python
def construir_tabla_contingencia(
    datos: pandas.DataFrame,
) -> pandas.DataFrame:
    ...
```

```python
def agregar_marginales(
    tabla: pandas.DataFrame,
) -> pandas.DataFrame:
    ...
```

```python
def calcular_chi_cuadrado_muestral(
    tabla_observada: pandas.DataFrame,
) -> ResultadoChiCuadrado:
    ...
```

Puedes utilizar una `dataclass` para devolver:

* tabla observada;
* frecuencias esperadas;
* estadístico Chi-cuadrado;
* grados de libertad;
* p-valor;
* frecuencia esperada mínima;
* porcentaje de frecuencias esperadas mayores o iguales a 5.

Usa:

```python
scipy.stats.chi2_contingency
```

sin corrección de Yates para la tabla 2 × 3:

```python
correction=False
```

No implementes manualmente una fórmula diferente a la de SciPy salvo para una verificación de pruebas.

## Orden de categorías

Mantén el orden:

### Sucursal

1. Rosario
2. Córdoba

### Nivel de fallos

1. Bajo
2. Medio
3. Alto

La tabla visual debe incluir los totales marginales de filas y columnas.

Los marginales no deben enviarse a `chi2_contingency`.

## Categorías no observadas

La lógica debe manejar archivos semanales donde alguna categoría válida no aparezca.

Para calcular Chi-cuadrado:

* elimina únicamente filas o columnas con total marginal igual a cero;
* exige al menos dos categorías observadas en cada variable;
* si no se puede calcular la prueba, muestra una advertencia comprensible en la interfaz;
* no dejes que Streamlit termine con una excepción técnica.

No inventes observaciones para completar categorías ausentes.

## Página gerencial

Implementa en `pages/1_Perfil_Gerencial.py` solamente el módulo cualitativo.

Debe contener:

1. Título de la página.
2. Identificación del archivo activo.
3. Explicación breve del enfoque muestral.
4. Sección “Análisis cualitativo”.
5. Tabla de contingencia observada con marginales.
6. Gráfico de barras agrupadas.
7. Gráfico de barras apiladas al 100 %.
8. Tarjetas o métricas para:

   * Chi-cuadrado muestral;
   * grados de libertad;
   * p-valor;
   * nivel de significancia seleccionado.
9. Deslizador para el nivel de significancia.

## Nivel de significancia

Crear un deslizador con:

* mínimo: 0.01;
* máximo: 0.10;
* valor inicial: 0.05;
* paso: 0.01.

El p-valor debe calcularse únicamente desde los datos y no debe cambiar cuando cambia el nivel de significancia.

Puede mostrarse una comparación neutral:

```text
p-valor < α
```

o:

```text
p-valor ≥ α
```

Pero en esta página no debe mostrarse:

* “se rechaza H₀”;
* “no se rechaza H₀”;
* “existe asociación poblacional”;
* “las variables son independientes”;
* ninguna conclusión sobre toda la población.

Agrega una aclaración visible indicando que la conclusión inferencial se presentará en la Página 2.

## Gráficos

Utiliza Plotly.

### Barras agrupadas

* Eje X: Sucursal.
* Series: Nivel_Fallos.
* Eje Y: frecuencia observada.
* Tooltip con categoría y frecuencia.
* Título y ejes en español.

### Barras apiladas al 100 %

* Mostrar la composición porcentual del nivel de fallos dentro de cada sucursal.
* Cada sucursal debe sumar 100 %.
* Tooltip con frecuencia y porcentaje.
* No utilizar los marginales para construir el gráfico.

Los gráficos deben actualizarse automáticamente cuando cambien los datos activos.

## Presentación

No recargues manualmente los datos desde el Excel dentro de la página.

No incluyas todavía:

* frecuencias esperadas visibles;
* frecuencias diferenciales relativas;
* evaluación formal de robustez;
* hipótesis estadísticas completas;
* conclusión inferencial.

Esos elementos corresponden a la Página 2.

Puedes mostrar el estadístico y p-valor porque la consigna los exige en la Página 1, pero sin decisión inferencial.

## Pruebas automatizadas

Agrega pruebas para:

1. Construcción correcta de la tabla de contingencia.
2. Orden de filas y columnas.
3. Totales marginales correctos.
4. Los marginales no alteran la tabla usada en la prueba.
5. Chi-cuadrado coincidente con SciPy.
6. Grados de libertad correctos.
7. P-valor entre 0 y 1.
8. Frecuencias esperadas con la misma dimensión que la tabla efectiva.
9. Suma de frecuencias esperadas igual al total observado.
10. Estadístico no negativo.
11. El p-valor no depende de α.
12. Manejo de una categoría válida ausente.
13. Error comprensible cuando solo existe una categoría observada en una variable.
14. Porcentajes por sucursal suman aproximadamente 100 %.
15. Los cálculos funcionan con el Excel predeterminado.
16. La página no contiene frases de conclusión inferencial prohibidas.

No crees tests frágiles basados en elementos visuales internos de Streamlit.

Prueba las transformaciones de datos que alimentan los gráficos mediante funciones puras.

## Documentación

Actualiza:

* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

Conserva P-00, P-01, P-02 y P-03.

Agrega P-04 con:

* prompt completo;
* archivos modificados;
* decisiones estadísticas;
* validaciones;
* problemas;
* resultado;
* commit propuesto.

Documenta explícitamente:

* diferencia entre descripción muestral e inferencia poblacional;
* por qué la Página 1 no contiene una conclusión;
* que el p-valor no cambia con α;
* que los marginales se muestran, pero no forman parte del cálculo de Chi-cuadrado;
* que la prueba utiliza `correction=False`.

## Validaciones finales

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
```

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Inicia Streamlit temporalmente y verifica que no haya errores:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless=true --server.address=127.0.0.1 --server.port=8765 --server.runOnSave=false
```

Detén el proceso después de comprobarlo.

Ejecuta también:

```powershell
git diff --check
git status --short
```

## Informe final

Reporta:

1. Plan aplicado.
2. Archivos creados.
3. Archivos modificados.
4. Funciones estadísticas implementadas.
5. Estadístico Chi-cuadrado del Excel predeterminado.
6. Grados de libertad.
7. P-valor.
8. Tabla de contingencia.
9. Resultado de los porcentajes del gráfico al 100 %.
10. Total de pruebas aprobadas.
11. Resultado de Streamlit.
12. Confirmación de que no existen conclusiones inferenciales en Página 1.
13. Estado de Git.
14. Mensaje de commit propuesto.

No realices commit, push, merge ni Pull Request.

Detente y espera mi revisión.
````

### Archivos modificados

- `README.md`
- `docs/decisiones_metodologicas.md`
- `docs/prompts.md`
- `docs/registro_pruebas.md`
- `pages/1_Perfil_Gerencial.py`
- `src/analisis_cualitativo.py`
- `tests/test_analisis_cualitativo.py`

### Decisiones estadísticas

- La Página 1 se mantiene descriptiva y muestral.
- Se usa `scipy.stats.chi2_contingency` con `correction=False`.
- Los marginales se muestran en la tabla visual, pero no se envían al cálculo.
- Las categorías válidas ausentes se conservan con cero en la tabla descriptiva
  y se eliminan solo de la tabla efectiva cuando su total marginal es cero.
- El p-valor se calcula con los datos y no cambia con el nivel de significancia.

### Resultado

Se implementó el módulo cualitativo gerencial con tabla de contingencia,
marginales, gráficos Plotly, métricas muestrales y comparación neutral con α.

### Problemas encontrados

No se encontraron bloqueos. La página evita frases de conclusión inferencial
prohibidas y muestra una aclaración de que la conclusión formal corresponde a la
Página 2.

### Corrección posterior a la revisión manual

- Se observó que la interfaz mostraba solamente las filas visibles de la vista
  previa y podía dar la impresión de que el análisis utilizaba solo nueve o diez
  registros.
- Se verificó que los cálculos estadísticos sí utilizaban las 48 observaciones
  completas.
- Se modificó `src/interfaz_carga.py` para mostrar el texto dinámico
  `Vista previa: 10 de 48 registros`.
- Se agregó un expander `Ver base completa (48 registros)`.
- `datos.head()` se utiliza únicamente para la vista previa.
- `st.session_state["datos_activos"]` conserva el DataFrame completo.
- Las pruebas automatizadas continuaron aprobándose: 71 pruebas.
- La aplicación inició correctamente en Streamlit.
- La revisión visual confirmó que la tabla de contingencia continúa sumando 48
  observaciones.

### Validaciones

- `.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests`
- `.\.venv\Scripts\python.exe -m pytest -q`
- Inicio temporal de Streamlit en `http://127.0.0.1:8765`
- `git diff --check`
- `git status --short`

### Commit propuesto

```text
feat: agregar modulo cualitativo gerencial
```

## P-05 — Módulo cuantitativo gerencial

### Fecha

2026-06-21.

### Herramienta

Codex.

### Etapa

Módulo cuantitativo descriptivo y muestral.

### Objetivo

Completar el módulo cuantitativo de la Página 1 para el perfil gerencial,
usando `Antiguedad_Bateria_Meses` como variable independiente y
`Autonomia_Real_Km` como variable dependiente, sin incorporar todavía
conclusiones inferenciales ni diagnóstico visible de residuos.

### Prompt completo

````text
Trabaja exclusivamente en la rama `feat/modulo-cuantitativo-gerencial`.

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Confirma la rama activa.
3. Verifica que el árbol de trabajo esté limpio.
4. Inspecciona:

   * `src/analisis_cuantitativo.py`
   * `src/config.py`
   * `src/interfaz_carga.py`
   * `pages/1_Perfil_Gerencial.py`
   * los tests existentes;
   * la documentación.
5. Confirma que el módulo cualitativo P-04 esté presente.
6. Presenta un plan breve.
7. No realices commit, push, merge ni Pull Request.

# Fase P-05: módulo cuantitativo descriptivo y muestral

## Objetivo

Completar el módulo cuantitativo de la Página 1 para el perfil gerencial.

Las variables serán:

* Variable independiente X: `Antiguedad_Bateria_Meses`.
* Variable dependiente Y: `Autonomia_Real_Km`.

La página debe presentar la relación observada en la muestra semanal mediante:

* gráfico de dispersión;
* recta de regresión muestral;
* ecuación estimada;
* coeficiente de correlación de Pearson;
* coeficiente de determinación;
* interpretación descriptiva dinámica.

No debe incluir todavía:

* prueba de hipótesis;
* estadístico t;
* grados de libertad inferenciales;
* intervalos de confianza;
* intervalos de predicción;
* conclusión poblacional;
* diagnóstico de residuos visible.

Esos elementos corresponden a la Página 2.

# Fuente de datos

Utiliza:

```python
st.session_state["datos_activos"]
```

Reutiliza el mecanismo de P-03.

No vuelvas a leer directamente el Excel desde esta página.

Los resultados deben actualizarse automáticamente cuando cambie el archivo activo.

# Lógica cuantitativa

Completa `src/analisis_cuantitativo.py` con funciones puras, tipadas y documentadas.

Implementa una estructura equivalente a:

```python
@dataclass(frozen=True)
class ResultadoRegresionMuestral:
    cantidad: int
    intercepto: float
    pendiente: float
    coeficiente_pearson: float
    coeficiente_determinacion: float
    valores_ajustados: pandas.Series
    residuos: pandas.Series
```

Implementa funcionalidad equivalente a:

```python
def ajustar_regresion_lineal(
    datos: pandas.DataFrame,
    columna_x: str = "Antiguedad_Bateria_Meses",
    columna_y: str = "Autonomia_Real_Km",
) -> ResultadoRegresionMuestral:
    ...
```

```python
def interpretar_correlacion_muestral(
    coeficiente: float,
) -> str:
    ...
```

```python
def interpretar_r_cuadrado_muestral(
    coeficiente_determinacion: float,
) -> str:
    ...
```

```python
def construir_datos_recta_regresion(
    datos: pandas.DataFrame,
    resultado: ResultadoRegresionMuestral,
) -> pandas.DataFrame:
    ...
```

Utiliza preferentemente `statsmodels` para ajustar el modelo, de manera que el resultado pueda reutilizarse posteriormente en la Página 2.

Para Pearson, utiliza `scipy.stats.pearsonr` o una implementación equivalente validada.

No dependas de una función automática de Plotly que calcule un modelo diferente al utilizado en las tarjetas.

La recta mostrada debe usar exactamente el mismo intercepto y pendiente que el resultado estadístico.

# Controles previos

Antes del ajuste verifica:

* al menos tres observaciones;
* valores numéricos y finitos;
* variabilidad en X;
* variabilidad en Y;
* ausencia de valores nulos.

Si X o Y son constantes, devuelve un error comprensible para la interfaz.

No permitas que Streamlit muestre una traza técnica completa.

# Coeficiente de Pearson

Debe cumplir:

[
-1\leq r\leq1
]

La interpretación debe ser descriptiva y referirse exclusivamente a la muestra.

Utiliza una clasificación heurística documentada basada en (|r|):

* menor que 0,20: muy débil;
* desde 0,20 y menor que 0,40: débil;
* desde 0,40 y menor que 0,60: moderada;
* desde 0,60 y menor que 0,80: fuerte;
* desde 0,80 hasta 1: muy fuerte.

También debe indicarse el sentido:

* positivo;
* negativo;
* sin dirección lineal apreciable cuando sea prácticamente cero.

Ejemplo válido:

> En la muestra semanal se observa una relación lineal negativa muy fuerte.

No utilizar expresiones como:

* “X causa Y”.
* “La relación se cumple en toda la población”.
* “Existe evidencia estadísticamente significativa”.

La clasificación es una ayuda descriptiva y debe documentarse como criterio convencional, no como una ley universal.

# Coeficiente de determinación

En regresión lineal simple con intercepto debe coincidir aproximadamente con:

[
R^2=r^2
]

La interpretación dinámica debe seguir una forma como:

> En la muestra, el modelo lineal con la antigüedad explica aproximadamente el 81,09 % de la variabilidad observada en la autonomía.

Evita afirmar causalidad.

Verifica que:

[
0\leq R^2\leq1
]

# Ecuación muestral

Mostrar:

[
\widehat{Autonomia}=b_0+b_1\cdot Antiguedad
]

Formatea correctamente el signo de la pendiente.

Por ejemplo:

```text
Autonomía estimada = 44,82 - 0,54 × Antigüedad
```

La ecuación debe indicar:

* autonomía en kilómetros;
* antigüedad en meses.

# Página gerencial

Conserva íntegro el módulo cualitativo P-04.

Agrega debajo una sección:

```text
Análisis cuantitativo
```

Debe incluir:

1. Explicación breve del enfoque muestral.
2. Gráfico de dispersión interactivo.
3. Recta de regresión superpuesta.
4. Tarjeta KPI de Pearson.
5. Tarjeta KPI de R².
6. Tarjeta o bloque con la ecuación de regresión.
7. Interpretación dinámica de Pearson.
8. Interpretación dinámica de R².
9. Aclaración de que la inferencia poblacional se realiza en la Página 2.

# Gráfico de dispersión

Utiliza Plotly.

Requisitos:

* Eje X: `Antiguedad_Bateria_Meses`.
* Título del eje: “Antigüedad de la batería (meses)”.
* Eje Y: `Autonomia_Real_Km`.
* Título del eje: “Autonomía real (km)”.
* Puntos correspondientes a cada monopatín.
* Recta de regresión muestral.
* Tooltip con:

  * antigüedad;
  * autonomía;
  * sucursal;
  * nivel de fallos.
* Leyenda que diferencie observaciones y recta.
* La línea debe construirse con valores X ordenados.
* No conectar los puntos observados entre sí.
* Los resultados deben cambiar cuando se cargue otro archivo válido.

Puedes diferenciar visualmente por sucursal, siempre que la recta represente el modelo global de todas las observaciones.

No agregues una regresión separada por sucursal.

# Precisión visual

Presenta:

* Pearson con cuatro decimales.
* R² con cuatro decimales y, en la interpretación, como porcentaje con dos decimales.
* Pendiente e intercepto con una precisión razonable, por ejemplo cuatro decimales en la tarjeta y dos en la ecuación visible.

No redondees los valores internamente antes de realizar cálculos.

# Pruebas automatizadas

Agrega o amplía pruebas para:

1. Ajuste correcto con datos lineales conocidos.
2. Pendiente positiva conocida.
3. Pendiente negativa conocida.
4. Intercepto correcto.
5. Pearson dentro de [-1, 1].
6. R² dentro de [0, 1].
7. Correspondencia aproximada entre R² y (r^2).
8. Valores ajustados con la misma cantidad de observaciones.
9. Residuos con la misma cantidad de observaciones.
10. Suma o media de residuos aproximadamente cero cuando existe intercepto.
11. Construcción de la recta con X ordenado.
12. La recta utiliza el mismo intercepto y pendiente del resultado.
13. Error con X constante.
14. Error con Y constante.
15. Error con valores no finitos.
16. Interpretación correcta del sentido negativo.
17. Interpretación correcta del sentido positivo.
18. Clasificación en cada rango de intensidad.
19. Interpretación de R² expresada como porcentaje muestral.
20. Resultados del Excel predeterminado:

    * Pearson aproximadamente -0,900523;
    * R² aproximadamente 0,810942.
21. La página no contiene frases inferenciales prohibidas.
22. El módulo cualitativo P-04 continúa presente.
23. Los cálculos no dependen del redondeo visual.

No pruebes detalles internos frágiles de widgets de Streamlit.

# Documentación

Actualiza:

* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

Conserva íntegramente P-00 a P-04.

Agrega P-05 con:

* prompt completo;
* archivos modificados;
* funciones implementadas;
* decisiones estadísticas;
* resultados;
* validaciones;
* problemas encontrados;
* correcciones humanas;
* commit propuesto.

Documenta:

* elección de X e Y;
* significado de pendiente e intercepto;
* significado descriptivo de Pearson;
* criterio heurístico de intensidad;
* significado de R²;
* diferencia entre asociación y causalidad;
* diferencia entre análisis muestral e inferencia poblacional;
* que el mismo modelo alimenta la recta y los KPI;
* que los residuos se calculan internamente para reutilización posterior, pero todavía no se muestran.

# Archivos esperados

Los cambios deberían limitarse principalmente a:

* `pages/1_Perfil_Gerencial.py`
* `src/analisis_cuantitativo.py`
* `tests/test_analisis_cuantitativo.py`
* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

No modifiques el generador, la carga, la validación ni el módulo cualitativo salvo que detectes un error real.

# Validaciones finales

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
```

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Inicia Streamlit temporalmente:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless=true --server.address=127.0.0.1 --server.port=8765 --server.runOnSave=false
```

Detén el proceso después de verificar el inicio.

Ejecuta:

```powershell
git diff --check
git status --short
```

Para el Excel predeterminado reporta:

* cantidad de observaciones;
* intercepto;
* pendiente;
* Pearson;
* R²;
* ecuación visible;
* media de residuos;
* interpretación dinámica de Pearson;
* interpretación dinámica de R².

# Informe final

Informa:

1. Plan aplicado.
2. Archivos creados.
3. Archivos modificados.
4. Funciones implementadas.
5. Resultado de la regresión predeterminada.
6. Pearson y R².
7. Interpretaciones generadas.
8. Total de pruebas aprobadas.
9. Resultado de Streamlit.
10. Confirmación de que P-04 sigue funcionando.
11. Confirmación de que no existen conclusiones inferenciales.
12. Resultado de `git diff --check`.
13. Estado de Git.
14. Mensaje de commit propuesto.

No realices commit, push, merge ni Pull Request.

Detente y espera mi revisión.
````

### Archivos modificados

- `README.md`
- `docs/decisiones_metodologicas.md`
- `docs/prompts.md`
- `docs/registro_pruebas.md`
- `pages/1_Perfil_Gerencial.py`
- `src/analisis_cuantitativo.py`
- `tests/test_analisis_cuantitativo.py`

### Funciones implementadas

- `ajustar_regresion_lineal`
- `interpretar_correlacion_muestral`
- `interpretar_r_cuadrado_muestral`
- `construir_datos_recta_regresion`
- `formatear_ecuacion_regresion`

### Decisiones estadísticas

- La Página 1 mantiene un enfoque descriptivo y muestral.
- Se utiliza `statsmodels` para ajustar una regresión lineal simple con
  intercepto.
- Pearson se calcula con `scipy.stats.pearsonr`.
- La recta visible se construye con el mismo intercepto y pendiente que alimentan
  los indicadores.
- Los residuos se calculan internamente, pero no se muestran en la interfaz
  gerencial.
- La interpretación de Pearson usa una clasificación heurística documentada y no
  se presenta como regla universal.
- No se incorporan hipótesis, intervalos, predicciones ni conclusiones
  poblacionales en la Página 1.

### Resultado

Se implementó el módulo cuantitativo gerencial con gráfico de dispersión,
recta de regresión muestral, ecuación visible, KPI de Pearson y R² e
interpretaciones descriptivas dinámicas.

Para el archivo predeterminado se obtuvo:

- cantidad de observaciones: 48;
- intercepto: 45.166071483068;
- pendiente: -0.552768328535;
- Pearson: -0.900523263956;
- R²: 0.810942148925;
- ecuación visible:
  `Autonomía estimada (km) = 45.17 - 0.55 × Antigüedad (meses)`;
- media de residuos: aproximadamente 0.

### Problemas encontrados

- El sandbox de Windows volvió a fallar al iniciar procesos con
  `CreateProcessAsUserW failed: 1920`; las validaciones se ejecutaron con
  permisos escalados cuando fue necesario.
- La revisión automática de permisos tuvo respuestas intermitentes al lanzar
  varios comandos en paralelo; se continuó con comandos individuales.
- Una prueba nueva intentaba insertar texto en una columna `float64` antes de
  llegar al validador. Se ajustó la prueba para convertir la columna a tipo
  `object` y representar correctamente un archivo con valor no numérico.

### Correcciones humanas

No se registraron correcciones humanas durante la implementación de P-05.

### Validaciones

- `.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests`
- `.\.venv\Scripts\python.exe -m pytest -q`
- Inicio temporal de Streamlit en `http://127.0.0.1:8765`
- `git diff --check`
- `git status --short`

### Commit propuesto

```text
feat: agregar modulo cuantitativo gerencial
```

## P-06 — Inferencia cualitativa

### Fecha

2026-06-21.

### Herramienta

Codex.

### Etapa

Inferencia cualitativa y prueba de independencia.

### Objetivo

Implementar en la Página 2 el análisis inferencial de `Sucursal` y
`Nivel_Fallos` mediante una prueba Chi-cuadrado de independencia, incluyendo
hipótesis, decisión, conclusión contextual, frecuencias esperadas, diferencias
relativas, aportes por celda y evaluación de robustez.

### Prompt completo

````text
Trabaja exclusivamente en la rama `feat/inferencia-cualitativa`.

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Confirma la rama activa.
3. Verifica que el árbol de trabajo esté limpio.
4. Inspecciona:

   * `src/analisis_cualitativo.py`
   * `src/interfaz_carga.py`
   * `pages/2_Perfil_Analista.py`
   * `pages/1_Perfil_Gerencial.py`
   * los tests existentes;
   * la documentación.
5. Confirma que P-04 y P-05 estén presentes.
6. Presenta un plan breve.
7. No realices commit, push, merge ni Pull Request.

# Fase P-06: inferencia cualitativa y prueba de independencia

## Objetivo

Implementar en la Página 2 el análisis inferencial de las variables:

* `Sucursal`
* `Nivel_Fallos`

Se aplicará una prueba Chi-cuadrado de independencia para evaluar si la relación observada en la muestra proporciona evidencia de asociación a nivel poblacional.

Esta fase debe incluir:

* hipótesis;
* frecuencias observadas;
* frecuencias esperadas;
* diferencias relativas;
* estadístico Chi-cuadrado;
* grados de libertad;
* p-valor;
* nivel de significancia;
* decisión;
* conclusión contextual;
* evaluación de supuestos;
* evaluación de robustez.

No implementes todavía la inferencia cuantitativa, los intervalos, la predicción ni los gráficos de residuos.

# Fuente de datos

Utiliza el DataFrame activo:

```python
st.session_state["datos_activos"]
```

Reutiliza `mostrar_carga_datos()` o la función correspondiente de `src/interfaz_carga.py`.

No leas directamente el Excel desde la página.

La página debe funcionar aunque el usuario acceda directamente a ella.

# Tipo de prueba

Utiliza una prueba Chi-cuadrado de independencia porque:

* existe una sola muestra semanal de monopatines;
* se observan conjuntamente dos variables cualitativas sobre cada unidad;
* se desea evaluar si ambas variables están asociadas.

Hipótesis:

```text
H₀: La sucursal y el nivel de fallos técnicos son independientes en la población de monopatines de Volt-Ar Scooters.

H₁: La sucursal y el nivel de fallos técnicos no son independientes; existe asociación entre ambas variables en la población.
```

Utiliza:

```python
scipy.stats.chi2_contingency(
    tabla_observada,
    correction=False,
)
```

Los marginales no deben incluirse en la prueba.

# Reutilización de P-04

Reutiliza las funciones existentes siempre que sean apropiadas:

* `construir_tabla_contingencia`
* `calcular_chi_cuadrado_muestral`

No dupliques cálculos.

Puedes ampliar la estructura de resultado o crear una nueva estructura inferencial si mejora la separación de responsabilidades, pero no rompas la Página 1.

# Frecuencias esperadas

Implementa una función equivalente a:

```python
def construir_tabla_frecuencias_esperadas(
    tabla_observada: pandas.DataFrame,
) -> pandas.DataFrame:
    ...
```

También verifica mediante pruebas la fórmula:

[
E_{ij}=
\frac{
(\text{total fila }i)
(\text{total columna }j)
}{
N
}
]

La tabla esperada debe mantener las mismas etiquetas y el mismo orden que la tabla observada efectiva.

No agregues marginales a la tabla esperada salvo como visualización separada, porque no forman parte de las celdas de la prueba.

# Frecuencias diferenciales relativas

La consigna utiliza la expresión “frecuencias diferenciales relativas”, pero el material disponible no incorpora una definición operacional explícita.

Utiliza como convención documentada:

[
D_{ij}=
\frac{O_{ij}-E_{ij}}{E_{ij}}
]

Para la interfaz, expresa el resultado como porcentaje:

[
D_{ij}%=
\frac{O_{ij}-E_{ij}}{E_{ij}}\times100
]

Implementa una función equivalente a:

```python
def calcular_diferencias_relativas(
    observadas: pandas.DataFrame,
    esperadas: pandas.DataFrame,
) -> pandas.DataFrame:
    ...
```

Interpretación técnica:

* valor positivo: frecuencia observada superior a la esperada bajo independencia;
* valor negativo: frecuencia observada inferior a la esperada;
* valor cercano a cero: frecuencia observada próxima a la esperada.

No interpretes una celda aislada como prueba suficiente de asociación.

Documenta expresamente que esta es la convención adoptada por el proyecto y que debe validarse con el criterio del docente si utiliza otra definición.

# Aporte de cada celda

Como complemento técnico, implementa internamente:

[
C_{ij}=
\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
]

La suma de los aportes debe coincidir con el estadístico Chi-cuadrado.

Puedes mostrar esta tabla dentro de un `st.expander` titulado:

```text
Ver aporte de cada celda al estadístico Chi-cuadrado
```

No confundas esta tabla con las diferencias relativas.

# Nivel de significancia

Agrega un deslizador en la Página 2:

* mínimo: 0.01;
* máximo: 0.10;
* valor inicial: 0.05;
* paso: 0.01;
* clave única de Streamlit.

El p-valor no debe cambiar con α.

La decisión sí debe actualizarse dinámicamente.

# Regla de decisión

Implementa:

```text
Si p-valor < α: se rechaza H₀.
Si p-valor ≥ α: no se rechaza H₀.
```

No utilizar “se acepta H₀”.

# Conclusión contextual dinámica

Cuando `p < α`, generar una conclusión equivalente a:

> Con un nivel de significancia de α, se rechaza la hipótesis nula. En el escenario analizado existe evidencia estadísticamente significativa de asociación entre la sucursal y el nivel de fallos técnicos en la población de monopatines de Volt-Ar Scooters.

Cuando `p ≥ α`, generar:

> Con un nivel de significancia de α, no se rechaza la hipótesis nula. Los datos disponibles no proporcionan evidencia estadística suficiente para afirmar que existe asociación entre la sucursal y el nivel de fallos técnicos en la población.

No afirmar categóricamente que las variables “son independientes” cuando no se rechaza H₀.

Como los datos son simulados, incluye una aclaración breve:

> La conclusión corresponde al escenario poblacional simulado con fines académicos.

# Supuestos y robustez

Evalúa dinámicamente:

## 1. Independencia de las observaciones

Este supuesto no puede verificarse únicamente a partir de la matriz.

Mostrar:

> Se asume que cada fila corresponde a un monopatín distinto y que cada observación es independiente. Este supuesto depende del diseño de recolección.

No marcarlo automáticamente como comprobado por una fórmula.

## 2. Categorías mutuamente excluyentes

Puede considerarse respaldado por la estructura validada:

* cada monopatín pertenece a una sola sucursal;
* cada monopatín posee un único nivel de fallos.

## 3. Frecuencias esperadas

Evaluar:

* ninguna frecuencia esperada menor que 1;
* al menos el 80 % de las celdas con frecuencia esperada mayor o igual que 5;
* porcentaje de celdas entre 1 y menos de 5;
* cantidad de celdas menores que 1.

Crear una estructura equivalente a:

```python
@dataclass(frozen=True)
class EvaluacionRobustezChiCuadrado:
    frecuencia_esperada_minima: float
    cantidad_menores_que_uno: int
    cantidad_menores_que_cinco: int
    porcentaje_mayores_o_iguales_a_cinco: float
    cumple_minimo_absoluto: bool
    cumple_regla_ochenta_por_ciento: bool
    es_robusta: bool
```

La prueba se considerará robusta solamente si:

```text
ninguna esperada < 1
y
al menos 80 % de esperadas ≥ 5
```

Si no se cumple, no bloquees el cálculo, pero muestra una advertencia indicando que la aproximación Chi-cuadrado debe interpretarse con precaución.

No agrupes categorías automáticamente.

Puede sugerirse:

* revisar si una combinación de categorías es metodológicamente válida;
* utilizar una prueba exacta apropiada;
* reportar el incumplimiento con cautela.

# Manejo de categorías ausentes

Reutiliza el criterio de P-04:

* elimina para el cálculo filas o columnas cuyo total observado sea cero;
* exige al menos dos categorías observadas en cada variable;
* conserva las categorías válidas cuando se muestren descripciones;
* informa qué categorías fueron excluidas del cálculo por no estar presentes.

No inventes frecuencias.

# Página 2

Completa `pages/2_Perfil_Analista.py`.

Debe contener:

1. Título “Perfil analista”.
2. Identificación del archivo activo.
3. Explicación del enfoque poblacional.
4. Sección “Inferencia cualitativa”.
5. Hipótesis H₀ y H₁.
6. Tabla de frecuencias observadas.
7. Tabla de frecuencias esperadas.
8. Tabla de diferencias relativas porcentuales.
9. Tarjetas:

   * Chi-cuadrado;
   * grados de libertad;
   * p-valor;
   * α.
10. Deslizador de α.
11. Decisión.
12. Conclusión contextual.
13. Evaluación de supuestos.
14. Indicador de robustez.
15. Expander opcional con aportes por celda.
16. Aclaración de que la inferencia cuantitativa se incorporará en la siguiente fase.

Las tablas deben tener títulos y una explicación breve.

No presentes la Página 2 como gerencial; debe ser técnica pero comprensible.

# Resultado predeterminado esperado

Con el Excel predeterminado:

Tabla observada:

```text
             Bajo  Medio  Alto
Rosario         3      9    12
Córdoba        14     10     0
```

Tabla esperada:

```text
             Bajo  Medio  Alto
Rosario       8.5    9.5    6.0
Córdoba       8.5    9.5    6.0
```

Diferencias relativas porcentuales aproximadas:

```text
Rosario:
Bajo   -64.71 %
Medio   -5.26 %
Alto   100.00 %

Córdoba:
Bajo    64.71 %
Medio    5.26 %
Alto  -100.00 %
```

Resultados:

* Chi-cuadrado ≈ 19.170279
* grados de libertad = 2
* p-valor ≈ 0.000069
* mínima esperada = 6
* esperadas ≥ 5 = 100 %
* prueba robusta = sí

Para α = 0.05 debe rechazarse H₀.

# Pruebas automatizadas

Agrega pruebas para:

1. Cálculo correcto de frecuencias esperadas.
2. Fórmula manual de una celda esperada.
3. Conservación de etiquetas y orden.
4. Igualdad de suma entre observadas y esperadas.
5. Cálculo correcto de diferencias relativas.
6. Signo positivo cuando O > E.
7. Signo negativo cuando O < E.
8. Cero cuando O = E.
9. Cálculo correcto de aportes por celda.
10. Suma de aportes igual al Chi-cuadrado.
11. Evaluación de robustez completamente cumplida.
12. Incumplimiento por frecuencia esperada menor que 1.
13. Incumplimiento de la regla del 80 %.
14. P-valor independiente de α.
15. Decisión de rechazo cuando `p < α`.
16. Decisión de no rechazo cuando `p ≥ α`.
17. No utilizar la expresión “aceptar H₀”.
18. Conclusión de rechazo contextualizada.
19. Conclusión de no rechazo sin afirmar independencia definitiva.
20. Resultado predeterminado esperado.
21. Manejo de categoría ausente.
22. Error cuando queda una sola categoría por variable.
23. La Página 2 contiene H₀ y H₁.
24. La Página 2 muestra la advertencia de independencia como supuesto de diseño.
25. P-04 y P-05 permanecen sin cambios funcionales.

No pruebes detalles internos frágiles de widgets.

# Documentación

Actualiza:

* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

Conserva P-00 a P-05.

Agrega P-06 con:

* prompt completo;
* archivos modificados;
* funciones implementadas;
* fórmula de frecuencias esperadas;
* convención adoptada para diferencias relativas;
* criterios de robustez;
* conclusiones dinámicas;
* validaciones;
* problemas y decisiones humanas;
* commit propuesto.

Documenta que la expresión “frecuencias diferenciales relativas” fue operacionalizada como `(O-E)/E`, dado que el material disponible no presenta una definición explícita con ese nombre.

# Archivos esperados

Los cambios deberían concentrarse en:

* `pages/2_Perfil_Analista.py`
* `src/analisis_cualitativo.py`
* `tests/test_analisis_cualitativo.py`
* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

No modifiques P-05 ni los módulos de carga o simulación salvo error real.

# Validaciones finales

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
```

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Inicia Streamlit temporalmente:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless=true --server.address=127.0.0.1 --server.port=8765 --server.runOnSave=false
```

Detén el proceso después de verificar el inicio.

Ejecuta:

```powershell
git diff --check
git status --short
```

Reporta para el Excel predeterminado:

* observadas;
* esperadas;
* diferencias relativas;
* aportes por celda;
* Chi-cuadrado;
* grados de libertad;
* p-valor;
* evaluación de robustez;
* decisión con α = 0.05;
* conclusión generada.

# Informe final

Informa:

1. Plan aplicado.
2. Archivos creados.
3. Archivos modificados.
4. Funciones implementadas.
5. Resultados predeterminados.
6. Criterios de robustez.
7. Resultado total de pruebas.
8. Resultado de Streamlit.
9. Confirmación de que P-04 y P-05 siguen funcionando.
10. Resultado de `git diff --check`.
11. Estado de Git.
12. Mensaje de commit propuesto.

No realices commit, push, merge ni Pull Request.

Detente y espera mi revisión.
````

### Archivos modificados

- `README.md`
- `docs/decisiones_metodologicas.md`
- `docs/prompts.md`
- `docs/registro_pruebas.md`
- `pages/2_Perfil_Analista.py`
- `src/analisis_cualitativo.py`
- `tests/test_analisis_cualitativo.py`

### Funciones implementadas

- `construir_tabla_frecuencias_esperadas`
- `calcular_diferencias_relativas`
- `calcular_aportes_chi_cuadrado`
- `evaluar_robustez_chi_cuadrado`
- `decidir_chi_cuadrado`
- `concluir_chi_cuadrado`
- `identificar_categorias_excluidas`

### Fórmula de frecuencias esperadas

Se implementó `Eij = total_fila_i * total_columna_j / N`, conservando las
etiquetas y el orden de la tabla observada efectiva.

### Convención para diferencias relativas

La expresión "frecuencias diferenciales relativas" fue operacionalizada como
`(O - E) / E`. En la interfaz se expresa como porcentaje mediante
`(O - E) / E * 100`, porque el material disponible no presentaba una definición
explícita con ese nombre.

### Criterios de robustez

La prueba se considera robusta solamente cuando no existe ninguna frecuencia
esperada menor que 1 y al menos el 80 % de las frecuencias esperadas es mayor o
igual que 5.

### Conclusiones dinámicas

- Si `p-valor < α`, se rechaza H0 y se informa evidencia estadísticamente
  significativa de asociación en el escenario poblacional simulado.
- Si `p-valor >= α`, no se rechaza H0 y se evita afirmar independencia
  definitiva.
- El p-valor no cambia cuando se modifica α; solo cambia la decisión.

### Resultado

Para el Excel predeterminado:

- tabla observada: Rosario `[3, 9, 12]`; Córdoba `[14, 10, 0]`;
- tabla esperada: Rosario `[8.5, 9.5, 6.0]`; Córdoba `[8.5, 9.5, 6.0]`;
- diferencias relativas porcentuales: Rosario `[-64.71, -5.26, 100.00]`;
  Córdoba `[64.71, 5.26, -100.00]`;
- Chi-cuadrado: 19.170278637771;
- grados de libertad: 2;
- p-valor: 0.000068742747;
- mínima esperada: 6.0;
- esperadas >= 5: 100 %;
- prueba robusta: sí;
- con α = 0.05 se rechaza H0.

### Problemas encontrados

- Al imprimir la decisión con `H₀` desde PowerShell apareció un
  `UnicodeEncodeError` por la codificación CP1252 de la consola. Se reejecutó el
  cálculo con `PYTHONIOENCODING=utf-8`.
- Una prueba del resultado predeterminado falló inicialmente porque el fixture
  esperado no incluía los nombres de índice y columnas (`Sucursal` y
  `Nivel_Fallos`); se corrigió el fixture.
- La comparación inicial del p-valor usaba el redondeo `0.000069` con una
  tolerancia demasiado estricta; se ajustó al valor real de SciPy
  `0.00006874274743165537`.

### Decisiones humanas

No se registraron correcciones humanas durante la implementación de P-06. La
definición de diferencias relativas queda documentada para validación posterior
con el criterio docente si fuera necesario.

### Validaciones

- `.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests`
- `.\.venv\Scripts\python.exe -m pytest -q`
- Inicio temporal de Streamlit en `http://127.0.0.1:8765`
- `git diff --check`
- `git status --short`

### Commit propuesto

```text
feat: agregar inferencia cualitativa
```

## P-07 — Inferencia cuantitativa

### Fecha

2026-06-26.

### Herramienta

Codex.

### Etapa

Inferencia cuantitativa para regresión lineal.

### Objetivo

Implementar en la Página 2 la prueba bilateral para la pendiente poblacional de
la regresión lineal entre `Antiguedad_Bateria_Meses` y `Autonomia_Real_Km`,
junto con intervalos de confianza para `β₀`, `β₁` y `ρ`.

### Prompt completo

````text
Trabaja exclusivamente en la rama `feat/inferencia-cuantitativa`.

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Confirma que la rama activa sea `feat/inferencia-cuantitativa`.
3. Verifica que el árbol de trabajo esté limpio.
4. Inspecciona:

   * `src/analisis_cuantitativo.py`
   * `pages/2_Perfil_Analista.py`
   * `pages/1_Perfil_Gerencial.py`
   * los tests existentes;
   * la documentación.
5. Confirma que P-06 esté presente en la Página 2.
6. Presenta un plan breve.
7. No realices commit, push, merge ni Pull Request.

# Fase P-07: inferencia cuantitativa para la regresión lineal

## Objetivo

Implementar en la Página 2 la prueba de hipótesis para la pendiente poblacional de la regresión lineal entre:

* X: `Antiguedad_Bateria_Meses`.
* Y: `Autonomia_Real_Km`.

También deben mostrarse intervalos de confianza dinámicos para los parámetros poblacionales.

No implementes todavía:

* calculadora de predicción;
* intervalo para la media esperada de Y;
* intervalo de predicción individual;
* gráfico de residuos;
* Q-Q Plot;
* histograma de residuos.

Estas funciones se incorporarán en fases posteriores.

# Fuente de datos

Utiliza el DataFrame activo almacenado en:

`st.session_state["datos_activos"]`

Reutiliza `mostrar_carga_datos()`.

No vuelvas a leer directamente el Excel.

Los resultados deben actualizarse automáticamente cuando cambien los datos activos.

# Modelo

Utiliza una regresión lineal simple con intercepto:

[
Y=\beta_0+\beta_1X+\varepsilon
]

Donde:

* (\beta_0): ordenada al origen poblacional.
* (\beta_1): pendiente poblacional.
* (X): antigüedad de la batería en meses.
* (Y): autonomía real en kilómetros.

Utiliza `statsmodels.api.OLS` o reutiliza el ajuste existente de P-05, evitando ajustar modelos distintos para la Página 1 y la Página 2.

No rompas la interfaz pública de las funciones utilizadas por P-05.

# Prueba de hipótesis

Implementa una prueba bilateral:

[
H_0:\beta_1=0
]

[
H_1:\beta_1\neq0
]

Interpretación:

* (H_0): no existe relación lineal poblacional entre antigüedad y autonomía.
* (H_1): existe una relación lineal poblacional entre antigüedad y autonomía.

Calcula:

* pendiente estimada;
* error estándar de la pendiente;
* estadístico (t);
* grados de libertad (n-2);
* p-valor bilateral;
* nivel de significancia;
* decisión.

El estadístico debe coincidir con:

[
t=\frac{b_1}{SE(b_1)}
]

y, en regresión simple, también con:

[
t=\frac{r\sqrt{n-2}}{\sqrt{1-r^2}}
]

Usa la salida de Statsmodels como fuente principal y la segunda fórmula como validación automatizada.

# Estructura de resultado

Crea una estructura tipada equivalente a:

```python
@dataclass(frozen=True)
class ResultadoInferenciaRegresion:
    cantidad: int
    grados_libertad: int
    intercepto: float
    pendiente: float
    error_estandar_intercepto: float
    error_estandar_pendiente: float
    estadistico_t_pendiente: float
    p_valor_pendiente: float
    coeficiente_pearson: float
    coeficiente_determinacion: float
    intervalo_intercepto: tuple[float, float]
    intervalo_pendiente: tuple[float, float]
    intervalo_correlacion: tuple[float, float] | None
    nivel_confianza: float
```

Puede ajustarse el diseño si existe una alternativa más limpia, pero debe mantenerse el acceso explícito a todos esos resultados.

# Nivel de significancia

Agrega un deslizador independiente para la inferencia cuantitativa:

* mínimo: 0.01;
* máximo: 0.10;
* valor inicial: 0.05;
* paso: 0.01;
* clave única de Streamlit.

El p-valor no debe cambiar al modificar α.

La decisión sí debe actualizarse.

Regla:

* si `p < α`: se rechaza (H_0);
* si `p ≥ α`: no se rechaza (H_0).

Nunca utilizar “se acepta H₀”.

# Conclusión contextual

Si `p < α` y la pendiente es negativa, generar una conclusión equivalente a:

> Con un nivel de significancia de α, se rechaza H₀. Existe evidencia estadísticamente significativa de una relación lineal negativa entre la antigüedad de la batería y la autonomía real en la población simulada de monopatines Volt-Ar.

Si `p < α` y la pendiente es positiva, adaptar el sentido.

Si `p ≥ α`, generar:

> Con un nivel de significancia de α, no se rechaza H₀. Los datos no proporcionan evidencia suficiente para afirmar que exista una relación lineal poblacional entre la antigüedad y la autonomía.

No afirmar causalidad.

Agregar:

> La conclusión corresponde al escenario poblacional simulado con fines académicos.

# Intervalos de confianza

Incorpora un deslizador de nivel de confianza:

* mínimo: 90 %;
* máximo: 99 %;
* valor inicial: 95 %;
* paso: 1 %;
* clave única de Streamlit.

Calcula dinámicamente intervalos para:

1. Intercepto poblacional (\beta_0).
2. Pendiente poblacional (\beta_1).

Utiliza la distribución t y los errores estándar del modelo, preferentemente mediante:

```python
modelo.conf_int(alpha=1 - nivel_confianza)
```

Los estimadores puntuales, el estadístico t y el p-valor no deben cambiar al modificar el nivel de confianza.

Solo deben cambiar los límites de los intervalos.

Mostrar claramente:

* estimación puntual;
* límite inferior;
* límite superior;
* nivel de confianza seleccionado.

Interpretación de la pendiente:

* si el intervalo no contiene cero, es coherente con el rechazo bilateral de (H_0) al nivel equivalente;
* si contiene cero, no existe esa coherencia.

No uses el intervalo como sustituto del p-valor; preséntalos como procedimientos equivalentes bajo las mismas condiciones.

# Intervalo para el coeficiente de correlación

Como complemento y para cubrir explícitamente la referencia de la consigna al coeficiente de correlación, calcula un intervalo para (\rho) mediante la transformación de Fisher:

[
z_r=\operatorname{atanh}(r)
]

[
SE_z=\frac{1}{\sqrt{n-3}}
]

[
z_r\pm z_{\alpha/2}SE_z
]

y transforma nuevamente con `tanh`.

Requisitos:

* solo se calcula cuando (n>3);
* manejar adecuadamente (r=1) o (r=-1);
* el intervalo debe permanecer dentro de ([-1,1]);
* documentar que se trata de la aproximación de Fisher.

Si el caso perfecto requiere un tratamiento especial, devuelve un resultado controlado y muestra una advertencia comprensible.

# Página 2

Conserva íntegramente el módulo cualitativo P-06.

Agrega debajo:

## Inferencia cuantitativa

Debe mostrar:

1. Modelo poblacional planteado.
2. Hipótesis (H_0) y (H_1).
3. Variable X y variable Y.
4. Pendiente estimada.
5. Error estándar de la pendiente.
6. Estadístico t.
7. Grados de libertad.
8. P-valor.
9. Deslizador de α.
10. Decisión.
11. Conclusión contextual.
12. Deslizador de confianza entre 90 % y 99 %.
13. Intervalo para (\beta_0).
14. Intervalo para (\beta_1).
15. Intervalo para (\rho), identificado como aproximación de Fisher.
16. Aclaración de que la predicción y los diagnósticos se incorporarán en las fases siguientes.

Utiliza tarjetas o columnas para organizar los valores.

# Controles estadísticos

Antes del ajuste, verifica:

* al menos cuatro observaciones;
* valores finitos;
* ausencia de nulos;
* variabilidad en X;
* variabilidad en Y;
* grados de libertad positivos.

Muestra errores comprensibles y no trazas técnicas de Python.

# Resultado esperado con el Excel predeterminado

Aproximadamente:

* (n=48);
* (gl=46);
* intercepto = 45.166071;
* pendiente = -0.552768;
* Pearson = -0.900523;
* (R^2=0.810942);
* estadístico (t) de la pendiente ≈ -14.0468;
* p-valor bilateral ≈ (2.97\times10^{-18}).

Para (\alpha=0.05), debe rechazarse (H_0).

Los intervalos deben calcularse con el modelo real; no los fijes manualmente.

# Pruebas automatizadas

Agrega pruebas para:

1. (gl=n-2).
2. Estadístico t igual a pendiente/error estándar.
3. Correspondencia con la fórmula basada en Pearson.
4. P-valor dentro de [0,1].
5. P-valor coincidente con Statsmodels.
6. Decisión de rechazo cuando `p < α`.
7. Decisión de no rechazo cuando `p ≥ α`.
8. No utilizar “aceptar H₀”.
9. Conclusión contextual negativa.
10. Conclusión contextual positiva.
11. Conclusión de no rechazo correctamente redactada.
12. Intervalo de pendiente coincidente con Statsmodels.
13. Intervalo de intercepto coincidente con Statsmodels.
14. Los intervalos se amplían al aumentar el nivel de confianza.
15. Los estimadores no cambian con el nivel de confianza.
16. El p-valor no cambia con α.
17. El intervalo de Fisher queda dentro de [-1,1].
18. El intervalo de Fisher contiene al valor r estimado.
19. Manejo de (n\leq3).
20. Manejo de correlación perfecta.
21. Error con X constante.
22. Error con Y constante.
23. Resultado aproximado del Excel predeterminado.
24. P-06 permanece presente.
25. P-04 y P-05 siguen funcionando.
26. La Página 2 no muestra todavía predicciones ni diagnósticos.
27. No aparece lenguaje causal.

No crees pruebas frágiles sobre detalles visuales internos de Streamlit.

# Documentación

Actualiza:

* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

Conserva íntegramente P-00 a P-06.

Agrega P-07 con:

* prompt completo;
* archivos modificados;
* fórmulas;
* decisiones estadísticas;
* intervalo de Fisher;
* validaciones;
* resultados;
* problemas encontrados;
* correcciones humanas;
* commit propuesto.

Documenta:

* diferencia entre pendiente muestral y pendiente poblacional;
* interpretación del estadístico t;
* (gl=n-2);
* relación entre prueba para pendiente y prueba para correlación;
* diferencia entre α y nivel de confianza;
* por qué el p-valor no cambia con α;
* por qué los intervalos se amplían al aumentar la confianza;
* ausencia de causalidad;
* carácter simulado del escenario.

# Archivos esperados

Los cambios deberían concentrarse en:

* `pages/2_Perfil_Analista.py`
* `src/analisis_cuantitativo.py`
* `tests/test_analisis_cuantitativo.py`
* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

No modifiques simulación, carga ni análisis cualitativo salvo que exista un error real.

# Validaciones finales

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
```

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Inicia Streamlit temporalmente:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless=true --server.address=127.0.0.1 --server.port=8765 --server.runOnSave=false
```

Detén el proceso después de comprobarlo.

Ejecuta:

```powershell
git diff --check
git status --short
```

Reporta para el Excel predeterminado:

* n;
* grados de libertad;
* intercepto;
* pendiente;
* error estándar de la pendiente;
* t;
* p-valor;
* decisión con α=0.05;
* IC del 95 % para (\beta_0);
* IC del 95 % para (\beta_1);
* IC del 95 % para (\rho);
* conclusión generada.

# Informe final

Informa:

1. Plan aplicado.
2. Archivos creados.
3. Archivos modificados.
4. Funciones implementadas.
5. Resultados predeterminados.
6. Intervalos calculados.
7. Resultado total de pruebas.
8. Resultado de Streamlit.
9. Confirmación de que P-06 sigue funcionando.
10. Confirmación de que no se implementaron predicción ni diagnósticos.
11. Resultado de `git diff --check`.
12. Estado de Git.
13. Mensaje de commit propuesto.

No realices commit, push, merge ni Pull Request.

Detente y espera mi revisión.
````

### Archivos modificados

- `README.md`
- `docs/decisiones_metodologicas.md`
- `docs/prompts.md`
- `docs/registro_pruebas.md`
- `pages/2_Perfil_Analista.py`
- `src/analisis_cuantitativo.py`
- `tests/test_analisis_cuantitativo.py`

### Fórmulas

- Modelo: `Y = β₀ + β₁X + ε`.
- Estadístico t de la pendiente: `t = b₁ / SE(b₁)`.
- Equivalencia con Pearson: `t = r * sqrt(n - 2) / sqrt(1 - r²)`.
- Grados de libertad: `gl = n - 2`.
- Intervalos de parámetros: `modelo.conf_int(alpha=1 - nivel_confianza)`.
- Fisher para `ρ`: `atanh(r) ± z_critico / sqrt(n - 3)`, con transformación
  inversa mediante `tanh`.

### Decisiones estadísticas

- Se reutiliza el mismo ajuste OLS con intercepto para mantener coherencia con
  P-05.
- La prueba para la pendiente es bilateral.
- El p-valor no cambia al modificar `α`; solo cambia la decisión.
- El nivel de confianza modifica únicamente los límites de los intervalos.
- El intervalo de Fisher se omite de forma controlada si `n <= 3` o si la
  correlación es perfecta.
- La conclusión evita lenguaje causal y se limita al escenario poblacional
  simulado.

### Resultado

Para el Excel predeterminado:

- n: 48;
- grados de libertad: 46;
- intercepto: 45.166071483068;
- pendiente: -0.552768328535;
- error estándar de la pendiente: 0.039351986237;
- estadístico t: -14.046770732231;
- p-valor bilateral: 2.973713410738031e-18;
- Pearson: -0.900523263956;
- R²: 0.810942148925;
- decisión con α = 0.05: se rechaza H0.

Intervalos del 95 %:

- `β₀`: [43.016085150163, 47.316057815973];
- `β₁`: [-0.631979768441, -0.473556888629];
- `ρ`: [-0.943296719385, -0.828334414381].

### Problemas encontrados

- Una prueba P-05 dependía del texto "al menos tres"; al parametrizar la cantidad
  mínima para P-07 el mensaje cambió a "3". Se corrigió para mantener la
  compatibilidad del mensaje previo.

### Correcciones humanas

No se registraron correcciones humanas durante la implementación de P-07.

### Validaciones

- `.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests`
- `.\.venv\Scripts\python.exe -m pytest -q`
- Inicio temporal de Streamlit en `http://127.0.0.1:8765`
- `git diff --check`
- `git status --short`

### Commit propuesto

```text
feat: agregar inferencia cuantitativa
```

## P-08 — Calculadora de predicción

### Fecha

2026-06-26.

### Herramienta

Codex.

### Etapa

Calculadora de predicción de autonomía.

### Objetivo

Implementar una calculadora técnica que permita ingresar la antigüedad de la
batería y obtener la autonomía estimada, el intervalo para la media esperada y
el intervalo de predicción individual, usando el mismo modelo de regresión de
P-05 y P-07.

### Prompt completo

````text
Trabaja exclusivamente en la rama `feat/calculadora-prediccion`.

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Confirma que la rama activa sea `feat/calculadora-prediccion`.
3. Verifica que el árbol de trabajo esté limpio.
4. Inspecciona:

   * `src/analisis_cuantitativo.py`
   * `pages/2_Perfil_Analista.py`
   * los tests existentes;
   * la documentación.
5. Confirma que P-06 y P-07 estén presentes en la Página 2.
6. Presenta un plan breve.
7. No realices commit, push, merge ni Pull Request.

# Fase P-08: calculadora de predicción de autonomía

## Objetivo

Implementar una calculadora técnica que permita ingresar un valor de antigüedad de la batería y obtener:

1. La autonomía puntual estimada.
2. El intervalo de confianza para el valor esperado promedio de autonomía.
3. El intervalo de predicción para una observación individual.

La calculadora debe utilizar el mismo modelo de regresión ajustado en P-05 y P-07.

No implementes todavía:

* gráfico de residuos;
* Q-Q Plot;
* histograma de residuos;
* pruebas adicionales de normalidad u homocedasticidad.

Estas funciones se incorporarán en fases posteriores.

# Fuente de datos y modelo

Utiliza el DataFrame activo:

`st.session_state["datos_activos"]`

No vuelvas a leer directamente el Excel.

No ajustes un segundo modelo distinto. Reutiliza el ajuste de Statsmodels empleado en la inferencia cuantitativa.

La variable independiente es:

`Antiguedad_Bateria_Meses`

La variable dependiente es:

`Autonomia_Real_Km`

# Nivel de confianza

Reutiliza el nivel de confianza seleccionado para los intervalos de P-07.

Evita crear dos selectores diferentes que puedan producir resultados contradictorios.

El nivel debe variar entre 90 % y 99 %.

Al aumentar la confianza:

* el intervalo para la media debe ampliarse;
* el intervalo de predicción individual debe ampliarse;
* la predicción puntual no debe cambiar.

# Entrada del analista

Agrega un campo numérico para ingresar la antigüedad:

* mínimo operativo: 1 mes;
* máximo operativo: 48 meses;
* paso: 1;
* valor inicial razonable, por ejemplo 24 meses;
* clave única de Streamlit.

La entrada debe considerarse numérica entera porque la variable se registra en meses completos.

También determina dinámicamente:

* mínimo observado de X;
* máximo observado de X.

Si el valor ingresado está fuera del rango observado de la muestra, pero dentro del rango operativo 1–48, permite calcular la predicción y muestra una advertencia:

> El valor ingresado se encuentra fuera del rango observado en la muestra. La estimación constituye una extrapolación y debe interpretarse con mayor precaución.

No bloquees una extrapolación válida dentro del rango operativo.

# Implementación estadística

Completa `src/analisis_cuantitativo.py` con una estructura equivalente a:

```python
@dataclass(frozen=True)
class ResultadoPrediccion:
    valor_x: float
    prediccion_puntual: float
    limite_inferior_media: float
    limite_superior_media: float
    limite_inferior_individual: float
    limite_superior_individual: float
    nivel_confianza: float
    es_extrapolacion: bool
    minimo_x_observado: float
    maximo_x_observado: float
```

Implementa funcionalidad equivalente a:

```python
def calcular_prediccion(
    datos: pandas.DataFrame,
    valor_x: float,
    nivel_confianza: float = 0.95,
) -> ResultadoPrediccion:
    ...
```

Utiliza Statsmodels:

```python
modelo.get_prediction(nuevos_datos).summary_frame(
    alpha=1 - nivel_confianza
)
```

Extrae correctamente:

* `mean`: predicción puntual;
* `mean_ci_lower`;
* `mean_ci_upper`;
* `obs_ci_lower`;
* `obs_ci_upper`.

No confundas los nombres ni intercambies ambos intervalos.

# Interpretación de los intervalos

## Intervalo para la media esperada

Debe presentarse como:

> Intervalo de confianza para la autonomía promedio esperada de todos los monopatines con una antigüedad de X meses.

No lo interpretes como un intervalo que contiene un porcentaje de monopatines individuales.

## Intervalo de predicción individual

Debe presentarse como:

> Intervalo de predicción para la autonomía de un monopatín individual con una antigüedad de X meses.

Debe aclararse que es más amplio porque incorpora:

* incertidumbre sobre la media estimada;
* variabilidad individual alrededor de la recta.

# Condición de amplitud

Debe cumplirse, salvo pequeñas tolerancias numéricas:

```text
ancho del intervalo individual
>=
ancho del intervalo para la media
```

Implementa funciones auxiliares si ayudan a probar esta condición.

# Límites físicos

No recortes automáticamente los intervalos estadísticos a 15–45 km.

La base simulada utiliza ese rango operativo, pero recortar los intervalos alteraría artificialmente el resultado matemático del modelo.

Si algún límite cae fuera del rango operativo, muestra una nota:

> El intervalo estadístico excede el rango operativo utilizado en la simulación; se presenta sin recorte para conservar el resultado del modelo.

La predicción puntual tampoco debe recortarse silenciosamente.

# Página 2

Conserva íntegramente:

* inferencia cualitativa P-06;
* prueba de pendiente e intervalos P-07.

Agrega debajo una sección:

## Calculadora de predicción

Debe mostrar:

1. Campo de antigüedad.
2. Nivel de confianza utilizado.
3. Predicción puntual.
4. Intervalo para la media esperada.
5. Intervalo de predicción individual.
6. Comparación visual de amplitudes.
7. Advertencia de extrapolación cuando corresponda.
8. Explicación de la diferencia entre ambos intervalos.
9. Nota sobre límites fuera del rango operativo cuando corresponda.

Presenta los resultados en kilómetros con dos decimales, pero conserva la precisión completa internamente.

# Gráfico opcional recomendado

Agrega un gráfico técnico sencillo con:

* eje X: antigüedad;
* eje Y: autonomía estimada;
* recta del modelo;
* banda del intervalo de confianza para la media;
* banda del intervalo de predicción individual;
* marcador para el valor ingresado.

Este gráfico es recomendado, pero no debe duplicar ni sustituir los valores numéricos.

Debe utilizar exactamente el mismo modelo y nivel de confianza.

No agregues una segunda regresión.

# Pruebas automatizadas

Agrega pruebas para:

1. Predicción puntual coincidente con (b_0+b_1x_0).
2. Resultados coincidentes con `get_prediction`.
3. Intervalo para la media correctamente asignado.
4. Intervalo individual correctamente asignado.
5. Intervalo individual más amplio o igual que el intervalo de la media.
6. La predicción puntual pertenece al intervalo de la media.
7. La predicción puntual pertenece al intervalo individual.
8. Los intervalos se amplían al aumentar la confianza.
9. La predicción puntual no cambia al modificar la confianza.
10. Detección de valor dentro del rango observado.
11. Detección de extrapolación inferior.
12. Detección de extrapolación superior.
13. Aceptación de valores operativos entre 1 y 48.
14. Rechazo de valores menores que 1.
15. Rechazo de valores mayores que 48.
16. Rechazo de valores no finitos.
17. Preservación de los intervalos sin recorte.
18. Resultado del Excel predeterminado para X = 24.
19. P-06 y P-07 permanecen presentes.
20. No se implementaron todavía gráficos de diagnóstico.
21. No aparece lenguaje causal.

No crees pruebas frágiles de detalles internos de Streamlit.

# Resultado esperado aproximado

Para el archivo predeterminado y X = 24:

[
\hat{Y}
 =======

## 45.166071

0.552768(24)
]

La predicción puntual debería ser aproximadamente:

[
31.90\text{ km}
]

Los intervalos deben calcularse dinámicamente mediante Statsmodels. No fijes manualmente sus límites.

El intervalo individual debe ser claramente más amplio que el intervalo para la media.

# Documentación

Actualiza:

* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

Conserva íntegramente P-00 a P-07.

Agrega P-08 con:

* prompt completo;
* funciones implementadas;
* diferencias entre ambos intervalos;
* decisión de no recortar los intervalos;
* tratamiento de extrapolación;
* resultados;
* pruebas;
* problemas encontrados;
* commit propuesto.

Documenta:

* diferencia entre estimación puntual e intervalo;
* intervalo para media esperada;
* intervalo para observación individual;
* motivo por el que el segundo es más amplio;
* efecto del nivel de confianza;
* diferencia entre interpolación y extrapolación;
* ausencia de causalidad.

# Archivos esperados

Los cambios deberían concentrarse en:

* `src/analisis_cuantitativo.py`
* `pages/2_Perfil_Analista.py`
* `tests/test_analisis_cuantitativo.py`
* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

No modifiques carga, simulación ni análisis cualitativo salvo que exista un error real.

# Validaciones finales

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
```

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Inicia Streamlit temporalmente:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless=true --server.address=127.0.0.1 --server.port=8765 --server.runOnSave=false
```

Detén el proceso después de comprobarlo.

Ejecuta:

```powershell
git diff --check
git status --short
```

Para el Excel predeterminado y X = 24 reporta:

* predicción puntual;
* intervalo para la media al 95 %;
* intervalo individual al 95 %;
* ancho de ambos intervalos;
* si es interpolación o extrapolación;
* advertencias aplicables.

# Informe final

Informa:

1. Plan aplicado.
2. Archivos creados.
3. Archivos modificados.
4. Funciones implementadas.
5. Resultado para X = 24.
6. Comparación de intervalos.
7. Total de pruebas aprobadas.
8. Resultado de Streamlit.
9. Confirmación de que P-06 y P-07 continúan funcionando.
10. Confirmación de que todavía no se implementaron diagnósticos.
11. Resultado de `git diff --check`.
12. Estado de Git.
13. Mensaje de commit propuesto.

No realices commit, push, merge ni Pull Request.

Detente y espera mi revisión.
````

### Funciones implementadas

- `calcular_prediccion`
- `construir_bandas_prediccion`
- `calcular_ancho_intervalo`

### Diferencia entre intervalos

- El intervalo para la media esperada estima la autonomía promedio esperada para
  monopatines con una antigüedad determinada.
- El intervalo individual estima la autonomía de un monopatín específico y es
  más amplio porque incorpora incertidumbre de la media y variabilidad
  individual alrededor de la recta.

### Decisiones estadísticas

- Se usa `modelo.get_prediction(...).summary_frame(alpha=1 - nivel_confianza)`.
- La predicción puntual usa `mean`.
- El intervalo para media usa `mean_ci_lower` y `mean_ci_upper`.
- El intervalo individual usa `obs_ci_lower` y `obs_ci_upper`.
- No se recortan predicción ni intervalos al rango operativo 15-45 km.
- La extrapolación se permite dentro del rango operativo 1-48 meses y se
  informa con advertencia.

### Resultado

Para el Excel predeterminado, X = 24 y confianza 95 %:

- predicción puntual: 31.899631598222 km;
- intervalo para la media: [30.864691368214, 32.934571828230];
- intervalo individual: [24.655952220355, 39.143310976089];
- ancho del intervalo para la media: 2.069880460016 km;
- ancho del intervalo individual: 14.487358755734 km;
- rango observado de X: 2 a 47 meses;
- X = 24 es interpolación;
- no aplica advertencia de extrapolación ni de límites fuera del rango operativo.

### Problemas encontrados

- Una prueba textual esperaba "Intervalo de predicción" en singular, pero la
  página usa el título "Intervalos de predicción". Se corrigió la prueba para
  reflejar el texto real.

### Correcciones humanas

No se registraron correcciones humanas durante la implementación de P-08.

### Validaciones

- `.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests`
- `.\.venv\Scripts\python.exe -m pytest -q`
- Inicio temporal de Streamlit en `http://127.0.0.1:8765`
- `git diff --check`
- `git status --short`

### Commit propuesto

```text
feat: agregar calculadora de prediccion
```

## P-09 — Diagnóstico de residuos y validación técnica de supuestos

### Objetivo

Completar la validación técnica del modelo de regresión lineal simple en la
Página 2 mediante residuos, residuos estandarizados, gráfico de residuos frente
a valores ajustados, Q-Q Plot e histograma complementario.

### Prompt completo

````text
Trabaja exclusivamente en la rama `feat/diagnostico-residuos`.

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Confirma que la rama activa sea `feat/diagnostico-residuos`.
3. Verifica que el árbol de trabajo esté limpio.
4. Inspecciona:

   * `src/analisis_cuantitativo.py`
   * `pages/2_Perfil_Analista.py`
   * los tests existentes;
   * la documentación.
5. Confirma que P-06, P-07 y P-08 estén presentes en la Página 2.
6. Presenta un plan breve.
7. No realices commit, push, merge ni Pull Request.

# Fase P-09: diagnóstico de residuos y validación técnica de supuestos

## Objetivo

Completar la validación técnica del modelo de regresión lineal mediante:

1. Gráfico de residuos frente a valores ajustados.
2. Gráfico de probabilidad normal Q-Q de los residuos.
3. Histograma de residuos como complemento.
4. Explicación técnica de los supuestos de:

   * linealidad;
   * homocedasticidad;
   * normalidad de los errores.

Los gráficos deben actualizarse automáticamente cuando cambie el archivo semanal activo.

No ajustes un modelo diferente. Reutiliza exactamente el mismo modelo empleado en P-05, P-07 y P-08.

# Fuente de datos

Utiliza:

`st.session_state["datos_activos"]`

No leas directamente el Excel.

La variable independiente continúa siendo:

`Antiguedad_Bateria_Meses`

La variable dependiente continúa siendo:

`Autonomia_Real_Km`

# Estructura de diagnóstico

Completa `src/analisis_cuantitativo.py` con una estructura tipada equivalente a:

```python
@dataclass(frozen=True)
class ResultadoDiagnosticoResiduos:
    valores_ajustados: pandas.Series
    residuos: pandas.Series
    residuos_estandarizados: pandas.Series
    media_residuos: float
    desviacion_residuos: float
    cantidad_residuos_atipicos_dos: int
    cantidad_residuos_atipicos_tres: int
```

Puedes adaptar el diseño si existe una alternativa más limpia, pero debe permitir reutilizar claramente los datos en la interfaz y las pruebas.

Implementa funciones equivalentes a:

```python
def calcular_diagnostico_residuos(
    datos: pandas.DataFrame,
) -> ResultadoDiagnosticoResiduos:
    ...
```

```python
def construir_datos_residuos_ajustados(
    datos: pandas.DataFrame,
    diagnostico: ResultadoDiagnosticoResiduos,
) -> pandas.DataFrame:
    ...
```

```python
def construir_datos_qq(
    residuos: pandas.Series,
) -> pandas.DataFrame:
    ...
```

```python
def construir_datos_histograma_residuos(
    residuos: pandas.Series,
) -> pandas.DataFrame:
    ...
```

# Residuos

Utiliza:

[
e_i = y_i-\hat y_i
]

Los residuos y valores ajustados deben provenir del mismo modelo utilizado en las fases anteriores.

Verifica:

* misma cantidad de residuos que observaciones;
* valores finitos;
* media de residuos aproximadamente cero debido a la presencia del intercepto;
* variabilidad residual positiva.

# Residuos estandarizados

Calcula residuos estandarizados mediante Statsmodels, preferentemente usando la influencia del modelo:

```python
influencia = modelo.get_influence()
residuos_estandarizados = influencia.resid_studentized_internal
```

No uses simplemente `residuo / desviación estándar` si Statsmodels ya proporciona el cálculo apropiado.

Utiliza los residuos estandarizados únicamente como ayuda diagnóstica.

Identifica:

* posibles observaciones atípicas cuando (|r_i|>2);
* observaciones más extremas cuando (|r_i|>3).

No elimines observaciones automáticamente.

No declares que una observación es errónea solamente por superar esos valores.

# Gráfico de residuos frente a valores ajustados

Utiliza Plotly.

Requisitos:

* Eje X: valores ajustados de autonomía.
* Eje Y: residuos.
* Línea horizontal en (y=0).
* Puntos individuales sin líneas que los conecten.
* Tooltip con:

  * autonomía observada;
  * autonomía ajustada;
  * residuo;
  * residuo estandarizado;
  * antigüedad;
  * sucursal;
  * nivel de fallos.
* Títulos y ejes en español.
* Los puntos con (|residuo estandarizado|>2) pueden destacarse visualmente.
* No elimines ni ocultes esos puntos.

Incluye una guía interpretativa:

### Linealidad

Un patrón curvo o sistemático alrededor de cero puede indicar que la forma lineal no representa adecuadamente la relación.

### Homocedasticidad

Una dispersión aproximadamente constante de residuos a lo largo de los valores ajustados es compatible con varianza constante.

Una forma de embudo puede indicar heterocedasticidad.

No generes automáticamente una conclusión categórica basada solamente en una regla simplista.

# Q-Q Plot

Construye el Q-Q Plot mediante:

```python
scipy.stats.probplot
```

o una alternativa estadísticamente equivalente.

Debe contener:

* cuantiles teóricos normales;
* residuos ordenados;
* línea de referencia;
* puntos individuales;
* ejes y título en español.

La línea debe construirse con la pendiente e intercepto devueltos por `probplot` o mediante un procedimiento equivalente validado.

Interpretación visible:

> Si los puntos se aproximan razonablemente a la línea de referencia, el supuesto de normalidad de los residuos resulta compatible con los datos. Desviaciones sistemáticas, especialmente en los extremos, pueden indicar falta de normalidad.

No afirmar automáticamente normalidad perfecta.

# Histograma de residuos

Incluye un histograma como complemento.

Requisitos:

* residuos en el eje X;
* frecuencia en el eje Y;
* cantidad razonable de intervalos;
* línea vertical en cero;
* título en español.

El histograma no sustituye al Q-Q Plot.

Puede colocarse dentro de un expander si la página queda demasiado extensa.

# Evaluación técnica visible

Agrega una sección con tres bloques:

## Linealidad

Explicar qué debe observarse en residuos frente a ajustados.

## Homocedasticidad

Explicar qué significa dispersión aproximadamente constante.

## Normalidad

Explicar que el supuesto se refiere a los residuos o errores del modelo, no necesariamente a X o Y.

También mostrar:

* media de residuos;
* desviación estándar residual;
* cantidad con (|residuo estandarizado|>2);
* cantidad con (|residuo estandarizado|>3).

No presentar estos conteos como una prueba definitiva.

# Supuesto de independencia

La independencia de los errores no puede validarse completamente mediante estos gráficos.

Incluye una aclaración:

> La independencia depende del diseño de recolección. Se asume que cada fila representa un monopatín diferente y que las observaciones no dependen entre sí.

No implementar pruebas de series temporales, ya que la matriz representa una muestra semanal transversal y no una serie ordenada en el tiempo.

# Página 2

Conserva íntegramente:

* P-06: inferencia cualitativa;
* P-07: inferencia para la pendiente e intervalos;
* P-08: calculadora de predicción.

Agrega debajo:

## Validación técnica de supuestos

Debe contener:

1. Introducción breve.
2. Gráfico de residuos frente a valores ajustados.
3. Explicación de linealidad y homocedasticidad.
4. Q-Q Plot.
5. Histograma de residuos.
6. Métricas diagnósticas.
7. Aclaración sobre independencia.
8. Advertencia de que los gráficos requieren interpretación conjunta.

No agregues una conclusión automática del tipo:

* “Todos los supuestos se cumplen”.
* “El modelo es válido”.
* “El modelo queda invalidado”.

Puede utilizarse un texto prudente como:

> Los gráficos permiten evaluar la compatibilidad de los datos con los supuestos. La decisión debe considerar conjuntamente los patrones observados, el contexto y el tamaño muestral.

# Manejo de errores

Antes del diagnóstico verifica:

* cantidad suficiente de datos;
* valores finitos;
* variabilidad en X;
* variabilidad en Y;
* residuos con variabilidad.

Muestra mensajes comprensibles y evita trazas técnicas en Streamlit.

# Resultado predeterminado

Para el Excel predeterminado reporta:

* media de residuos;
* desviación estándar de residuos;
* mínimo y máximo de residuos;
* cantidad con (|residuo estandarizado|>2);
* cantidad con (|residuo estandarizado|>3);
* parámetros de la línea Q-Q;
* confirmación de que se generaron 48 puntos en cada diagnóstico correspondiente.

No fijes manualmente resultados esperados que dependan de cálculos reales.

# Pruebas automatizadas

Agrega pruebas para:

1. Cantidad de residuos igual a n.
2. Cantidad de valores ajustados igual a n.
3. Cantidad de residuos estandarizados igual a n.
4. Residuos iguales a observado menos ajustado.
5. Media de residuos aproximadamente cero.
6. Valores finitos.
7. Variabilidad residual positiva.
8. Construcción de datos para residuos frente a ajustados.
9. Conservación de columnas de contexto para tooltip.
10. Línea horizontal de referencia definida en cero.
11. Q-Q Plot con la misma cantidad de puntos que residuos.
12. Cuantiles teóricos ordenados.
13. Residuos ordenados en los datos Q-Q.
14. Pendiente Q-Q finita.
15. Intercepto Q-Q finito.
16. Histograma construido con todos los residuos.
17. Conteo correcto de residuos estandarizados mayores que 2.
18. Conteo correcto de residuos estandarizados mayores que 3.
19. No eliminación automática de observaciones atípicas.
20. Error con X constante.
21. Error con Y constante.
22. Error con residuos sin variabilidad.
23. Resultado coherente con el Excel predeterminado.
24. P-06, P-07 y P-08 permanecen presentes.
25. La Página 2 contiene los títulos de ambos gráficos obligatorios.
26. La página explica que normalidad se evalúa sobre los residuos.
27. La página no declara automáticamente que todos los supuestos se cumplen.
28. No aparece lenguaje causal.

No crees pruebas frágiles sobre la configuración interna de los widgets.

# Documentación

Actualiza:

* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

Conserva íntegramente P-00 a P-08.

Agrega P-09 con:

* prompt completo;
* funciones implementadas;
* definición de residuo;
* significado de residuos estandarizados;
* criterios orientativos de (|r|>2) y (|r|>3);
* interpretación de linealidad;
* interpretación de homocedasticidad;
* interpretación del Q-Q Plot;
* limitación para evaluar independencia;
* resultados;
* pruebas;
* problemas encontrados;
* commit propuesto.

Documenta que:

* la normalidad requerida corresponde a los errores del modelo;
* el gráfico de residuos permite evaluar simultáneamente linealidad y homocedasticidad;
* el Q-Q Plot es la herramienta principal para normalidad;
* el histograma es complementario;
* los gráficos no producen automáticamente una decisión definitiva.

# Archivos esperados

Los cambios deben concentrarse en:

* `src/analisis_cuantitativo.py`
* `pages/2_Perfil_Analista.py`
* `tests/test_analisis_cuantitativo.py`
* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`

No modifiques simulación, carga ni análisis cualitativo salvo error real.

# Validaciones finales

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
```

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Inicia Streamlit temporalmente:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless=true --server.address=127.0.0.1 --server.port=8765 --server.runOnSave=false
```

Detén el proceso después de comprobarlo.

Ejecuta:

```powershell
git diff --check
git status --short
```

Para el Excel predeterminado reporta:

* cantidad de residuos;
* media;
* desviación estándar;
* mínimo;
* máximo;
* cantidad de residuos estandarizados con valor absoluto mayor que 2;
* cantidad mayor que 3;
* parámetros de referencia del Q-Q Plot;
* resultado total de pruebas.

# Informe final

Informa:

1. Plan aplicado.
2. Archivos creados.
3. Archivos modificados.
4. Funciones implementadas.
5. Resultados diagnósticos.
6. Total de pruebas aprobadas.
7. Resultado de Streamlit.
8. Confirmación de que P-06, P-07 y P-08 continúan funcionando.
9. Confirmación de que no se emite una aprobación automática de supuestos.
10. Resultado de `git diff --check`.
11. Estado de Git.
12. Mensaje de commit propuesto.

No realices commit, push, merge ni Pull Request.

Detente y espera mi revisión.
````

### Funciones implementadas

- `calcular_diagnostico_residuos`
- `construir_datos_residuos_ajustados`
- `construir_datos_qq`
- `construir_datos_histograma_residuos`

### Definiciones y criterios

- El residuo se define como `e_i = y_i - y_hat_i`.
- Los residuos estandarizados se calculan con
  `modelo.get_influence().resid_studentized_internal`.
- Los umbrales `|r| > 2` y `|r| > 3` se utilizan como ayudas diagnósticas
  orientativas. No eliminan observaciones ni implican que una fila sea errónea.
- El gráfico de residuos frente a ajustados permite revisar linealidad y
  homocedasticidad.
- El Q-Q Plot es la herramienta principal para revisar compatibilidad visual con
  normalidad de residuos.
- El histograma es complementario y no reemplaza al Q-Q Plot.
- La independencia depende del diseño de recolección y no puede validarse por
  completo mediante estos gráficos.
- Los gráficos no generan automáticamente una decisión definitiva sobre validez
  o invalidez del modelo.

### Resultado

Para el Excel predeterminado:

- cantidad de residuos: 48;
- media: -0.000000000000023;
- desviación estándar: 3.523622766997476;
- mínimo: -6.519009897968544;
- máximo: 9.230990102031456;
- cantidad con `|residuo estandarizado| > 2`: 1;
- cantidad con `|residuo estandarizado| > 3`: 0;
- puntos del Q-Q Plot: 48;
- pendiente de referencia Q-Q: 3.593496451157682;
- intercepto de referencia Q-Q: -0.000000000000023;
- filas en datos de residuos-ajustados: 48;
- frecuencia total del histograma: 48.

### Problemas encontrados

- El sandbox de Windows volvió a fallar con
  `CreateProcessAsUserW failed: 1920`; las inspecciones y validaciones se
  reintentaron con ejecución escalada.
- Se mantuvo una advertencia no fatal de PowerShell relacionada con
  `PSReadLine` cuando se ejecutaron comandos con perfil.
- Una prueba nueva comparó inicialmente contra
  `ResultadoInferenciaRegresion.valores_ajustados`, atributo que no existe. Se
  corrigió para comparar contra `ajustar_regresion_lineal`, que expone los
  valores ajustados del mismo modelo OLS.
- La validación de residuos sin variabilidad requirió una tolerancia numérica
  (`1e-12`) para evitar que un ajuste perfectamente lineal pasara por ruido de
  punto flotante.

### Correcciones humanas

No se registraron correcciones humanas durante la implementación de P-09.

### Validaciones

- `.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests`
- `.\.venv\Scripts\python.exe -m pytest -q`
- Inicio temporal de Streamlit en `http://127.0.0.1:8765`
- `git diff --check`
- `git status --short`

### Commit propuesto

```text
feat: agregar diagnostico de residuos
```

## P-10 — Integración final, pruebas completas y control de requisitos

### Objetivo

Realizar una revisión integral del dashboard para comprobar que las fases P-00 a
P-09 funcionan correctamente de manera conjunta, sin incorporar nuevos métodos
estadísticos.

### Resumen operativo del prompt

````text
Trabaja exclusivamente en la rama `feat/integracion-final`.

No realices commit, push, merge ni Pull Request.

# Fase P-10: integración final, pruebas completas y control de requisitos

## Objetivo general

Realizar una revisión integral del dashboard Volt-Ar Scooters para comprobar que
todas las funcionalidades desarrolladas entre P-00 y P-09 funcionan
correctamente de manera conjunta.

Esta fase no debe incorporar nuevos métodos estadísticos. Debe concentrarse en
integración entre módulos, consistencia estadística, actualización dinámica,
manejo de archivos válidos e inválidos, navegación completa por Streamlit,
experiencia de uso, documentación, cumplimiento de la consigna, pruebas de
regresión y detección de errores que solo aparecen al ejecutar páginas
específicas.

Antes de modificar archivos, leer `AGENTS.md`, confirmar la rama
`feat/integracion-final`, ejecutar `git status --short --branch`, verificar árbol
limpio, confirmar que la rama fue creada desde un `main` actualizado con P-09,
inspeccionar `app.py`, páginas, `src/`, tests y documentación, confirmar P-00 a
P-09 documentadas y presentar un plan breve.

Revisar Página 1 con enfoque gerencial descriptivo y muestral: carga activa,
vista previa diferenciada, tabla de contingencia, marginales, barras agrupadas,
barras apiladas, Chi-cuadrado muestral, grados de libertad, p-valor, α dinámico,
comparación neutral y ausencia de decisiones inferenciales poblacionales.

Revisar Página 1 cuantitativa: dispersión, una sola recta global, ecuación,
Pearson, R², interpretación muestral, unidades, aclaración de inferencia en
Página 2 y ausencia de hipótesis, causalidad, intervalos y diagnósticos.

Revisar Página 2: inferencia cualitativa, inferencia cuantitativa, calculadora
de predicción y validación técnica de supuestos, incluyendo hipótesis,
frecuencias esperadas, diferencias relativas, aportes, robustez, prueba t,
intervalos, predicción, residuos frente a ajustados, Q-Q Plot, histograma,
conteos de residuos estandarizados y ausencia de aprobación automática de
supuestos.

Verificar consistencia entre módulos y páginas: uso de
`st.session_state["datos_activos"]`, ausencia de lectura directa de Excel desde
páginas, uso del DataFrame completo, `head()` solo en vista previa, misma tabla
observada, mismo Chi-cuadrado, Pearson, R², pendiente, intercepto, predicción,
residuos, bandas, niveles independientes de significancia, claves de widgets
sin duplicar, p-valores invariantes ante α, estimadores invariantes ante nivel de
confianza e intervalo individual más amplio que el intervalo para la media.

Navegar realmente en Streamlit por página principal, Perfil Gerencial, Perfil
Analista, secciones cualitativas y cuantitativas, calculadora, residuos, Q-Q Plot,
histograma y expanders relevantes. Verificar ausencia de `NameError`, `KeyError`,
`AttributeError`, `ValueError` no controlado, claves duplicadas, errores de
Plotly, errores de importación y trazas técnicas visibles.

Usar al menos tres matrices válidas: semana predeterminada y dos semanas
generadas con semillas distintas. Verificar cantidad de observaciones, tabla de
contingencia, Chi-cuadrado, p-valor cualitativo, Pearson, R², pendiente,
p-valor de la pendiente, intervalos, predicción X = 24, media de residuos y
cantidad de puntos en gráficos. Confirmar que los resultados cambien cuando
cambian los datos.

Comprobar rechazo de archivos inválidos: columna faltante, columna adicional,
columna `Unnamed`, menos de 30 filas, más de 60 filas, sucursal desconocida,
nivel de fallos desconocido, valor nulo, infinito, antigüedad fuera de rango o
decimal, autonomía fuera de rango, Excel sin hoja `datos`, CSV inválido,
extensión no permitida y archivo vacío.

Agregar pruebas de integración en `tests/test_integracion_dashboard.py` o una
estructura equivalente para verificar consistencia cruzada, uso de 48 filas,
vista previa, cambio/restauración de semanas, constantes `VARIABLE_*`, ausencia
de expresiones prohibidas, ausencia de lenguaje causal y ausencia de aprobación
automática de supuestos.

Crear `docs/matriz_cumplimiento.md` con columnas: Requisito oficial,
Implementación, Archivo o módulo, Prueba asociada, Estado y Observaciones. Usar
estados Cumplido, Cumplido con observación o Pendiente.

Actualizar `README.md`, `docs/decisiones_metodologicas.md`,
`docs/registro_pruebas.md`, `docs/prompts.md` y la matriz de cumplimiento.
Conservar íntegramente P-00 a P-09. Incluir prompt completo, plan, archivos
modificados, problemas encontrados, errores corregidos, pruebas integrales,
resultados con varias semanas, pruebas de archivos inválidos, limitaciones,
validación humana y commit propuesto.

Revisar rutas locales absolutas, `.gitignore`, cachés, secretos y archivos
temporales. No eliminar archivos válidos.

Ejecutar validaciones finales: compileall, Pytest completo, Pytest de
integración, inicio y navegación real de Streamlit, detención del servidor,
`git diff --check`, `git status --short`, `git diff --stat` y `git diff`.

No realizar commit, push, merge ni Pull Request. Detenerse y esperar revisión.
````

### Prompt completo

````text
Trabaja exclusivamente en la rama `feat/integracion-final`.

No realices commit, push, merge ni Pull Request.

# Fase P-10: integración final, pruebas completas y control de requisitos

## Objetivo general

Realizar una revisión integral del dashboard Volt-Ar Scooters para comprobar que todas las funcionalidades desarrolladas entre P-00 y P-09 funcionan correctamente de manera conjunta.

Esta fase no debe incorporar nuevos métodos estadísticos.

Debe concentrarse en:

* integración entre módulos;
* consistencia estadística;
* actualización dinámica;
* manejo de archivos válidos e inválidos;
* navegación completa por Streamlit;
* experiencia de uso;
* documentación;
* cumplimiento de la consigna;
* pruebas de regresión;
* detección de errores que solo aparecen al ejecutar páginas específicas.

## Preparación obligatoria

Antes de modificar archivos:

1. Lee `AGENTS.md`.
2. Confirma que la rama activa sea:

```text
feat/integracion-final
```

3. Ejecuta:

```powershell
git status --short --branch
```

4. Verifica que el árbol de trabajo esté limpio.
5. Confirma que la rama fue creada desde un `main` actualizado que contiene P-09.
6. Inspecciona:

   * `app.py`
   * `pages/1_Perfil_Gerencial.py`
   * `pages/2_Perfil_Analista.py`
   * todos los archivos de `src/`
   * todos los tests;
   * `README.md`
   * `docs/decisiones_metodologicas.md`
   * `docs/diccionario_datos.md`
   * `docs/registro_pruebas.md`
   * `docs/prompts.md`.
7. Confirma que P-00 a P-09 estén documentadas.
8. Presenta un plan breve antes de modificar archivos.

No realices cambios hasta haber inspeccionado el estado completo del proyecto.

# 1. Revisión de la estructura funcional

Verifica que la aplicación conserve correctamente las siguientes funcionalidades.

## Página 1: Perfil gerencial

### Análisis cualitativo descriptivo y muestral

Debe contener:

* identificación del archivo activo;
* cantidad total de observaciones;
* vista previa claramente diferenciada de la base completa;
* tabla de contingencia observada;
* totales marginales;
* gráfico de barras agrupadas;
* gráfico apilado al 100 %;
* estadístico Chi-cuadrado muestral;
* grados de libertad;
* p-valor;
* deslizador de significancia;
* comparación neutral entre p-valor y α;
* aclaración de que la conclusión inferencial corresponde a Página 2.

No debe contener:

* decisión inferencial poblacional;
* “se rechaza H₀”;
* “no se rechaza H₀”;
* afirmaciones de independencia poblacional;
* afirmaciones de asociación poblacional.

### Análisis cuantitativo descriptivo y muestral

Debe contener:

* gráfico de dispersión;
* una sola recta de regresión global;
* ecuación estimada;
* coeficiente de Pearson;
* coeficiente de determinación R²;
* interpretación dinámica muestral;
* unidades de antigüedad en meses;
* unidades de autonomía en kilómetros;
* aclaración de que la inferencia corresponde a Página 2.

No debe contener:

* prueba de hipótesis;
* conclusión poblacional;
* lenguaje causal;
* intervalos inferenciales;
* diagnósticos de residuos.

## Página 2: Perfil analista

### Inferencia cualitativa

Debe contener:

* hipótesis H₀ y H₁;
* frecuencias observadas;
* frecuencias esperadas;
* diferencias relativas porcentuales;
* aportes de cada celda al Chi-cuadrado;
* estadístico Chi-cuadrado;
* grados de libertad;
* p-valor;
* nivel de significancia;
* decisión;
* conclusión contextual;
* evaluación de supuestos;
* evaluación de robustez;
* aclaración de población simulada.

### Inferencia cuantitativa

Debe contener:

* modelo poblacional;
* hipótesis para la pendiente;
* pendiente estimada;
* error estándar;
* estadístico t;
* grados de libertad n − 2;
* p-valor bilateral;
* nivel de significancia;
* decisión;
* conclusión contextual;
* intervalo para β₀;
* intervalo para β₁;
* intervalo aproximado de Fisher para ρ;
* deslizador de nivel de confianza.

### Calculadora de predicción

Debe contener:

* entrada de antigüedad;
* predicción puntual;
* intervalo de confianza para la media esperada;
* intervalo de predicción individual;
* nivel de confianza coherente con P-07;
* comparación de amplitudes;
* advertencia de extrapolación;
* nota de no recorte estadístico;
* gráfico técnico con recta y bandas.

### Validación técnica de supuestos

Debe contener:

* residuos frente a valores ajustados;
* línea horizontal en residuo cero;
* Q-Q Plot;
* histograma de residuos;
* media residual;
* desviación residual;
* conteos de residuos estandarizados;
* explicación de linealidad;
* explicación de homocedasticidad;
* explicación de normalidad;
* aclaración sobre independencia;
* ausencia de aprobación automática de los supuestos.

# 2. Consistencia entre módulos y páginas

Verifica mediante inspección y pruebas que:

1. Ambas páginas utilicen:

```python
st.session_state["datos_activos"]
```

2. No se lea directamente el Excel desde los módulos estadísticos ni desde las páginas.
3. El archivo activo sea el mismo en toda la aplicación.
4. Cambiar el archivo activo actualice todos los resultados.
5. Restaurar el archivo predeterminado restaure todos los resultados.
6. El DataFrame completo alimente los análisis, no `head(10)`.
7. `head()` se utilice únicamente en la vista previa.
8. Página 1 y Página 2 utilicen la misma tabla observada.
9. El Chi-cuadrado coincida en ambas páginas.
10. Pearson coincida entre análisis descriptivo e inferencial.
11. R² coincida entre análisis descriptivo e inferencial.
12. La pendiente e intercepto coincidan en:

    * gráfico de dispersión;
    * ecuación;
    * inferencia;
    * calculadora de predicción;
    * diagnóstico de residuos.
13. La predicción puntual coincida con:

[
\hat Y=b_0+b_1x_0
]

14. Los residuos coincidan con:

[
e_i=y_i-\hat y_i
]

15. Las bandas de predicción provengan del mismo modelo.
16. No existan modelos ajustados con configuraciones contradictorias.
17. Los niveles de significancia cualitativo y cuantitativo tengan claves independientes.
18. Los widgets de Streamlit no tengan claves duplicadas.
19. El nivel de confianza de intervalos y predicción sea coherente.
20. Cambiar α no modifique el p-valor.
21. Cambiar el nivel de confianza no modifique los estimadores puntuales.
22. El intervalo individual sea más amplio que el intervalo para la media.

# 3. Navegación real de Streamlit

No consideres suficiente que el servidor inicie.

Debes navegar y ejecutar explícitamente:

1. Página principal.
2. Página `Perfil Gerencial`.
3. Página `Perfil Analista`.
4. Sección cualitativa de Página 1.
5. Sección cuantitativa de Página 1.
6. Inferencia cualitativa de Página 2.
7. Inferencia cuantitativa de Página 2.
8. Calculadora de predicción.
9. Residuos frente a valores ajustados.
10. Q-Q Plot.
11. Histograma de residuos.
12. Todos los expanders relevantes.

Revisa que no aparezcan:

* `NameError`;
* `KeyError`;
* `AttributeError`;
* `ValueError` no controlado;
* claves duplicadas de widgets;
* errores de Plotly;
* errores de importación;
* trazas técnicas visibles para el usuario.

Revisa todas las constantes `VARIABLE_*` utilizadas por las páginas y confirma que:

* existan en `src.config`;
* estén correctamente importadas;
* no existan cadenas duplicadas innecesarias;
* no existan nombres usados sin definición.

Mantén o amplía la prueba preventiva basada en AST incorporada en P-09.

# 4. Pruebas con varias semanas válidas

Utiliza al menos tres matrices válidas:

1. Semana predeterminada.
2. Semana generada con una semilla distinta.
3. Semana generada con otra semilla distinta.

Cada matriz debe:

* contener entre 30 y 60 filas;
* tener exactamente las cuatro variables;
* respetar las categorías permitidas;
* respetar los rangos numéricos;
* contener variabilidad suficiente en X e Y;
* permitir ejecutar todos los análisis.

Verifica para cada semana:

* cantidad de observaciones;
* tabla de contingencia;
* Chi-cuadrado;
* p-valor cualitativo;
* Pearson;
* R²;
* pendiente;
* p-valor de la pendiente;
* intervalos;
* predicción para X = 24;
* media de residuos;
* cantidad de puntos en los gráficos.

Confirma que los resultados cambien cuando cambian los datos.

No deben quedar valores almacenados de una semana anterior.

No es obligatorio conservar los Excel adicionales. Si se conservan, deben ubicarse claramente como datos de demostración y documentarse.

# 5. Pruebas con archivos inválidos

Comprueba que se rechacen correctamente:

1. Archivo con una columna faltante.
2. Archivo con una columna adicional.
3. Archivo con columna `Unnamed`.
4. Archivo con menos de 30 filas.
5. Archivo con más de 60 filas.
6. Categoría de sucursal desconocida.
7. Categoría de nivel de fallos desconocida.
8. Valor nulo.
9. Valor infinito.
10. Antigüedad menor que 1.
11. Antigüedad mayor que 48.
12. Antigüedad decimal no entera.
13. Autonomía menor que 15.
14. Autonomía mayor que 45.
15. Excel sin hoja `datos`.
16. CSV con estructura inválida.
17. Extensión no permitida.
18. Archivo vacío.

En todos los casos:

* mostrar un mensaje comprensible;
* no mostrar una traza técnica;
* conservar el último conjunto válido activo;
* no reemplazar `st.session_state["datos_activos"]`.

# 6. Pruebas estadísticas cruzadas

Agrega un archivo de pruebas de integración, por ejemplo:

```text
tests/test_integracion_dashboard.py
```

o amplía la estructura existente si resulta más coherente.

Debe verificar como mínimo:

1. Tabla observada común entre módulos.
2. Chi-cuadrado común entre Página 1 y Página 2.
3. Pearson común entre descripción e inferencia.
4. R² común entre descripción e inferencia.
5. Intercepto y pendiente comunes.
6. Predicción puntual coincidente con la ecuación.
7. Residuos coincidentes con observado menos ajustado.
8. Intervalo individual más amplio que el de la media.
9. P-valor independiente de α.
10. Intervalos más amplios al aumentar la confianza.
11. Estimadores invariantes ante el nivel de confianza.
12. Uso de las 48 filas completas del archivo predeterminado.
13. La vista previa no modifica los datos activos.
14. Los resultados cambian con otra semana.
15. Restaurar los datos predeterminados devuelve los resultados originales.
16. Los nombres `VARIABLE_*` usados por ambas páginas existen y están importados.
17. No existen expresiones prohibidas en Página 1.
18. No se utiliza “se acepta H₀”.
19. No aparece lenguaje causal.
20. No se aprueban automáticamente los supuestos.

Evita pruebas frágiles basadas en posiciones visuales internas de Streamlit.

# 7. Revisión visual y de experiencia de uso

Revisa:

* títulos consistentes;
* terminología en español;
* ortografía;
* acentos;
* decimales razonables;
* uso de coma o punto decimal consistente;
* unidades visibles;
* tablas legibles;
* gráficos con título;
* ejes correctamente identificados;
* tooltips comprensibles;
* leyendas correctas;
* ausencia de textos duplicados;
* ausencia de contenido técnico excesivo abierto por defecto;
* uso de expanders para información complementaria;
* mensajes de error comprensibles;
* ausencia de trazas técnicas.

Verifica especialmente:

* “muestra” y “muestral” en Página 1;
* “inferencia” y “población simulada” en Página 2;
* diferencia entre asociación y causalidad;
* diferencia entre IC de la media e intervalo individual;
* diferencia entre interpolación y extrapolación;
* diferencia entre p-valor y α;
* diferencia entre nivel de confianza y nivel de significancia;
* normalidad referida a los residuos;
* independencia referida al diseño de recolección.

No realices un rediseño visual completo.

No agregues CSS complejo salvo que sea estrictamente necesario para resolver un problema concreto.

# 8. Rendimiento y reutilización

Revisa que:

* no existan lecturas repetidas del Excel;
* no se duplique lógica estadística;
* no se copie código entre páginas;
* las funciones estadísticas sean puras cuando sea posible;
* se reutilicen estructuras ya existentes;
* no se ajuste innecesariamente el mismo modelo varias veces dentro de una misma función;
* no se guarden resultados obsoletos al cambiar de archivo.

Puedes utilizar `st.cache_data` únicamente si:

* la función es pura;
* el DataFrame participa correctamente en la clave;
* no se conservan resultados de semanas anteriores;
* existe una mejora justificada.

No optimices prematuramente.

# 9. Matriz de cumplimiento

Crea:

```text
docs/matriz_cumplimiento.md
```

Debe contener una tabla con estas columnas:

| Requisito oficial | Implementación | Archivo o módulo | Prueba asociada | Estado | Observaciones |

Incluye como mínimo:

* cantidad de observaciones;
* cuatro variables;
* variable cualitativa nominal;
* variable cualitativa ordinal;
* dos variables cuantitativas;
* correlación lógica intencional;
* carga semanal;
* Excel y CSV;
* Página 1;
* Página 2;
* tabla de contingencia;
* marginales;
* barras agrupadas;
* barras apiladas;
* Chi-cuadrado;
* α dinámico;
* frecuencias esperadas;
* diferencias relativas;
* robustez;
* dispersión;
* recta de regresión;
* Pearson;
* R²;
* prueba de pendiente;
* intervalos de parámetros;
* predicción puntual;
* intervalo para la media;
* intervalo individual;
* residuos frente a ajustados;
* Q-Q Plot;
* histograma;
* uso documentado de IA;
* registro de prompts;
* validación humana;
* pruebas automatizadas.

El estado debe ser uno de:

* Cumplido.
* Cumplido con observación.
* Pendiente.

No marques requisitos como cumplidos sin evidencia concreta.

# 10. Documentación final

Actualiza:

* `README.md`
* `docs/decisiones_metodologicas.md`
* `docs/registro_pruebas.md`
* `docs/prompts.md`
* `docs/matriz_cumplimiento.md`

Conserva íntegramente P-00 a P-09.

Agrega P-10 con:

* prompt completo;
* plan;
* archivos modificados;
* problemas encontrados;
* errores corregidos;
* pruebas integrales;
* resultados con varias semanas;
* pruebas de archivos inválidos;
* matriz de cumplimiento;
* limitaciones;
* validación humana;
* commit propuesto.

## README

Debe incluir claramente:

1. Descripción del proyecto.
2. Objetivos.
3. Variables analizadas.
4. Requisitos de Python.
5. Creación del entorno virtual.
6. Instalación de dependencias.
7. Ejecución de Streamlit.
8. Generación de datos.
9. Carga semanal.
10. Formato esperado del Excel y CSV.
11. Estructura de páginas.
12. Funcionalidades estadísticas.
13. Ejecución de pruebas.
14. Estructura de carpetas.
15. Limitaciones.
16. Uso de inteligencia artificial.
17. Validación humana de resultados.

No incluyas credenciales, rutas locales absolutas ni información específica del equipo del desarrollador.

# 11. Control de rutas y portabilidad

Busca y elimina de la documentación o código cualquier ruta local absoluta como:

```text
C:\Users\lucas\...
```

La aplicación debe utilizar rutas relativas o construidas con `pathlib`.

Verifica que no se hayan versionado accidentalmente:

* `.venv/`
* `__pycache__/`
* `.pytest_cache/`
* archivos temporales;
* capturas no solicitadas;
* archivos de OneDrive;
* archivos de configuración del editor;
* logs;
* archivos con secretos.

Revisa `.gitignore`.

No elimines archivos válidos del proyecto.

# 12. Validaciones finales obligatorias

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests
```

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Ejecuta además las pruebas de integración por separado:

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests/test_integracion_dashboard.py
```

Adapta el comando si utilizas otro nombre de archivo.

Inicia Streamlit:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.headless=true --server.address=127.0.0.1 --server.port=8765 --server.runOnSave=false
```

No te limites a comprobar el inicio.

Navega explícitamente por:

* Página principal.
* Perfil Gerencial.
* Perfil Analista.
* Gráfico cualitativo.
* Gráfico cuantitativo.
* Inferencia cualitativa.
* Inferencia cuantitativa.
* Calculadora.
* Gráfico de residuos.
* Q-Q Plot.
* Histograma.

Detén el servidor y confirma que el puerto quede libre.

Ejecuta:

```powershell
git diff --check
git status --short
```

Revisa también:

```powershell
git diff --stat
git diff
```

# 13. Restricciones

No hagas:

* commit;
* push;
* merge;
* Pull Request;
* cambios de rama;
* nuevos métodos estadísticos;
* reestructuración general innecesaria;
* rediseño completo;
* eliminación de documentación anterior;
* modificación de datos predeterminados sin una razón real;
* cambios silenciosos en fórmulas;
* conclusiones causales;
* aprobación automática de supuestos.

Si detectas un error estadístico real, corrígelo y documéntalo explícitamente.

Si detectas una ambigüedad metodológica, no la ocultes: documéntala.

# 14. Informe final

Al terminar reporta:

1. Rama confirmada.
2. Plan aplicado.
3. Archivos creados.
4. Archivos modificados.
5. Problemas encontrados.
6. Correcciones realizadas.
7. Cantidad total de pruebas aprobadas.
8. Resultado de las pruebas de integración.
9. Resultados de las tres semanas.
10. Resultados de archivos inválidos.
11. Consistencia entre páginas.
12. Resultado de la navegación real de Streamlit.
13. Requisitos cumplidos.
14. Requisitos cumplidos con observación.
15. Requisitos pendientes.
16. Limitaciones documentadas.
17. Resultado de `git diff --check`.
18. Estado final de Git.
19. Mensaje de commit propuesto.

El mensaje de commit propuesto puede ser:

```text
chore: completar integracion y control de calidad
```

No realices el commit.

Detente y espera mi revisión.
````

### Plan aplicado

1. Se verificó rama, estado limpio, historial de `main` con P-09 y documentación
   P-00 a P-09.
2. Se inspeccionaron páginas, módulos `src/`, tests y documentación.
3. Se corrigieron textos obsoletos de integración en `app.py` y Página 1.
4. Se agregó `tests/test_integracion_dashboard.py`.
5. Se calcularon métricas reales para semanas con semillas 42, 7 y 123.
6. Se creó `docs/matriz_cumplimiento.md`.
7. Se actualizaron README, decisiones metodológicas, registro de pruebas y este
   registro de prompts.
8. Se ejecutarán las validaciones finales antes del cierre de la fase.

### Archivos creados o modificados

- `app.py`
- `pages/1_Perfil_Gerencial.py`
- `tests/test_integracion_dashboard.py`
- `README.md`
- `docs/decisiones_metodologicas.md`
- `docs/registro_pruebas.md`
- `docs/prompts.md`
- `docs/matriz_cumplimiento.md`

### Problemas encontrados

- La portada conservaba texto de fase inicial que indicaba que los módulos
  estadísticos se implementarían en fases posteriores.
- Una nota de Página 1 indicaba en futuro que la conclusión inferencial se
  presentaría en Página 2.
- El primer fixture para el caso inválido de valor nulo en la prueba de
  integración usaba una máscara de Pandas con forma incorrecta. Se corrigió el
  fixture sin modificar la aplicación.

### Resultados con varias semanas

| Semilla | Chi-cuadrado | p Chi-cuadrado | Pearson | R² | Pendiente | p pendiente | Predicción X=24 | `|r est.| > 2` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 42 | 19.170279 | 0.000068742747 | -0.900523 | 0.810942 | -0.552768 | 2.97371341074e-18 | 31.899632 | 1 |
| 7 | 19.047619 | 0.000073090693 | -0.920086 | 0.846558 | -0.518881 | 2.39587404239e-20 | 31.625117 | 2 |
| 123 | 13.945455 | 0.000937093707 | -0.920721 | 0.847728 | -0.568801 | 2.00789672304e-20 | 32.999408 | 3 |

### Pruebas de archivos inválidos

Se verificó rechazo de 18 casos inválidos: columnas faltantes, adicionales,
`Unnamed`, cantidades fuera del rango 30-60, categorías desconocidas, valores
nulos, infinitos, rangos numéricos inválidos, Excel sin hoja `datos`, CSV
inválido, extensión no permitida y archivo vacío.

### Validaciones

- `.\.venv\Scripts\python.exe -m compileall -q app.py pages src tests`
- `.\.venv\Scripts\python.exe -m pytest -q`
- `.\.venv\Scripts\python.exe -m pytest -q tests/test_integracion_dashboard.py`
- Inicio temporal y navegación de Streamlit
- `git diff --check`
- `git status --short`
- `git diff --stat`
- `git diff`

### Commit propuesto

```text
chore: completar integracion y control de calidad
```

## Plantilla para próximos registros

## P-XX — Nombre de la intervención

- Fecha:
- Herramienta:
- Etapa:
- Objetivo:
- Archivos creados o modificados:
- Resultado:
- Problemas encontrados:
- Correcciones humanas:
- Validaciones ejecutadas:
- Resultado de las pruebas:
- Commit relacionado:

### Prompt completo

```text
Pegar aquí el prompt literal.
```

### Respuesta relevante de la IA

```text
Pegar aquí el resumen o los fragmentos relevantes.
```

### Evaluación de los integrantes

Explicar qué se aceptó, qué se corrigió y cómo se comprobó.
