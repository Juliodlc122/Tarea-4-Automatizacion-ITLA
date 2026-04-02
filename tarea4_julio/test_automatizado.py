import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    opciones = webdriver.ChromeOptions()
    opciones.add_argument('--start-maximized')
    navegador = webdriver.Chrome(options=opciones)
    ruta_absoluta = "file://" + os.path.abspath("index.html")
    navegador.get(ruta_absoluta)
    yield navegador
    navegador.quit()

class TestAutomatizacionSelenium:

    def test_hu01_login_prueba_negativa(self, driver):
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
        driver.find_element(By.ID, "clave").send_keys("clave_erronea")
        driver.find_element(By.ID, "btn_entrar").click()
        wait.until(EC.text_to_be_present_in_element((By.ID, "mensaje_login"), "denegado"))
        driver.save_screenshot("01_Login_Negativo.png")
        assert "denegado" in driver.find_element(By.ID, "mensaje_login").text

    def test_hu01_login_camino_feliz(self, driver):
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
        driver.find_element(By.ID, "clave").send_keys("1234")
        driver.find_element(By.ID, "btn_entrar").click()
        wait.until(EC.visibility_of_element_located((By.ID, "pantalla_crud")))
        driver.save_screenshot("02_Login_Exitoso.png")
        assert driver.find_element(By.ID, "pantalla_crud").is_displayed()

    def test_hu02_crear_prueba_limites(self, driver):
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
        driver.find_element(By.ID, "clave").send_keys("1234")
        driver.find_element(By.ID, "btn_entrar").click()
        wait.until(EC.visibility_of_element_located((By.ID, "pantalla_crud")))
        driver.find_element(By.ID, "btn_crear").click()
        wait.until(EC.text_to_be_present_in_element((By.ID, "mensaje_crud"), "obligatorio"))
        driver.save_screenshot("03_Crear_Limite.png")
        assert "obligatorio" in driver.find_element(By.ID, "mensaje_crud").text

    def test_hu02_crear_camino_feliz(self, driver):
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
        driver.find_element(By.ID, "clave").send_keys("1234")
        driver.find_element(By.ID, "btn_entrar").click()
        wait.until(EC.visibility_of_element_located((By.ID, "pantalla_crud")))
        driver.find_element(By.ID, "nombre_cliente").send_keys("Julio Ruiz")
        driver.find_element(By.ID, "edad_cliente").send_keys("20")
        driver.find_element(By.ID, "telefono_cliente").send_keys("809-555-0123")
        driver.find_element(By.ID, "direccion_cliente").send_keys("La Romana")
        driver.find_element(By.ID, "btn_crear").click()
        wait.until(EC.visibility_of_element_located((By.ID, "toast")))
        driver.save_screenshot("04_Crear_Exitoso.png")
        assert "agregó" in driver.find_element(By.ID, "toast").text

    def test_hu03_leer_camino_feliz(self, driver):
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
        driver.find_element(By.ID, "clave").send_keys("1234")
        driver.find_element(By.ID, "btn_entrar").click()
        wait.until(EC.visibility_of_element_located((By.ID, "pantalla_crud")))
        driver.find_element(By.ID, "nombre_cliente").send_keys("Julio Ruiz")
        driver.find_element(By.ID, "edad_cliente").send_keys("20")
        driver.find_element(By.ID, "btn_crear").click()
        wait.until(EC.visibility_of_element_located((By.ID, "registro_1")))
        driver.save_screenshot("05_Leer_Exitoso.png")
        assert driver.find_element(By.ID, "registro_1").is_displayed()

    def test_hu04_actualizar_prueba_negativa(self, driver):
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
        driver.find_element(By.ID, "clave").send_keys("1234")
        driver.find_element(By.ID, "btn_entrar").click()
        wait.until(EC.visibility_of_element_located((By.ID, "pantalla_crud")))
        driver.find_element(By.ID, "nombre_cliente").send_keys("Julio Ruiz")
        driver.find_element(By.ID, "btn_crear").click()
        wait.until(EC.visibility_of_element_located((By.ID, "registro_1")))
        driver.find_element(By.CSS_SELECTOR, "#registro_1 .btn-editar").click()
        wait.until(EC.visibility_of_element_located((By.ID, "btn_guardar_edicion")))
        driver.find_element(By.ID, "nombre_cliente").clear()
        driver.find_element(By.ID, "btn_guardar_edicion").click()
        wait.until(EC.text_to_be_present_in_element((By.ID, "mensaje_crud"), "obligatorio"))
        driver.save_screenshot("06_Actualizar_Negativo.png")
        assert "obligatorio" in driver.find_element(By.ID, "mensaje_crud").text

    def test_hu04_actualizar_camino_feliz(self, driver):
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
        driver.find_element(By.ID, "clave").send_keys("1234")
        driver.find_element(By.ID, "btn_entrar").click()
        wait.until(EC.visibility_of_element_located((By.ID, "pantalla_crud")))
        driver.find_element(By.ID, "nombre_cliente").send_keys("Julio Ruiz")
        driver.find_element(By.ID, "edad_cliente").send_keys("20")
        driver.find_element(By.ID, "btn_crear").click()
        wait.until(EC.visibility_of_element_located((By.ID, "registro_1")))
        driver.find_element(By.CSS_SELECTOR, "#registro_1 .btn-editar").click()
        wait.until(EC.visibility_of_element_located((By.ID, "btn_guardar_edicion")))
        driver.find_element(By.ID, "nombre_cliente").clear()
        driver.find_element(By.ID, "nombre_cliente").send_keys("Julio Modificado")
        driver.find_element(By.ID, "btn_guardar_edicion").click()
        wait.until(EC.visibility_of_element_located((By.ID, "toast")))
        driver.save_screenshot("07_Actualizar_Exitoso.png")
        assert "editó" in driver.find_element(By.ID, "toast").text

    def test_hu05_eliminar_camino_feliz(self, driver):
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "usuario"))).send_keys("admin")
        driver.find_element(By.ID, "clave").send_keys("1234")
        driver.find_element(By.ID, "btn_entrar").click()
        wait.until(EC.visibility_of_element_located((By.ID, "pantalla_crud")))
        driver.find_element(By.ID, "nombre_cliente").send_keys("Julio Ruiz")
        driver.find_element(By.ID, "btn_crear").click()
        wait.until(EC.visibility_of_element_located((By.ID, "registro_1")))
        driver.find_element(By.CSS_SELECTOR, "#registro_1 .btn-eliminar").click()
        wait.until(EC.visibility_of_element_located((By.ID, "toast")))
        driver.save_screenshot("08_Eliminar_Exitoso.png")
        assert "eliminó" in driver.find_element(By.ID, "toast").text