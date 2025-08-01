from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def testar_login(usuario, senha):
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(senha)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    if "secure" in driver.current_url:
        print("Login bem-sucedido!")
    else:
        erro = driver.find_element(By.ID, "flash").text
        print("Erro:", erro)

print("CT01 - Login válido")
testar_login("tomsmith", "SuperSecretPassword!")

print("CT02 - Senha inválida")
testar_login("tomsmith", "senha_errada")

print("CT03 - Usuário em branco")
testar_login("", "SuperSecretPassword!")

driver.quit()
