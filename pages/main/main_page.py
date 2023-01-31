from locators import MainPageLocators
from pages.news.news_page import NewsPageInMain

class MainPage(NewsPageInMain):
    def is_visibility(self):
        assert self.is_find_element(*MainPageLocators.SITE_MAP), "Site map is not presented!"
    
    def is_ref_accessible(self):
        assert self.is_find_elements(*MainPageLocators.REFERENCES_SITE_MAP), "Href in site map is not presented!"
    
    def get_refs(self):
        ref = self.browser.find_elements(*MainPageLocators.REFERENCES_SITE_MAP)
        href = [el.get_attribute('href') for el in ref]
        return href
        
