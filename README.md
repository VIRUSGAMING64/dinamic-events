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

## Dynamic Events — Planificador dinámico de tareas y recursos 🚀

Dynamic Events es un proyecto ligero para modelar y probar la planificación de tareas que consumen recursos compartidos (CPU, GPU, RAM u otros). Permite definir tareas (con dependencias de recursos), programarlas en un calendario y detectar conflictos antes de que se solapen. Incluye una GUI basada en CustomTkinter y utilidades de consola.

## Contenido rápido

- Visión general
- Cómo funciona
- Requisitos e instalación
- Uso (GUI y consola)
- Estructura del repositorio
- Documentación de clases (qué hace cada clase)
- Pruebas

---

## 🌐 Visión general

El proyecto ofrece:

- Un modelo de eventos (`event`) que resuelve dependencias de recursos.
- Un motor `Calendar` que agrega/quita eventos y valida la disponibilidad de recursos en intervalos horarios.
- Guardado/recuperación en JSON (carpeta `saved/`) para persistir eventos activos y recursos usados.
- Interfaz gráfica (main.py + `TaskCreator`, `TaskRemover`) para crear y eliminar eventos.

Es ideal para experimentar con políticas de planificación, simulación de cargas y prototipado de orquestadores simples.

---

## ¿Cómo funciona (resumen técnico)?

- Los eventos se describen en JSON (ver `templates/tasks.json`) y al instanciarse calculan sus recursos requeridos incluyendo dependencias.
- `Calendar` mantiene una lista de eventos y un mapa de recursos usados por minuto. Para comprobar la disponibilidad usa compresión de coordenadas y un árbol de segmentos (`SegTree`) para consultas rápidas de máximo en rangos.
- Cuando se añade un evento, el calendario verifica que para cada recurso necesario no se exceda el conteo disponible en ningún minuto del rango.
- El estado se guarda en `saved/actives_events.json` y `saved/used_resources.json` mediante los métodos de `Calendar`.

---

## 🛠️ Requisitos e instalación

- Python 3.10+ (probado en 3.11/3.12)
- pip
- (Opcional) Entorno virtual

Instalación básica:

