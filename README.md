# Dynamic Events 🚀

> Planificador dinámico de tareas y recursos. Crea eventos, reserva CPU/GPU/RAM y detecta colisiones antes de que sucedan.


## 📚 Tabla de contenidos

- [Visión general](#-visión-general)
- [Características clave](#-características-clave)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Ejecución](#-ejecución)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Módulos principales](#-módulos-principales)
- [Pruebas y utilidades](#-pruebas-y-utilidades)
- [Archivos de configuración](#-archivos-de-configuración)
- [Próximos pasos](#-próximos-pasos)

---

## 🌐 Visión general

Dynamic Events es una plataforma ligera para experimentar con planificación de recursos. Define tareas con necesidades de hardware, prográmalas en un calendario compartido y detecta conflictos con una GUI construida con CustomTkinter o desde la consola.

Ideal para: laboratorios de automatización, ensayos de carga y pruebas de orquestación.

---

## ✨ Características clave

- Interface gráfica CustomTkinter con listas de eventos y recursos.
- Consola interactiva para carga, edición y guardado del calendario.
- Motor `Calendar` con verificación de colisiones y persistencia en JSON.
- Helpers para importar definiciones desde `tasks.json` y `resources.json`.
- Base para extender hacia una versión web (`modules/webapp.py`).

---

## 🛠️ Requisitos

- Python 3.10 o superior (verificado en 3.11 y 3.12)
- `pip`
- (Recomendado) entorno virtual `venv`
- Dependencias listadas en `requirements.txt`

---

## 📦 Instalación

```bash
# 1. Clonar o descargar el repositorio
git clone https://github.com/<tu-usuario>/dinamic-events.git
cd dinamic-events

# 2. Crear y activar un entorno virtual (opcional, pero sugerido)
python -m venv .venv
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

> 💡 `requirements.txt` incluye `customtkinter` y las librerías usadas por la GUI.

---

## ▶️ Ejecución

```bash
# Lanzar la GUI principal (interfaz gráfica en `main.py`)
python main.py

# Usar la interfaz/menú de consola (si existe una alternativa de consola)
# (nota: en este repo actual la entrada gráfica principal es `main.py`)

# Ejecutar el script de apoyo (Linux/macOS)
bash run.sh
```

> 🔁 Reinicia la app tras editar `templates/tasks.json` o `templates/resources.json` para recargar la configuración.
>
> ⚠️ Nota: `run.sh` actualmente ejecuta `dinev.py` y `testfile.py` — si esos archivos los renombraste a `main.py` o a otros nombres, actualiza `run.sh` o mantenlo como helper según prefieras.

---

## 🗂️ Estructura del proyecto

```
dinamic-events/
├─ main.py                # Entrada GUI principal (CustomTkinter wrappers)
├─ run.sh
├─ clean.sh
├─ requirements.txt
├─ runtests.py
├─ changelog
├─ logs.txt
├─ project.md
├─ saved/                 # Estado en tiempo de ejecución (eventos / recursos usados)
│  ├─ actives_events.json
│  └─ used_resources.json
├─ modules/
│  ├─ calendar.py
│  ├─ console_utils.py
│  ├─ events.py
│  ├─ gvar.py
│  ├─ handlers.py
│  ├─ utils.py
│  ├─ webapp.py
│  └─ gui_core/
│     ├─ customGUI.py
│     ├─ TaskCreator.py
│     └─ TaskRemover.py
├─ templates/
│  ├─ resources.json
│  ├─ sample.json
│  └─ tasks.json
└─ tests/
   ├─ test1.py
   ├─ test2.py
   └─ test3.py
```

---

## 🧭 Módulos principales

| Módulo | Rol principal |
| --- | --- |
| `modules/calendar.py` | Implementa `Calendar`, orquesta eventos, recursos usados y persistencia. |
| `modules/events.py` | Define la clase `event`, normaliza datos y detecta incompatibilidades. |
| `modules/handlers.py` | Carga y guarda JSON de tareas, recursos y eventos. |
| `modules/console_utils.py` | Menú de consola para gestionar el calendario sin GUI. |
| `modules/gui_core/customGUI.py` | Widgets auxiliares y estilos para la interfaz CustomTkinter. |
| `modules/gui_core/TaskCreator.py` / `TaskRemover.py` | Ventanas auxiliares para crear / eliminar tareas desde la GUI. |
| `modules/gvar.py` | Variables globales, calendario compartido y bootstrap de datos. |
| `modules/utils.py` | Helpers generales (conversión de tiempo, manejo de diccionarios, etc.). |
| `modules/webapp.py` | Punto de partida para exponer la lógica vía web. |

---

## 🧪 Pruebas y utilidades

- `python runtests.py`: ejecuta los tests definidos en `tests/`.
- `tests/test1.py`, `tests/test2.py`, `tests/test3.py`: casos de ejemplo para carga/guardado y estrés.

> ✅ Ejecuta `python runtests.py` tras refactorizar los módulos de planificación.

---

## 🗃️ Archivos de configuración

- `templates/tasks.json`: definición de tareas con sus requisitos.
- `templates/resources.json`: inventario de recursos disponibles.
- `templates/sample.json`: plantilla con datos de ejemplo.

> ℹ️ Los eventos activos y el estado runtime se guardan en `saved/actives_events.json` y `saved/used_resources.json`.

---

## 🔮 Próximos pasos

1. Añadir más ejemplos o casos de uso en `templates/`.
2. Ampliar la suite de tests para el motor `Calendar`.
3. Dockerizar el proyecto si necesitas deployar rápidamente.

---

¿Te gustaría que avancemos con alguno de estos puntos? ¡Estoy listo! ✨
