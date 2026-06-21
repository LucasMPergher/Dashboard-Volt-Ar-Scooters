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
