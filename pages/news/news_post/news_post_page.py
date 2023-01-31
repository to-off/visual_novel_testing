from pages.base_func import BasePage

class NewsPostPage(BasePage):
    def go_to_main_page(self):
        ref_main_page = self.browser.find_element(*NewsPostPageLocators.MAIN)
        ref_main_page.click()
        
    def go_to_news_page(self):
        ref_main_page = self.browser.find_element(*NewsPostPageLocators.NEWS)
        ref_main_page.click() 
        
    def get_ref_in_news(self):
        ref_description = self.browser.find_elements(*NewsPostPageLocators.REFERENCES_ON_DESCRIPTION_NEWS)
        return [ref_desc.get_attribute('href') for el in ref_description]
