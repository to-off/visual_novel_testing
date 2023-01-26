from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from .locators import NewsPageLocators

class NewsPage(BasePage):
    def go_to_main_page(self):
        href_main_page = self.browser.find_element(*NewsPageLocators.MAIN)
        href_main_page.click()
        
    def is_news_list_present(self):
        try:
            self._news_list = self.browser.find_elements(*NewsPageLocators.NEWS_LIST)
        except :
            return False
        return True
        
    def change_news_pageination(self, number):
    	self._page_clickabel = number
        pagination = self.browser.find_elements(*NewsPageLocators.PAGINATION_NEWS)
        if pagination[number].get_attribute('active') == 'true':
            print('Click on active page button')
        pagination[numder].click()
                
    def is_btn_news_page_change_active(self, number):
        pagination = self.browser.find_elements(*NewsPageLoators.PAGINATION_NEWS)
        if pagination[number].get_attribute('active') == 'true':
            return True
        return False
        
                
    def is_news_page_changes(self):
        new_news_list = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(NewsPageLocators.NEWS_LIST))
        if self._news_list != new_news_list:
            return True
        return False
        
        
        
