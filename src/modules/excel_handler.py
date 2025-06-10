import pandas as pd
import os

# Variable global para el logger, se asignará desde main.py
logger = None

def read_excel_to_dataframe(file_path, log_instance, sheet_name=0):
    """
    Lee un archivo Excel y devuelve un DataFrame de pandas.
    :param file_path: Ruta al archivo Excel.
    :param log_instance: Instancia del logger.
    :param sheet_name: Nombre o índice de la hoja a leer (por defecto la primera).
    :return: pandas.DataFrame
    :raises FileNotFoundError: Si el archivo Excel no se encuentra.
    :raises Exception: Para otros errores de lectura del Excel.
    """
    global logger
    logger = log_instance
    if not os.path.exists(file_path):
        logger.error(f"Archivo Excel no encontrado: {file_path}")
        raise FileNotFoundError(f"Archivo Excel no encontrado: {file_path}")
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        logger.info(f"Archivo Excel '{file_path}' leído correctamente. Filas: {len(df)}")
        return df
    except Exception as e:
        logger.error(f"Error al leer el archivo Excel '{file_path}': {e}", exc_info=True)
        raise

def write_dataframe_to_excel(dataframe, file_path, log_instance, sheet_name='Sheet1', index=False):
    """
    Escribe un DataFrame de pandas a un archivo Excel.
    :param dataframe: DataFrame a escribir.
    :param file_path: Ruta donde se guardará el archivo Excel.
    :param log_instance: Instancia del logger.
    :param sheet_name: Nombre de la hoja en la que se escribirá.
    :param index: Si es True, incluye el índice del DataFrame en el Excel.
    :raises Exception: Para errores de escritura en Excel.
    """
    global logger
    logger = log_instance
    try:
        # Asegúrate de que el directorio de salida exista
        output_dir = os.path.dirname(file_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        dataframe.to_excel(file_path, sheet_name=sheet_name, index=index)
        logger.info(f"DataFrame escrito correctamente en '{file_path}'.")
    except Exception as e:
        logger.error(f"Error al escribir el DataFrame en Excel '{file_path}': {e}", exc_info=True)
        raise

# Puedes añadir más funciones aquí: append_to_excel, get_cell_value, etc.