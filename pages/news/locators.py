from selenium.webdriver.common.by import By


class NewsPageLocators:
    ACTIVE_PAGINATION_NEWS = lambda num: (By.CSS_SELECTOR, f'#news-list-table ul.pagination li:nth-child({num})')
    MAIN = (By.CSS_SELECTOR, 'div>h3>a:first-of-type')
    NEWS_LIST = (By.CSS_SELECTOR, '#news-list-table div.title a')
    NEWS_POST = lambda num: (By.CSS_SELECTOR, f'tr.news:nth-child({num}) div.title a')
    PAGINATION_NEWS = (By.CSS_SELECTOR, f'#news-list-table ul.pagination a')
    PAGE_NEWS = lambda num: (By.CSS_SELECTOR, f'#news-list-table ul.pagination li:nth-child({num}) a')

    REFERENCES_ON_DESCRIPTION_NEWS = (By.CSS_SELECTOR, '#news-list-table div.short_description a')
