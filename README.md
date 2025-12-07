# Dynamic Events 🚀

> Planificador dinámico de tareas y recursos. Crea eventos, reserva CPU/GPU/RAM y detecta colisiones antes de que sucedan.

## 📚 Tabla de contenidos

- [Visión general](#-visión-general)
- [¿Cómo funciona?](#-cómo-funciona-resumen-técnico)
- [Requisitos e instalación](#-requisitos-e-instalación)
- [Uso rápido](#-uso-rápido)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Descripción de las clases](#-descripción-de-las-clases-qué-hace-cada-clase)
- [Pruebas](#-pruebas)
- [Siguientes pasos](#-siguientes-pasos-recomendados)

---

## 🌐 Visión general

Dynamic Events es una plataforma ligera para experimentar con planificación de recursos. Define tareas con necesidades de hardware, prográmalas en un calendario compartido y detecta conflictos con una GUI construida con CustomTkinter.

Ofrece:
- Un modelo de eventos (`event`) que resuelve dependencias de recursos.
- Un motor `Calendar` que agrega/quita eventos y valida la disponibilidad de recursos.
- Guardado/recuperación en JSON para persistir el estado de la aplicación.
- Interfaz gráfica para crear y eliminar eventos de forma interactiva.
- Barra de progreso en el menú principal para visualizar el estado de la tarea seleccionada en tiempo real.

Es ideal para: laboratorios de automatización, simulación de cargas y prototipado de orquestadores simples.

---

## ⚙️ ¿Cómo funciona? (Resumen técnico)

- Los eventos se describen en `templates/tasks.json` y al instanciarse calculan sus recursos requeridos, incluyendo dependencias definidas en `templates/resources.json`.
- `Calendar` mantiene una lista de eventos y un mapa de recursos usados por minuto. Para comprobar la disponibilidad de forma eficiente, usa **compresión de coordenadas** y un **Árbol de Segmentos** (`SegTree`) para consultas rápidas de máximo en rangos de tiempo.
- **Optimización:** Se utiliza un caché del árbol de segmentos para acelerar operaciones repetitivas como `add_event` y `suggest_brute_lr`.
- Cuando se añade un evento, el calendario verifica que para cada recurso necesario no se exceda la capacidad disponible en ningún minuto del intervalo solicitado.
- El estado se guarda en la carpeta `saved/` para mantener la persistencia entre sesiones.

---

## 🛠️ Requisitos e instalación

- Python 3.10+ (probado en 3.11/3.12)
- `pip`
- (Recomendado) Entorno virtual `venv`

Pasos para la instalación:
```bash
# 1. Clonar el repositorio
git clone https://github.com/<tu-usuario>/dinamic-events.git
cd dinamic-events

# 2. Crear y activar un entorno virtual
python -m venv .venv
# En Windows: .venv\Scripts\activate
# En Linux/macOS: source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## ▶️ Uso rápido

- Para lanzar la interfaz gráfica principal:
```bash
python main.py
```
- Los *templates* con las definiciones de tareas y recursos están en `templates/`.
- Si editas los archivos JSON de los *templates*, reinicia la aplicación para que los cambios surtan efecto.

---

## 🗂️ Estructura del proyecto

```
dinamic-events/
├─ main.py                # Entrada GUI principal
├─ clean.py               # Script de limpieza
├─ test.py                # Script de pruebas
├─ requirements.txt
├─ changelog              # Registro de cambios
├─ saved/                 # Estado guardado (eventos activos, uso de recursos)
├─ modules/               # Lógica principal del programa
│  ├─ calendar.py
│  ├─ events.py
│  ├─ gvar.py
│  ├─ handlers.py
│  ├─ Pool.py
│  ├─ SegTree.py
│  ├─ utils.py
│  └─ gui_core/           # Componentes de la interfaz gráfica
│     ├─ EventDeffiner.py
│     ├─ ResAdder.py
│     ├─ TaskCreator.py
│     └─ TaskRemover.py
├─ templates/             # Plantillas de configuración
│  ├─ resources.json
│  └─ tasks.json
└─ tests/                 # Pruebas unitarias y de integración
   ├─ test1.py
   ├─ test2.py
   ├─ test3.py
   └─ test4.py
```

---

## 📘 Descripción de las clases (qué hace cada clase)

Guía rápida de las clases principales, incluyendo su **complejidad temporal** (donde $N$ es el número de eventos, $R$ el número de recursos y $M$ el número de puntos de tiempo únicos).

- **app** (en `main.py`) — Ventana principal (CustomTkinter)
  - **Propósito**: Orquesta la GUI, mostrando eventos y lanzando las ventanas de creación/eliminación.
  - **Métodos clave**:
    - `create_task()` / `remove_task()`: $O(1)$
    - `update()`: $O(N)$ — Refresca la lista de eventos en la GUI.

- **Calendar** (en `modules/calendar.py`) — Motor del calendario
  - **Propósito**: Gestiona la lista de eventos, valida colisiones y persiste el estado.
  - **Métodos clave**:
    - `add_event(event)`: $O(R \cdot \log M)$ — Añade un evento tras validar la disponibilidad de sus recursos.
    - `remove(index)`: $O(N \cdot R \cdot \log M)$ — Elimina un evento y reconstruye el estado de los recursos.
    - `check_available(resource, start, end)`: $O(\log M)$ — Comprueba si un recurso está libre en un intervalo.
    - `suggest_brute_lr(...)`: $O(T \cdot R \cdot \log M)$ — Busca un hueco libre para un evento.
    - `save_json_data()` / `load_used_resources()`: $O(N \cdot R)$

- **event** (en `modules/events.py`) — Representación de una tarea/evento
  - **Propósito**: Encapsula los datos de un evento y resuelve sus dependencias de recursos.
  - **Métodos clave**:
    - `__init__`: $O(R^2)$ — Resuelve el grafo de dependencias de recursos.
    - `__str__()` / `__dict__()`: $O(1)$

- **SegTree** (en `modules/SegTree.py`) — Árbol de Segmentos
  - **Propósito**: Estructura de datos para consultar el uso máximo de recursos en rangos de tiempo.
  - **Métodos clave**:
    - `update(l, r, x)`: $O(\log M)$
    - `query(l, r)`: $O(\log M)$

- **TaskCreator** / **TaskRemover** (en `modules/gui_core/`) — Ventanas GUI
  - **Propósito**: Formularios para añadir y eliminar eventos de forma interactiva.
  - **Complejidad**: Sus operaciones (`add_event`, `remove`) dependen directamente de los métodos correspondientes en `Calendar`.

- **Utils** (en `modules/utils.py`) — Funciones de utilidad
  - **Funciones clave**:
    - `tominute(date)`: $O(1)$
    - `get_sources_dependency(resources, res)`: $O(R + E)$ — DFS sobre el grafo de dependencias (donde $E$ es el número de aristas).

---

## 🧪 Pruebas

- Para ejecutar el conjunto de pruebas, utiliza:
```bash
python test.py
```
Este comando buscará y ejecutará los tests definidos en la carpeta `tests/`.

---

## 🎯 Siguientes pasos recomendados

1.  Añadir más tests unitarios para `Calendar` y `SegTree` (casos de colisión y límites).
2.  Optimizar el método `remove` de `Calendar` para evitar la reconstrucción completa del estado.
3.  Implementar un sistema de logging más robusto para facilitar la depuración.
4.  Desarrollar la base de `webapp.py` para exponer la funcionalidad a través de una API REST.
