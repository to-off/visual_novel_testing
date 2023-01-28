from pages.browser_func import BrowserFunction
from pages.locators import NavBarLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
Тут находится общий функционал, присутствующий почти на всех страницах:
1. Переход на главное меню осуществляется почти со всех страниц

Если на вашей странице нет перехода на главную (кроме navbar), то наследуйтесь сразу от класса BrowserFunction
'''

class NavBar(BrowserFunction):

    def user_is_authorized(self):
        self.find_element(*NavBarLocators.EXIT)
        self.find_element(*NavBarLocators.ACCOUNT)
    def main_page(self):
        ref = self.browser.find_element(*NavBarLocators.MAIN)
        ref.click()

    def chart_page(self):
        ref = self.browser.find_element(*NavBarLocators.CHART)
        ref.click()

    def translations_page(self):
        ref = self.browser.find_element(*NavBarLocators.TRANSLATE)
        ref.click()

    def about_site_page(self):
        ref = self.browser.find_element(*NavBarLocators.ABOUT_SITE)
        ref.click()

    def account_page(self):
        self.user_is_authorized()
        ref = self.browser.find_element(*NavBarLocators.ACCOUNT)
        ref.click()

    def login_page(self):
        ref = self.browser.find_element(*NavBarLocators.LOGIN)
        ref.click()

    def exit_page(self):
        self.user_is_authorized()
        ref = self.browser.find_element(*NavBarLocators.EXIT)
        ref.click()



class GeneralFunction(NavBar):
    def go_to_main_page(self):
        main = self.browser.find_element(By.CSS_SELECTOR, "div>h3>a:first-of-type")
        main.click()