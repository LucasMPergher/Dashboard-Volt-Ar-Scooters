# Decisiones metodológicas

- Unidad de análisis: un monopatín eléctrico.
- Población: monopatines de Volt-Ar Scooters de Rosario y Córdoba.
- Muestra semanal simulada: entre 30 y 60 monopatines.
- Asociación cualitativa: `Sucursal` y `Nivel_Fallos`.
- Relación cuantitativa: `Antiguedad_Bateria_Meses` y `Autonomia_Real_Km`.
- Relación cuantitativa esperada: negativa, lógica y no perfecta.
- Prueba cualitativa prevista: Chi-cuadrado de independencia.
- Modelo cuantitativo previsto: regresión lineal simple.

## Fase P-02: simulación de datos

- Cantidad predeterminada: 48 observaciones. Se eligió porque queda dentro del
  rango solicitado, permite balancear 24 monopatines por sucursal y ofrece una
  base suficiente para controles técnicos iniciales.
- Balance entre sucursales: se construye una lista con cantidades iguales para
  muestras pares. Para muestras impares, la diferencia entre sucursales no supera
  una observación. Luego la lista se mezcla con el generador aleatorio.
- Reproducibilidad: se utiliza `numpy.random.default_rng(semilla)` con semilla
  predeterminada 42, sin depender del estado aleatorio global de NumPy.
- Probabilidades condicionales de `Nivel_Fallos`:
  - Rosario: Bajo 0.20, Medio 0.35, Alto 0.45.
  - Córdoba: Bajo 0.55, Medio 0.35, Alto 0.10.
- Antigüedad de batería: se genera como entero entre 1 y 48 meses y no depende
  directamente de `Nivel_Fallos`.
- Fórmula generadora de autonomía:
  `Autonomia_Real_Km = 45 - 0.52 * Antiguedad_Bateria_Meses + error_aleatorio`.
- Error aleatorio: proviene de una distribución normal con media 0 y desviación
  estándar 4.0. Se incorpora para evitar una correlación perfecta y representar
  variabilidad operativa.
- Rango de autonomía: los valores se limitan entre 15 y 45 kilómetros y se
  redondean a dos decimales.
- Control de límites: para el archivo predeterminado se contabilizan las
  observaciones exactamente iguales a 15 y 45 km. La concentración observada no
  se consideró excesiva, por lo que no se ajustó la dispersión.
- Semana: se representa mediante el nombre del archivo, por ejemplo
  `volt_ar_semana_01.xlsx`, y no como una quinta variable estadística.

## Fase P-03: carga y validación semanal

- Formatos admitidos: `.xlsx` y `.csv`.
- Excel: se exige la hoja `datos`. Si la hoja no existe, se informa el listado de
  hojas encontradas y no se selecciona otra hoja automáticamente.
- CSV: se lee como UTF-8 y se permite detección de separador coma o punto y coma
  cuando Pandas puede interpretarlo.
- Estructura: se exigen exactamente las cuatro variables estadísticas. Si están
  en otro orden pero el conjunto es correcto, se reordenan al orden canónico.
- Columnas rechazadas: faltantes, adicionales y columnas `Unnamed`.
- Cantidad de filas: se mantiene el rango metodológico de 30 a 60 observaciones.
- Categorías cualitativas: se eliminan espacios y se normalizan diferencias de
  mayúsculas y minúsculas sin corregir nombres desconocidos.
- Variables numéricas: la antigüedad debe convertirse a entero sin decimales no
  enteros; la autonomía debe convertirse a número real. No se aceptan infinitos.
- Valores nulos: no se permiten en ninguna columna.
- Duplicados: no se eliminan, porque sin identificador dos monopatines pueden
  compartir los mismos valores observados.
- Archivo predeterminado: `data/volt_ar_semana_01.xlsx` se carga cuando todavía
  no existe una actualización válida cargada por el usuario.
- Estado activo: la aplicación guarda el DataFrame validado en
  `st.session_state["datos_activos"]` y el nombre del archivo en
  `st.session_state["nombre_archivo_activo"]`.
- Errores: si un archivo nuevo es inválido, se muestra un mensaje comprensible y
  no se reemplazan los datos activos.
- Alcance: esta fase no aplica pruebas estadísticas, gráficos, correlación,
  regresión ni conclusiones inferenciales.

## Fase P-04: módulo cualitativo gerencial

- Enfoque de la Página 1: descriptivo y muestral. La página resume la muestra
  semanal activa sin formular conclusiones inferenciales sobre la población.
- Variables analizadas: `Sucursal` en filas y `Nivel_Fallos` en columnas.
- Orden de categorías: Rosario, Córdoba para `Sucursal`; Bajo, Medio, Alto para
  `Nivel_Fallos`.
- Tabla visual: se muestran totales marginales de filas y columnas para lectura
  gerencial.