```bash
git clone https://github.com/<tu-usuario>/dinamic-events.git
cd dinamic-events
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Uso rápido

- Ejecutar la GUI principal:

```bash
python main.py
```

- Los templates con definiciones están en `templates/tasks.json` y `templates/resources.json`.
- Al editar esos JSON reinicia la aplicación para recargar la configuración.

---

## �️ Estructura principal del proyecto

```
dinamic-events/
├─ main.py                # Entrada GUI principal (ventana `app`)
├─ requirements.txt
├─ runtests.py            # Runner de tests de ejemplo
├─ saved/                 # Estado runtime persistido
├─ modules/               # Lógica del motor
│  ├─ calendar.py         # Clase Calendar
│  ├─ events.py           # Clase event
│  ├─ handlers.py         # BasicHandler y utilidades de carga JSON
│  ├─ SegTree.py          # Estructura de datos segment tree (rango)
│  ├─ utils.py            # Funciones auxiliares (timinute, logs, etc.)
│  ├─ gvar.py             # Variables globales (bootstrap)
│  └─ gui_core/           # Ventanas auxiliares (TaskCreator, TaskRemover)
├─ templates/             # Definiciones ejemplo (tasks/resources)
└─ tests/                 # Tests de ejemplo
```

---

## 📘 Descripción de las clases (qué hace cada clase)

Aquí tienes una guía rápida de las clases principales del repo y sus responsabilidades. Esto te ayuda a entender dónde tocar si quieres añadir funciones o cambiar comportamiento.

- app (en `main.py`) — Ventana principal (CustomTkinter)
   - Propósito: Interfaz principal que orquesta `TaskCreator` y `TaskRemover`, muestra la lista de eventos actuales y su información.
   - Métodos clave: `create_task()`, `remove_task()`, `update()` — refresca la lista de eventos.

- Calendar (en `modules/calendar.py`) — Motor del calendario
   - Propósito: Mantiene la lista de eventos activos, registra el uso de recursos por minuto y ofrece funciones para añadir/quitar eventos, sugerir fechas y persistir el estado.
   - Atributos importantes: `used_resources` (mapa por recursos -> tiempos), `available_tasks` (plantillas), `events` (lista de `event`).
   - Métodos clave:
      - `list_events()` — devuelve eventos vigentes (descarta antiguos).
      - `add_event(event)` — valida recursos y añade el evento si hay disponibilidad.
      - `remove(index)` — elimina evento por índice y actualiza consumos.
      - `check_available(resource, start, end)` — comprueba si un recurso está disponible en el intervalo (usa compresión de coordenadas + `SegTree`).
      - `suggest_brute(ev)` / `suggest_brute_lr(L,R,resources)` — funciones de sugerencia/ajuste (algoritmos de fuerza bruta; candidatos a optimizar).
      - `save_json_data()` / `load_used_resources(filename)` — persistencia en `saved/`.

- event (en `modules/events.py`) — Representación de una tarea/evento
   - Propósito: Encapsula los datos de un evento (nombre, rango de tiempo en minutos, rango de fechas, recursos requeridos y notas). Durante la inicialización expande dependencias de recursos y valida colisiones definidas en `templates/resources.json`.
   - Atributos: `need_resources`, `date`, `time`, `task`, `start`, `end`, `notes`.
   - Métodos: `__str__()` / `__dict__()` para serializar, `get_no_utilization(res)` para conocer recursos excluidos.

- BasicHandler (en `modules/handlers.py`) — Helper para carga/serialización JSON
   - Propósito: Funciones base que usan otros módulos para leer JSON, convertir entre dict/JSON y cargar tasks/resources.
   - Métodos: `_load_json(filename)`, `_load_resources(filename)`, `_load_tasks(name)`, `_jsonstr_to_dict()` y `_dict_to_jsonstr()`.

- SegTree (en `modules/SegTree.py`) — Árbol de segmentos con lazy propagation
   - Propósito: Permite actualizaciones en rangos y consultas de máximo en rangos. Es usado por `Calendar` para calcular la carga máxima de un recurso en un intervalo.
   - Métodos: `update(l,r,x)` para sumar en un rango, `query(l,r)` para obtener el máximo.

- TaskCreator (en `modules/gui_core/TaskCreator.py`) — Ventana GUI para crear eventos
   - Propósito: Formulario gráfico para seleccionar una tarea, ver las dependencias y crear un `event` con comprobación de fecha y disponibilidad. Usa `calendar.suggest_brute_lr` para sugerir fechas cuando es necesario.
   - Métodos: `_get_tasks()`, `_get_deps(selected)`, `add_event()` y `adjust()`.

- TaskRemover (en `modules/gui_core/TaskRemover.py`) — Ventana GUI para eliminar eventos
   - Propósito: Muestra eventos activos, permite seleccionar uno y eliminarlo. Actualiza `saved/` tras un borrado.
   - Métodos: `update_combo()` (daemon que refresca la lista), `remove()`.

Si quieres que genere documentación automática (por ejemplo un archivo markdown por clase o docstrings más completos), lo puedo añadir.

---

## 🧪 Pruebas

- `python runtests.py` ejecuta los tests de ejemplo en `tests/`.

---

## Siguientes pasos recomendados

1. Añadir más tests unitarios para `Calendar` y `SegTree` (casos de colisión y límites).
2. Refactorizar `Calendar.check_available` y `suggest_brute*` para mejorar rendimiento y legibilidad.
3. Docker / CI si vas a desplegar o compartir con colaboradores.

---

¿Quieres que además genere una sección de ejemplos (fragmentos de código) mostrando cómo añadir eventos programáticamente y cómo testear `Calendar` de forma unitaria? Puedo añadirlos ahora.
