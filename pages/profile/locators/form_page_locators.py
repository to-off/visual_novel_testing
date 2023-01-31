from selenium.webdriver.common.by import By

class FormPageLocators:
    USERNAME = (By.CSS_SELECTOR, '#id_username')
    PASSWORD1 = (By.CSS_SELECTOR, '#id_password1')
    PASSWORD2 = (By.CSS_SELECTOR, '#id_password2')
    EMAIL = (By.CSS_SELECTOR, '#id_email')
    BUTTON = (By.CSS_SELECTOR, 'body > div.container > form > button')