- Cálculo Chi-cuadrado: los marginales no forman parte de la tabla enviada a
  `scipy.stats.chi2_contingency`.
- Configuración del cálculo: se utiliza `correction=False`, sin corrección de
  Yates, sobre la tabla efectiva observada.
- Categorías ausentes: se conservan en la tabla descriptiva con frecuencia cero,
  pero se eliminan únicamente para el cálculo si su total marginal es cero.
- Condición mínima: para calcular Chi-cuadrado deben existir al menos dos
  categorías observadas en cada variable.
- Nivel de significancia: el deslizador cambia solo la comparación visual con
  α. El p-valor se calcula exclusivamente desde los datos y no cambia con α.
- Página 1: puede mostrar estadístico, grados de libertad y p-valor por
  consigna, pero no muestra decisión inferencial. La conclusión formal queda
  reservada para la Página 2.

## Fase P-05: módulo cuantitativo gerencial

- Enfoque de la Página 1: descriptivo y muestral. El módulo cuantitativo resume
  la relación observada en la semana activa sin extender la conclusión a toda la
  población.
- Variable independiente X: `Antiguedad_Bateria_Meses`.
- Variable dependiente Y: `Autonomia_Real_Km`.
- Modelo utilizado: regresión lineal simple con intercepto, ajustada con
  `statsmodels` para poder reutilizar el resultado en la Página 2.
- Pendiente: representa el cambio promedio muestral en la autonomía real, en
  kilómetros, asociado a un mes adicional de antigüedad de batería dentro de la
  recta ajustada.
- Intercepto: representa el valor de la recta cuando la antigüedad es cero
  meses. Se usa como parámetro técnico del modelo y no como observación real de
  la muestra.
- Pearson: se interpreta como medida descriptiva de dirección e intensidad
  lineal en la muestra semanal, no como prueba de hipótesis.
- Criterio heurístico de intensidad de `|r|`: menor que 0,20 muy débil; desde
  0,20 y menor que 0,40 débil; desde 0,40 y menor que 0,60 moderada; desde 0,60
  y menor que 0,80 fuerte; desde 0,80 hasta 1 muy fuerte.
- R²: se interpreta como porcentaje de variabilidad observada en la autonomía
  que queda explicada descriptivamente por el modelo lineal con la antigüedad.
- En regresión lineal simple con intercepto se controla que R² coincida
  aproximadamente con el cuadrado del coeficiente de Pearson.
- Asociación y causalidad: la relación negativa observada no se presenta como
  causalidad. La Página 1 evita expresiones como que X causa Y.
- Muestra e inferencia: la Página 1 puede mostrar coeficientes muestrales, pero
  no hipótesis, estadístico t, intervalos, predicciones ni conclusiones
  poblacionales.
- Coherencia visual: la recta del gráfico se construye con el mismo intercepto
  y la misma pendiente que alimentan los indicadores KPI.
- Residuos: se calculan internamente para verificación y reutilización
  posterior, pero no se muestran todavía en la interfaz gerencial.

## Fase P-06: inferencia cualitativa

- Enfoque de la Página 2: inferencial y poblacional. La prueba se interpreta en
  el escenario poblacional simulado con fines académicos.
- Variables analizadas: `Sucursal` y `Nivel_Fallos`.
- Prueba utilizada: Chi-cuadrado de independencia, porque se dispone de una
  muestra semanal y dos variables cualitativas observadas conjuntamente en cada
  monopatín.
- Hipótesis nula: la sucursal y el nivel de fallos técnicos son independientes
  en la población de monopatines de Volt-Ar Scooters.
- Hipótesis alternativa: la sucursal y el nivel de fallos técnicos no son
  independientes; existe asociación entre ambas variables en la población.
- Configuración del cálculo: `scipy.stats.chi2_contingency` con
  `correction=False`. Los marginales no se incluyen en la prueba.
- Frecuencias esperadas: se calculan con la fórmula
  `Eij = total_fila_i * total_columna_j / N`, manteniendo etiquetas y orden de
  la tabla observada efectiva.
- Categorías ausentes: se excluyen del cálculo únicamente las filas o columnas
  cuyo total observado es cero. No se inventan frecuencias.
- Frecuencias diferenciales relativas: dado que el material disponible no
  presenta una definición operacional explícita con ese nombre, el proyecto
  adopta la convención `(O - E) / E`. En la interfaz se muestra como porcentaje:
  `(O - E) / E * 100`.
- Diferencias relativas: valores positivos indican frecuencias observadas
  superiores a las esperadas bajo independencia; valores negativos indican
  frecuencias inferiores; valores cercanos a cero indican proximidad entre
  observadas y esperadas.
- Aportes por celda: se calculan como `(O - E)^2 / E`. La suma de los aportes
  coincide con el estadístico Chi-cuadrado.
