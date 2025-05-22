from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import tempfile
import time

## Configurações iniciais ##
URL = "https://demos.bellatrix.solutions"
product_name = "Saturn V"

## Dados de compra ##
checkout_data = {
    "first_name": "Ana",
    "last_name": "Paula",
    "country": "Brazil",
    "address": "Rua da Alegria, 123",
    "city": "São Paulo",
    "state": "São Paulo",
    "zip": "12345-678",
    "phone": "12987654320",
    "email": "ana.paula@email.com"
}

## Função utilizada para o dropdown de país ##
def select_country(driver, wait, country):
    driver.find_element(By.CLASS_NAME, "select2-selection--single").click()
    search_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "select2-search__field")))
    search_input.send_keys(country)
    search_input.send_keys(Keys.RETURN)

## Função utilizada para o dropdown de estado ##
def select_state(driver, wait, state):
    driver.find_element(By.ID, "select2-billing_state-container").click()
    search_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "select2-search__field")))
    search_input.send_keys(state)
    search_input.send_keys(Keys.RETURN)

## Configurações de perfil do Google Chrome ##
def main():
    chrome_options = Options()
    temp_profile = tempfile.mkdtemp()

    chrome_options.add_argument(f"--user-data-dir={temp_profile}")
    chrome_options.add_argument("--disable-autofill")
    chrome_options.add_argument("--disable-save-password-bubble")

    prefs = {
     "credentials_enable_service": False,
     "profile.password_manager_enabled": False,
     "profile.autofill_profile_enabled": False,
     "profile.autofill_credit_card_enabled": False,
     "profile.default_content_setting_values.notifications": 2
    }
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)

    try:
        ## Acessando o site ##
        driver.maximize_window()
        driver.get(URL)

        ## Buscando o produto ##
        search_input = wait.until(EC.presence_of_element_located((By.NAME, "s")))
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.RETURN)

        ## Clicando no produto ##
        wait.until(EC.presence_of_element_located((By.XPATH, f'//h2[contains(text(), "{product_name}")]')))
        product_link = driver.find_element(By.XPATH, f'//h2[contains(text(), "{product_name}")]/ancestor::a')
        product_link.click()

        ## Adicionando o produto ao carrinho ##
        wait.until(EC.element_to_be_clickable((By.NAME, "add-to-cart"))).click()

        ## Indo para o carrinho de compras ##
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cart-contents"))).click()

        ## Indo para o checkout ##
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))).click()

        ## Preenchendo o formulário de compra ##
        wait.until(EC.presence_of_element_located((By.ID, "billing_first_name"))).send_keys(checkout_data["first_name"])
        driver.find_element(By.ID, "billing_last_name").send_keys(checkout_data["last_name"])
        select_country(driver, wait, checkout_data["country"])
        driver.find_element(By.ID, "billing_address_1").send_keys(checkout_data["address"])
        driver.find_element(By.ID, "billing_city").send_keys(checkout_data["city"])
        select_state(driver, wait, checkout_data["state"])
        driver.find_element(By.ID, "billing_postcode").send_keys(checkout_data["zip"])
        driver.find_element(By.ID, "billing_phone").send_keys(checkout_data["phone"])
        driver.find_element(By.ID, "billing_email").send_keys(checkout_data["email"])

        ## Finalizando o pedido ##
        driver.find_element(By.ID, "place_order").click()

        ## Verificação da confirmação ##
        confirmation_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received")))
        
        assert "Thank you. Your order has been received." in confirmation_message.text
        print("Thank you. Your order has been received.")

    except Exception as e:
        print("Erro durante a automação: {e}")

    finally:
        time.sleep(5)
        driver.quit()


if __name__ == "__main__":
    main()
