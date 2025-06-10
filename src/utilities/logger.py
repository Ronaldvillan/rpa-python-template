import logging
import os
from datetime import datetime

def get_logger(name='rpa_bot', log_file='logs/rpa_log.log', level=logging.INFO):
    """
    Configura y devuelve una instancia de logger para el proyecto.
    Crea el directorio 'logs' si no existe.
    """
    # Asegúrate de que el directorio de logs exista
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configuración básica del logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevenir que se añadan múltiples handlers al mismo logger
    if not logger.handlers:
        # Handler para la consola
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # Handler para el archivo de log
        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger

# Puedes añadir una función para probarlo o usarlo directamente en otros módulos
if __name__ == "__main__":
    test_logger = get_logger(log_file='test_logs/test_rpa.log')
    test_logger.info("Este es un mensaje informativo desde el logger de prueba.")
    test_logger.warning("Esto es una advertencia.")
    test_logger.error("¡Ha ocurrido un error!")