- Nivel de significancia: el deslizador cambia la decisión, pero no modifica el
  p-valor.
- Regla de decisión: si `p-valor < α`, se rechaza H0; si `p-valor >= α`, no se
  rechaza H0. No se utiliza la expresión "se acepta H0".
- Conclusión contextual: cuando se rechaza H0 se informa evidencia
  estadísticamente significativa de asociación; cuando no se rechaza H0 se
  indica que los datos disponibles no proporcionan evidencia suficiente, sin
  afirmar independencia definitiva.
- Independencia de observaciones: no puede verificarse únicamente con la matriz.
  Se presenta como supuesto dependiente del diseño de recolección.
- Categorías mutuamente excluyentes: se consideran respaldadas por la estructura
  validada de datos.
- Robustez: la aproximación Chi-cuadrado se considera robusta solo si ninguna
  frecuencia esperada es menor que 1 y al menos el 80 % de las esperadas es
  mayor o igual que 5.
- Si no se cumplen los criterios de robustez, el cálculo no se bloquea, pero la
  interfaz advierte que la aproximación debe interpretarse con precaución.

## Fase P-07: inferencia cuantitativa

- Enfoque de la Página 2: inferencial y poblacional para la relación lineal
  entre `Antiguedad_Bateria_Meses` y `Autonomia_Real_Km`.
- Modelo poblacional: `Y = β₀ + β₁X + ε`, con intercepto poblacional `β₀` y
  pendiente poblacional `β₁`.
- Pendiente muestral y poblacional: la pendiente estimada `b₁` resume la muestra
  activa; la prueba evalúa si la pendiente poblacional `β₁` puede considerarse
  distinta de cero.
- Prueba de hipótesis: bilateral, con `H0: β₁ = 0` y `H1: β₁ != 0`.
- Estadístico t: se calcula como `b₁ / SE(b₁)` usando la salida de
  `statsmodels`. Se verifica también la equivalencia
  `t = r * sqrt(n - 2) / sqrt(1 - r^2)` en regresión lineal simple.
- Grados de libertad: `gl = n - 2`, porque se estiman intercepto y pendiente.
- Relación con la correlación: en regresión lineal simple con intercepto, la
  prueba para `β₁ = 0` es equivalente a la prueba para correlación lineal nula.
- Nivel de significancia: `α` controla la regla de decisión. El p-valor se
  calcula desde el modelo y no cambia al modificar `α`.
- Regla de decisión: si `p < α`, se rechaza H0; si `p >= α`, no se rechaza H0.
  No se utiliza la expresión "se acepta H0".
- Conclusión contextual: se informa evidencia de relación lineal poblacional
  positiva o negativa según el signo de la pendiente. No se afirma causalidad.
- Nivel de confianza: controla únicamente los límites de los intervalos de
  confianza para `β₀`, `β₁` y `ρ`; no modifica estimadores, estadístico t ni
  p-valor.
- Intervalos: al aumentar el nivel de confianza, los intervalos se amplían
  porque se utiliza un valor crítico más exigente.
- Intervalos de parámetros: se calculan con `modelo.conf_int(alpha=1 -
  nivel_confianza)`.
- Intervalo de correlación: se calcula como complemento mediante la
  aproximación de Fisher, usando `atanh(r)`, `1 / sqrt(n - 3)` y transformación
  inversa con `tanh`.
- Intervalo de Fisher: solo se calcula con `n > 3` y correlación no perfecta. Si
  `r = 1` o `r = -1`, se informa de forma controlada que no se calcula.
- Alcance pendiente: no se implementan todavía calculadora de predicción,
  intervalos para la media esperada de Y, intervalos de predicción individual,
  gráfico de residuos, Q-Q Plot ni histograma de residuos.
- Escenario: las conclusiones corresponden al escenario poblacional simulado con
  fines académicos.

## Fase P-08: calculadora de predicción

- Enfoque: herramienta técnica de Página 2 para estimar autonomía a partir de
  una antigüedad de batería ingresada por el analista.
- Modelo utilizado: el mismo modelo OLS con intercepto empleado en P-05 y P-07.
  No se ajusta una segunda regresión.
- Variable de entrada: `Antiguedad_Bateria_Meses`, tratada como valor entero en
  la interfaz porque la medición se registra en meses completos.
- Rango operativo de entrada: de 1 a 48 meses. Los valores dentro de ese rango
  se permiten aunque queden fuera del rango observado en la muestra.
- Interpolación: ocurre cuando el valor ingresado está entre el mínimo y el
  máximo observados de X en la muestra activa.
- Extrapolación: ocurre cuando el valor ingresado está dentro del rango
  operativo, pero fuera del rango observado. Se permite el cálculo y se muestra
  una advertencia de cautela.
