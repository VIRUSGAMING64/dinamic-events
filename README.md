# Jamazon - Administrador de Tareas y Eventos 📅🚀

**Jamazon** (también conocido como *Dinamic Events*) es una aplicación de escritorio desarrollada en Python para la gestión eficiente de tareas, eventos y recursos. Utiliza una interfaz gráfica moderna y estructuras de datos avanzadas para manejar la programación y evitar conflictos de recursos.

## 🌟 Características Principales

*   **Gestión de Tareas:** Crear y eliminar tareas fácilmente.
*   **Definición de Eventos:** Programar eventos con rangos de fecha y hora específicos.
*   **Gestión de Recursos:** Añadir recursos y manejar dependencias entre ellos.
*   **Detección de Conflictos:** Sistema inteligente que verifica si los recursos necesarios están disponibles y no entran en conflicto con otras reglas.
*   **Interfaz Moderna:** GUI oscura y amigable basada en `customtkinter`.

## 🛠️ Instalación y Ejecución

Sigue estos pasos para ejecutar la aplicación en tu entorno local:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/VIRUSGAMING64/Jamazon.git
    cd Jamazon
    ```

2.  **Instalar dependencias:**
    Asegúrate de tener Python instalado. Luego, instala las librerías necesarias:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar la aplicación:**
    ```bash
    python main.py
    ```

## 📖 Guía de Uso

Al iniciar la aplicación, verás un panel de control con las siguientes opciones:

*   **Create new task:** Abre un formulario para registrar una nueva tarea en el sistema.
*   **Remove existing task:** Permite eliminar tareas que ya no son necesarias.
*   **Add Resource:** Agrega nuevos recursos (ej. salas, equipos) que pueden ser asignados a eventos.
*   **Define new event:** Crea eventos complejos que requieren recursos y tienen una duración específica. El sistema validará automáticamente si los recursos están disponibles y si existen conflictos de dependencia.

## 🧠 Detalles Técnicos y Módulos

El proyecto está construido con un enfoque modular. A continuación se detallan los componentes principales:

### 1. Núcleo (`modules/`)

*   **`app` (en `main.py`)**:
    *   Es la ventana principal de la aplicación.
    *   Configura la interfaz, carga imágenes y gestiona la navegación a otras herramientas.

*   **`Calendar` (en `modules/calendar.py`)**:
    *   Gestiona la lista de eventos activos y los recursos utilizados.
    *   Se encarga de guardar y cargar el estado de la aplicación.
    *   Coordina la disponibilidad de las tareas.

*   **`event` (en `modules/events.py`)**:
    *   Representa un evento individual con fecha, hora y recursos necesarios.
    *   **Validación:** Verifica dependencias y colisiones de recursos al inicializarse. Si hay un conflicto, impide la creación del evento.

*   **`SegTree` (en `modules/SegTree.py`)**:
    *   Implementa un **Árbol de Segmentos** con *Lazy Propagation*.
    *   Se utiliza para realizar consultas eficientes sobre rangos de tiempo, permitiendo verificar rápidamente la disponibilidad o el uso de recursos en intervalos específicos.

### 2. Interfaz Gráfica (`modules/gui_core/`)

*   **`EventCreator` (en `EventDeffiner.py`)**: Ventana para ingresar detalles de nuevos eventos.
*   **`TaskCreator`**: Interfaz para registrar nuevas tareas en el sistema.
*   **`TaskRemover`**: Interfaz para eliminar tareas existentes.
*   **`ResAdder`**: Permite añadir nuevos recursos a la base de datos (`resources.json`).

## 📂 Estructura del Proyecto

```text
Jamazon/
├── changelog           # Registro de cambios del proyecto
├── clean.py            # Script de limpieza de archivos temporales
├── logs.txt            # Archivo de registro de errores y eventos
├── main.py             # 🏁 Punto de entrada principal de la aplicación
├── README.md           # Documentación del proyecto
├── requirements.txt    # Lista de dependencias de Python
├── test.py             # Script para pruebas rápidas
├── modules/            # 🧠 Núcleo lógico del sistema
│   ├── __init__.py
│   ├── calendar.py     # Lógica del calendario y disponibilidad
│   ├── events.py       # Definición de la clase Evento y validaciones
│   ├── gvar.py         # Variables globales
│   ├── handlers.py     # Manejadores base y utilidades
│   ├── SegTree.py      # Implementación de Segment Tree (Árbol de Segmentos)
│   ├── utils.py        # Funciones de utilidad general
│   └── gui_core/       # 🎨 Componentes de la Interfaz Gráfica
│       ├── __init__.py
│       ├── EventDeffiner.py  # Ventana para definir nuevos eventos
│       ├── EventShower.py    # Visualizador de eventos
│       ├── ResAdder.py       # Ventana para añadir recursos
│       ├── TaskCreator.py    # Ventana para crear tareas
│       └── TaskRemover.py    # Ventana para eliminar tareas
├── saved/              # Carpeta para datos guardados
├── templates/          # 📄 Plantillas y datos estáticos
│   ├── resources.json  # Base de datos de recursos disponibles
│   └── tasks.json      # Base de datos de tareas guardadas
└── tests/              # 🧪 Pruebas unitarias
```

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Si deseas mejorar Jamazon:

1.  Haz un Fork del proyecto.
2.  Crea una rama para tu nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3.  Realiza tus cambios y haz commit (`git commit -m "Añadir nueva funcionalidad"`).
4.  Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5.  Abre un Pull Request.

---
Desarrollado por [VIRUSGAMING64](https://github.com/VIRUSGAMING64)
