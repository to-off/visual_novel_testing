from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.common.exceptions import "Login link is not presented"

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
        '''
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except "Login link is not presented":
            return False
        return True
        '''