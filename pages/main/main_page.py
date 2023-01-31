from .locators import MainPageLocators
from pages.news.news_page import NewsPageInMain


class MainPage(NewsPageInMain):
    def should_be_main_page(self):
        self.is_title_main_page_present()
        self.is_news_list_present()
        self.is_news_page_navbar_present()
        self.is_site_map_is_present()

    def get_refs_site_map(self):
        self.is_site_map_ref_accessible()
        ref = self.browser.find_elements(*MainPageLocators.REFERENCES_SITE_MAP)
        href = [el.get_attribute('href') for el in ref]
        return href

    def go_news_page_from_site_map(self):
        ref = self.browser.find_elements(*MainPageLocators.REF_NEWS_PAGE_IN_SITE_MAP)
        ref.click()

    def is_site_map_is_present(self):
        assert self.find_element(*MainPageLocators.SITE_MAP), "Site map is not presented!"

    def is_site_map_ref_accessible(self):
        assert self.find_elements(*MainPageLocators.REFERENCES_SITE_MAP), "References in site map is not presented!"

    def is_title_main_page_present(self):
        assert self.find_element(*MainPageLocators.TITLE_PAGE)



