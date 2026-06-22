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
