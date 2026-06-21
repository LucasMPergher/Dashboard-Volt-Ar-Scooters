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
