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
