from pages.browser_func import BrowserFunction
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
Тут находится общий функционал, присутствующий почти на всех страницах:
1. Переход на главное меню осуществляется почти со всех страниц

Если на вашей странице нет перехода на главную (кроме navbar), то наследуйтесь сразу от класса BrowserFunction
'''
class GeneralFunction(BrowserFunction):
    def go_to_main_page(self):
        main = self.browser.find_element(By.CSS_SELECTOR, "div>h3>a:first-of-type")
        main.click()