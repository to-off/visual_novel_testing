import time

from generator.generator import generated_person
from pages.profile.BaseRegPage import BasePage
from locators.form_page_locators import FormPageLocators as locators
from locators.auth_page_locators import AuthPageLoc as locator


class FormPage(BasePage):
    person = generated_person()

    def fill_fields_and_submit(self):

        #self.person = generated_person()

        self.element_is_visible(locators.USERNAME).send_keys(self.person.username)
        self.element_is_visible(locators.PASSWORD1).send_keys(self.person.password1)
        self.element_is_visible(locators.PASSWORD2).send_keys(self.person.password1)
        self.element_is_visible(locators.EMAIL).send_keys(self.person.email)
        self.element_is_visible(locators.BUTTON).click()
        return self.person.username, self.person.password1, self.person.email
        time.sleep(15)


    def to_test_in(self):

        self.element_is_visible(locator.LOGIN).send_keys(self.person.username)
        self.element_is_visible(locator.PASSW).send_keys(self.person.password1)
        time.sleep(5)