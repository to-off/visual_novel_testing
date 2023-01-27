from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
Класс с основными методами браузера и его определением
'''
class BrowserFunction():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
    def open(self):
        self.browser.get(self.url)