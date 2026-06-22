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
