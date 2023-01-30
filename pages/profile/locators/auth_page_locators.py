from selenium.webdriver.common.by import By

class AuthPageLoc:
    LOGIN =  (By.CSS_SELECTOR, '#id_username')
    PASSW = (By.CSS_SELECTOR, '#id_password')
    SEND = (By.CSS_SELECTOR, 'body > div.container > form > button')