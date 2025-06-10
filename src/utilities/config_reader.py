import configparser
import os
from dotenv import load_dotenv

def get_config(config_file='config/settings.ini'):
    """
    Lee la configuración de un archivo .ini.
    """
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Archivo de configuración no encontrado: {config_file}")
    config.read(config_file)
    return config

def get_credentials(env_file='config/.env'):
    """
    Carga variables de entorno desde un archivo .env.
    """
    load_dotenv(dotenv_path=env_file)
    return os.environ

# Ejemplo de uso (solo si se ejecuta directamente este módulo)
if __name__ == "__main__":
    # Asegúrate de tener un archivo config/settings.ini
    # y un archivo .env (o .env.example) en la raíz de tu proyecto
    print("--- Probando config_reader ---")
    
    try:
        settings = get_config()
        print(f"URL base de settings.ini: {settings['WEB']['BASE_URL']}")
        print(f"Directorio de entrada: {settings['PATHS']['INPUT_DIR']}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Error al leer settings.ini: {e}")

    try:
        # Crea un archivo .env en la raíz de tu proyecto para probar esto
        # Ejemplo: MY_API_KEY=tu_clave_secreta
        credentials = get_credentials()
        print(f"Credencial de .env (ej. MY_API_KEY): {credentials.get('MY_API_KEY', 'No definida')}")
    except Exception as e:
        print(f"Error al leer .env: {e}")
    print("--- Fin prueba config_reader ---")