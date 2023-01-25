from .base_page import BasePage
from .locators import ChartPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By


class ChartPage(BasePage):
    def go_to_main_page(self):
        main = self.browser.find_element(*ChartPageLocators.MAIN)
        main.click()
    def go_to_chart_page(self):
        chart_main = self.browser.find_element(*ChartPageLocators.CHART_MAIN)
        chart_main.click()
    def go_to_novel_page(self, title):
        detailed = self.browser.find_element(By.CSS_SELECTOR, "[title='{0}']~.p-main-vn-links > .btn-primary".format(title))
        detailed.click()
    def sort_by(self, sorting_type):
        sorting = self.browser.find_element(By.CSS_SELECTOR, "[href$='{0}']".format(sorting_type))
        sorting.click()
    def filter_by(self, filt_by, filt_type):
        dropdown_lists = self.browser.find_element(By.CSS_SELECTOR, "div.col-lg-12>div>div>.dropdown-toggle")
        for el in dropdown_lists:
            if el.text() == filter_by:
                el.click()
        f_lists = self.browser.find_element(By.CSS_SELECTOR, ".open li a")
        for el in f_lists:
            if el.text() == filter_type:
                el.click()
    