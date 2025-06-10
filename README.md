 # 🤖 Prueba RPA con Python (Intelligent Automation) 🤖

Este es un proyecto de ejemplo para explorar la automatización de procesos robóticos (RPA) utilizando Python, con una estructura modular y preparada para integrar capacidades de Inteligencia Artificial.

---

## 🎯 Objetivo del Proyecto

Demostrar la estructura básica de un proyecto RPA en Python, incluyendo:
- Gestión de configuración y credenciales.
- Registro de eventos (logging).
- Módulos para automatización web, manejo de Excel y procesamiento de datos.
- Preparación para la integración de IA.

---

## 📂 Estructura del Proyecto

prueba_rpa_python/
├── src/
│   ├── main.py                   # Orquestador principal del proceso
│   ├── modules/
│   │   ├── web_automation.py     # Funciones para interacción web (Selenium)
│   │   ├── excel_handler.py      # Funciones para manipulación de Excel (Pandas, OpenPyXL)
│   │   └── data_processor.py     # Funciones para procesamiento de datos y lógica de IA
│   └── utilities/
│       ├── logger.py             # Módulo para configuración de logging
│       └── config_reader.py      # Módulo para leer configuración y credenciales
├── data/
│   ├── input/                    # Archivos de datos de entrada para el RPA
│   └── output/                   # Archivos de datos generados por el RPA
├── config/
│   ├── settings.ini              # Configuraciones no sensibles (URLs, rutas)
│   └── .env.example              # Plantilla para variables de entorno sensibles (credenciales)
├── logs/                         # Archivos de registro de la ejecución del bot
├── .env                          # ⚠️ Archivo REAL de credenciales (IGNORADO POR GIT)
├── .gitignore                    # Archivos y carpetas a ignorar por Git
├── requirements.txt              # Listado de librerías Python necesarias
└── README.md                     # Documentación del proyecto


---

## 🚀 Cómo Empezar

1.  **Clonar el Repositorio (si aplica) o Crear la Estructura:**
    ```bash
    mkdir prueba_rpa_python
    cd prueba_rpa_python
    # Luego, sigue los comandos de creación de estructura
    ```

2.  **Crear y Activar el Entorno Virtual:**
    ```bash
    python3 -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuración de Credenciales:**
    Crea un archivo llamado `.env` dentro de la carpeta `config/` (al mismo nivel que `settings.ini`) y rellénalo con tus credenciales y variables de entorno reales, siguiendo el formato de `config/.env.example`.
    **¡IMPORTANTE! Este archivo `.env` NO debe ser subido a Git.**

    Ejemplo de `config/.env`:
    ```
    WEB_USERNAME=tu_usuario_real
    WEB_PASSWORD=tu_contraseña_real
    ```

5.  **Configuración General:**
    Revisa y ajusta los valores en `config/settings.ini` según sea necesario (URLs, rutas de archivos, etc.).

---

## ⚙️ Ejecución

Para ejecutar el proceso de automatización principal:

```bash
# Asegúrate de que el entorno virtual esté activo
python src/main.py
Los mensajes de log aparecerán en la consola y se guardarán en el archivo logs/rpa_log.log.