from selenium.webdriver.common.by import By
class NavBarLocators:
    MAIN = (By.XPATH, '//*[@id="navbar-main"]//li[1]/a')
    CHART = (By.XPATH, '//*[@id="navbar-main"]//li[2]/a')
    TRANSLATE = (By.XPATH, '//*[@id="navbar-main"]//li[3]/a')
    ABOUT_SITE = (By.XPATH, '//*[@id="navbar-main"]//li[4]/a')
    VNDB = (By.XPATH, '//*[@id="navbar-main"]//li[5]/a')

    # if not login
    LOGIN = (By.XPATH, '//*[@id="navbar-main"]//li[6]/a')

    # if login
    ACCOUNT = (By.XPATH, '//*[@id="navbar-main"]//li[6]/a')
    EXIT = (By.XPATH, '//*[@id="navbar-main"]//li[7]/a')
