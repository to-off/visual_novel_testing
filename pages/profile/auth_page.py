import time


from pages.profile.BaseRegPage import BasePage

from locators.auth_page_locators import  AuthPageLoc as locators

class AuthPage(BasePage):

    def to_come_in(self):
        log = 'admin'
        passw = 'admin'
        self.element_is_visible(locators.LOGIN).send_keys(log)
        self.element_is_visible(locators.PASSW).send_keys(passw)
        self.element_is_visible(locators.SEND).click()
        time.sleep(5)


