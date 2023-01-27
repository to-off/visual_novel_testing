from pages.general_func import GeneralFunction
from .locators import BaseChartLocators

class BaseChartFunction(GeneralFunction):
    def go_to_chart_page(self):
        chart_main = self.browser.find_element(*ChartPageLocators.CHART_LOCATOR)
        chart_main.click()