- Predicción puntual: corresponde a `b0 + b1 * x0` y no cambia al modificar el
  nivel de confianza.
- Intervalo para la media esperada: estima la autonomía promedio esperada de
  todos los monopatines con antigüedad `x0`.
- Intervalo de predicción individual: estima la autonomía de un monopatín
  individual con antigüedad `x0`.
- Amplitud: el intervalo individual es al menos tan amplio como el intervalo
  para la media porque combina incertidumbre sobre la media estimada y
  variabilidad individual alrededor de la recta.
- Nivel de confianza: al aumentar la confianza, se amplían tanto el intervalo
  para la media como el intervalo individual; la predicción puntual no cambia.
- Implementación: se utiliza `modelo.get_prediction(...).summary_frame(alpha=1 -
  nivel_confianza)` de Statsmodels.
- Asignación de intervalos: `mean_ci_lower` y `mean_ci_upper` alimentan el
  intervalo para la media; `obs_ci_lower` y `obs_ci_upper` alimentan el
  intervalo individual.
- Límites físicos: no se recortan automáticamente la predicción ni los
  intervalos al rango operativo 15-45 km. Si un límite queda fuera de ese rango,
  se informa que el resultado se conserva sin recorte para no alterar el modelo.
- Alcance de P-08: la calculadora no incorporaba todavía diagnósticos del
  modelo ni pruebas adicionales de normalidad u homocedasticidad. Esos elementos
  se agregan en P-09.
- Ausencia de causalidad: la calculadora estima valores bajo el modelo lineal,
  pero no afirma que la antigüedad cause cambios en la autonomía.

## Fase P-09: diagnóstico de residuos y validación técnica de supuestos

- Enfoque: validación técnica del mismo modelo OLS con intercepto utilizado en
  P-05, P-07 y P-08. No se ajusta un modelo alternativo.
- Fuente de datos: el diagnóstico usa el DataFrame activo en Streamlit
  (`st.session_state["datos_activos"]`) y se actualiza cuando cambia el archivo
  semanal cargado.
- Definición de residuo: `e_i = y_i - y_hat_i`, donde `y_i` es la autonomía
  observada y `y_hat_i` es la autonomía ajustada por el modelo lineal.
- Residuos estandarizados: se calculan con la influencia de Statsmodels mediante
  `modelo.get_influence().resid_studentized_internal`.
- Criterios orientativos: se informan conteos de observaciones con
  `|residuo estandarizado| > 2` y `|residuo estandarizado| > 3`. Estos umbrales
  son ayudas diagnósticas; no eliminan observaciones ni prueban por sí solos que
  un dato sea erróneo.
- Linealidad: el gráfico de residuos frente a valores ajustados permite observar
  si aparecen patrones curvos o sistemáticos alrededor de cero.
- Homocedasticidad: el mismo gráfico permite revisar si la dispersión de los
  residuos se mantiene aproximadamente constante a lo largo de los valores
  ajustados. Una forma de embudo puede sugerir heterocedasticidad.
- Normalidad: el supuesto relevante corresponde a los errores o residuos del
  modelo, no necesariamente a la distribución marginal de X o de Y.
- Q-Q Plot: se construye con `scipy.stats.probplot` y se utiliza como herramienta
  principal para evaluar compatibilidad visual con normalidad de residuos.
- Histograma: se presenta como complemento del Q-Q Plot y no lo sustituye.
- Independencia: no puede validarse completamente con estos gráficos. Depende del
  diseño de recolección; se asume que cada fila corresponde a un monopatín
  distinto y que las observaciones no dependen entre sí.
- Decisión interpretativa: los gráficos no producen automáticamente una
  aprobación ni invalidación del modelo. La evaluación requiere revisar patrones,
  contexto, tamaño muestral y supuestos de recolección.

### Corrección posterior a la revisión manual

- Durante la navegación manual a la sección "Residuos frente a valores
  ajustados" se detectó un `NameError`.
- La página utilizaba `VARIABLE_SUCURSAL` y `VARIABLE_NIVEL_FALLOS` en el
  tooltip del gráfico de residuos, pero no las importaba desde `src.config`.
- El inicio del servidor Streamlit no había detectado el problema porque la
  página específica todavía no había sido ejecutada mediante navegación.
- Se agregaron ambos imports canónicos desde `src.config`, sin crear constantes
  duplicadas.
- No se modificaron cálculos, residuos, gráficos ni resultados estadísticos.
- Se agregó el test `test_pagina_analista_importa_constantes_variables_usadas`,
  basado en AST, para verificar que las constantes `VARIABLE_*` utilizadas por
  la página existan y sean importadas desde `src.config`.
- Luego de la corrección aprobaron 204 pruebas.
- Se navegó explícitamente a `Perfil Analista` y el gráfico de residuos se
  renderizó sin `NameError`.
