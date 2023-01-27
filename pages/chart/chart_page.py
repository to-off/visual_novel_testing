from pages.chart.general_func import GeneralFunction
from .locators import ChartPageLocators

class ChartPage(GeneralFunction):
    def go_to_novel_page_by_btn(self, title_num):
        novels_btn_list = self.browser.find_elements(*ChartPageLocators.BTNS_LOCATOR)
        novels_btn_list[title_num].click()
        
    def go_to_novel_page_by_img(self, title_num):
        novels_img_list = self.browser.find_elements(*ChartPageLocators.IMGS_LOCATOR)
        novels_img_list[title_num].click()

    def sort_by(self, sorting_type_num):
        sorting_list = self.browser.find_elements(*ChartPageLocators.SORTING_LOCATOR)
        sorting_list[sorting_type_num].click()
        
    def filter_by(self, filter_num, filter_type_num):
        dropdown_list = self.browser.find_elements(*ChartPageLocators.FILTER_LOCATOR)
        dropdown_list[filter_num].click()
        ftype_list = self.browser.find_elements(*ChartPageLocators.DD_ELEMS_LOCATOR)
        ftype_list[filter_type_num].click()
        
    def get_sort_menu(self):
        sorting_list = self.browser.find_elements(*ChartPageLocators.SORTING_LOCATOR)
        sort_menu = [x.text for x in sorting_list if len(x.text) > 0]
        return sort_menu
        
    def get_filter_menu(self):
        dropdown_list = self.browser.find_elements(*ChartPageLocators.FILTER_LOCATOR)
        filter_menu = [x.text for x in dropdown_list if len(x.text) > 0]
        return filter_menu
        
    def get_filter_types(self, filter_num):
        dropdown_list = self.browser.find_elements(*ChartPageLocators.FILTER_LOCATOR)
        dropdown_list[filter_num].click()
        ftype_list = self.browser.find_elements(*ChartPageLocators.DD_ELEMS_LOCATOR)
        type_list = [x.text for x in ftype_list if len(x.text) > 0]
        return type_list
