from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.exeptions import ElementNotVisibleException

class BasePage():
    def __init__(self, browser, url, timeout = 5):
        self.browser = browser
        self.url = url
        self.browser.implisitly_wait(timeout)
        
    def open(self):
        self.browser.get(self.url)
        
    def is_find_element(self, how, what):
        try:
            self.browser.find_element(how, what)
        except ElementNotVisibleException :
            return False
        return True
        
     def is_find_elements(self, how, what):
        return True if self.browser.find_elements(how, what) != 0 else False
    
