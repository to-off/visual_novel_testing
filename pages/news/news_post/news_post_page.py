from pages.general_func import GeneralFunction
from .locators import NewsPostPageLocators


class NewsPostPage(GeneralFunction):
    def go_to_news_page(self):
        self.is_element_present(*NewsPostPageLocators.NEWS)
        ref_main_page = self.browser.find_element(*NewsPostPageLocators.NEWS)
        ref_main_page.click() 
        
    def get_ref_in_news(self):
        ref_description = self.browser.find_elements(*NewsPostPageLocators.REFERENCES_ON_DESCRIPTION_NEWS)
        return [ref_description.get_attribute('href') for el in ref_description]

    def get_title_news_post(self):
        title_news_post = self.browser.find_element(*NewsPostPageLocators.TITLE_NEWS_POST)
        return title_news_post
