from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, browser, url, timeout = 5):
        self.browser = browser
        self.url = url
        self.browser.implisitly_wait(timeout)
        
    def open(self):
        self.browser.get(self.url)
        
    def is_find_element(self, how, what):
        try:
            self.browser.find_elements(how, what)
        except :
            return False
        return True
