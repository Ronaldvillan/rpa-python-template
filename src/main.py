
# src/main.py
import os
import time
import pandas as pd # Para simular un DataFrame de entrada

# Importa tus módulos
from src.utilities.logger import get_logger
from src.utilities.config_reader import get_config, get_credentials
from src.modules import web_automation, excel_handler, data_processor


def main():
    """
    Función principal que orquesta el proceso de automatización RPA.
    """
    driver = None # Inicializa driver a None para asegurar que siempre se cierre si falla

    try:
        # --- 1. Configuración Inicial ---
        config = get_config() # Obtiene la configuración del archivo settings.ini
        credentials = get_credentials() # Obtiene las credenciales del archivo .env

        # Obtiene la ruta del archivo de log desde la configuración y inicializa el logger
        log_file_path = config['PATHS']['LOG_FILE']
        logger = get_logger(log_file=log_file_path)

        logger.info("--- Iniciando el proceso de automatización RPA ---")

        # --- 2. Preparación de Variables desde Configuración y Credenciales ---
        web_url = config['WEB']['BASE_URL']
        web_username = credentials.get('WEB_USERNAME') 
        web_password = credentials.get('WEB_PASSWORD') 

        username_field_id = config['WEB']['USERNAME_FIELD_ID']
        password_field_id = config['WEB']['PASSWORD_FIELD_ID']
        login_button_id = config['WEB']['LOGIN_BUTTON_ID']

        input_excel_path = os.path.join(config['PATHS']['INPUT_DIR'], 'data_to_process.xlsx')
        output_excel_path = os.path.join(config['PATHS']['OUTPUT_DIR'], 'processed_results.xlsx')

        # --- 3. Ejecución del Proceso RPA ---

        # Paso 3.1: Inicializar el navegador y hacer login (Web Automation)
        logger.info("Paso 1: Inicializando navegador y realizando login...")
        # Puedes cambiar 'headless=False' a 'headless=True' si no quieres ver el navegador
        driver = web_automation.initialize_driver(logger, headless=False) 

        # Nota: Para probar el login, la URL de ejemplo no es funcional.
        # Necesitarías una URL real con campos de login con los IDs especificados.
        # web_automation.login(driver, web_url, username_field_id, password_field_id, login_button_id, web_username, web_password)

        # Para la simulación inicial, solo navegaremos a la URL de ejemplo.
        web_automation.navigate_to_url(driver, web_url)
        logger.info(f"Navegado a la URL de ejemplo: {web_url}")
        time.sleep(3) # Pequeña pausa para ver la página

        # Paso 3.2: Leer datos de Excel (Excel Handler)
        logger.info(f"Paso 2: Simulando lectura de datos de Excel: {input_excel_path}")
        # **Para que esta parte funcione, crea manualmente un archivo `data/input/data_to_process.xlsx`**
        # con algunas columnas, por ejemplo: 'Quantity', 'UnitPrice', 'Description'.
        # Si no lo creas, la función read_excel_to_dataframe lanzará un FileNotFoundError.

        # Simulamos un DataFrame para que el proceso continúe si no tienes el archivo Excel aún
        data_sample = {'Quantity': [10, 20, 15], 'UnitPrice': [5.5, 10.0, 7.2], 'Description': ['Item A', 'Item B', 'Item C']}
        df_input = pd.DataFrame(data_sample)

        # Descomenta la siguiente línea y elimina la simulación de DataFrame cuando tengas tu archivo Excel real:
        # df_input = excel_handler.read_excel_to_dataframe(input_excel_path, logger)
        logger.info(f"Se cargaron {len(df_input)} filas (simuladas o reales) del archivo de entrada.")


        # Paso 3.3: Procesar datos (aquí se integraría la IA)
        logger.info("Paso 3: Procesando datos y aplicando lógica (aquí iría la IA)...")
        df_processed = data_processor.process_data(df_input.copy(), logger) # .copy() para evitar SettingWithCopyWarning
        logger.info("Procesamiento de datos completado.")

        # Paso 3.4: Escribir resultados a Excel (Excel Handler)
        logger.info(f"Paso 4: Escribiendo resultados procesados a: {output_excel_path}")
        excel_handler.write_dataframe_to_excel(df_processed, output_excel_path, logger)
        logger.info("Resultados escritos en el archivo de salida.")

        logger.info("--- Proceso de automatización RPA finalizado con éxito ---")

    except FileNotFoundError as fnfe:
        logger.error(f"Error: Archivo no encontrado - {fnfe}", exc_info=True)
    except Exception as e:
        logger.error(f"¡El proceso de automatización ha fallado! Error: {e}", exc_info=True)
        logger.info("--- Proceso de automatización RPA finalizado con errores ---")
    finally:
        # Asegura que el navegador se cierre al final del proceso
        if driver:
            web_automation.close_driver(driver)
        logger.info("Limpieza de recursos completada.")

if __name__ == "__main__":
    main()