from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.browser_func import BrowserFunction
from pages.news.locators import NewsPageLocators


class NewsPageInMain(BrowserFunction):

    def change_news_pagination(self, number):
        pagination = self.browser.find_element(*NewsPageLocators.PAGE_NEWS(number))
        pagination.click()
        WebDriverWait(self.browser, 5).until(EC.text_to_be_present_in_element_attribute(NewsPageLocators.ACTIVE_PAGINATION_NEWS(number), 'class', 'active'))

    def get_news_list(self):
        self.is_news_list_present()
        return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located(NewsPageLocators.NEWS_LIST))

    def get_pagination_news(self):
        return self.browser.find_elements(*NewsPageLocators.PAGINATION_NEWS)

    def go_news_post(self, number):
        self.is_news_post_present(number)
        news_post = self.browser.find_element(*NewsPageLocators.NEWS_POST(number))
        news_post.click()

    def is_news_post_present(self, number):
        assert self.is_visibility(*NewsPageLocators.NEWS_POST(number)), f"News post number {number} is not exists"

    def is_news_list_present(self):
        assert self.is_visibility(*NewsPageLocators.NEWS_LIST), "News list is not find"

    def is_news_page_navbar_present(self):
        assert self.is_visibility(*NewsPageLocators.PAGINATION_NEWS), "Pagination news is not find"


class NewsPage(NewsPageInMain):
    def go_to_main_page(self):
        ref_main_page = self.browser.find_element(*NewsPageLocators.MAIN)
        ref_main_page.click()

    def should_be_news_page(self):
        assert 'news/all' in self.browser.current_url, "URL is not correct"
        self.is_news_list_present()
        self.is_news_page_navbar_present()
