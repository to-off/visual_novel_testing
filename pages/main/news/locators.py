from selenium.webdriver.common.by import By

class NewsPageLocators():
    MAIN = (By.CSS_SELECTOR, 'div>h3>a:first-of-type')
    NEWS_LIST = (By.CSS_SELECTOR, '#news-list-table div.title a')
    PAGINATION_NEWS = (By.CSS_SELECTOR, '#news-list-table ul.pagination a')
    REFERENCES_ON_DESCRIPTION_NEWS = (By.CSS_SELECTOR, '#news-list-table div.short_description a')
