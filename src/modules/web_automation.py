from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# Variable global para el logger, se asignará desde main.py
logger = None 

def initialize_driver(log_instance, headless=False):
    """
    Inicializa y devuelve un WebDriver de Chrome.
    :param log_instance: Instancia del logger para registrar eventos.
    :param headless: Si es True, el navegador se ejecuta en segundo plano (sin interfaz gráfica).
    :return: selenium.webdriver.Chrome
    """
    global logger
    logger = log_instance
    logger.info("Inicializando WebDriver de Chrome...")
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    try:
        # Maneja la descarga y configuración del driver automáticamente
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        logger.info("WebDriver inicializado correctamente.")
        return driver
    except Exception as e:
        logger.error(f"Error al inicializar WebDriver: {e}", exc_info=True)
        raise # Relanza la excepción para que sea manejada en main.py

def navigate_to_url(driver, url):
    """
    Navega a una URL específica.
    :param driver: Instancia del WebDriver.
    :param url: URL a la que navegar.
    """
    logger.info(f"Navegando a la URL: {url}")
    driver.get(url)
    time.sleep(2) # Pequeña pausa para asegurar la carga inicial de la página

def login(driver, url, username_field_id, password_field_id, login_button_id, username, password):
    """
    Realiza el proceso de login en una página web.
    :param driver: Instancia del WebDriver.
    :param url: URL de la página de login.
    :param username_field_id: ID o selector del campo de usuario.
    :param password_field_id: ID o selector del campo de contraseña.
    :param login_button_id: ID o selector del botón de login.
    :param username: Nombre de usuario.
    :param password: Contraseña.
    """
    logger.info(f"Intentando login en: {url}")
    navigate_to_url(driver, url)

    try:
        # Espera a que el campo de usuario esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, username_field_id))
        )
        driver.find_element(By.ID, username_field_id).send_keys(username)
        logger.info("Usuario ingresado.")

        driver.find_element(By.ID, password_field_id).send_keys(password)
        logger.info("Contraseña ingresada.")

        driver.find_element(By.ID, login_button_id).click()
        logger.info("Botón de login clickeado.")

        # Aquí podrías añadir una espera para verificar que el login fue exitoso,
        # por ejemplo, esperando la presencia de un elemento en la página post-login.
        # WebDriverWait(driver, 15).until(
        #    EC.presence_of_element_located((By.ID, "dashboard_element"))
        # )
        # logger.info("Login exitoso. Página de dashboard cargada.")

    except Exception as e:
        logger.error(f"Error durante el proceso de login: {e}", exc_info=True)
        raise # Relanza la excepción para que main.py la capture

def close_driver(driver):
    """
    Cierra el WebDriver.
    :param driver: Instancia del WebDriver.
    """
    if driver:
        logger.info("Cerrando WebDriver.")
        driver.quit()

# Puedes añadir más funciones aquí: extract_table_data, fill_form, click_element, etc.
