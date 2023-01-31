from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

'''
Класс с основными методами браузера и его определением
'''


class BrowserFunction:
    def __init__(self, browser, url='', timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what, time=5):
        try:
            WebDriverWait(self.browser, time).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_elements_present(self, how, what, time=5):
        try:
            WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)


















