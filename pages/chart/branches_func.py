from pages.general_func import GeneralFunction
from .locators import BranchesLocator
from selenium.common.exceptions import NoSuchAttributeException

class BranchesFunction(GeneralFunction):
    def go_to_chart_page(self):
        try:
            chart = self.browser.find_element(*BranchesLocator.CHART_LOCATOR)
            chart.click()
        except NoSuchAttributeException:
            return "This element is not clickable now"