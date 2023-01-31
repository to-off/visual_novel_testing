from selenium.webdriver.common.by import By

class MainPageLocators:
    SITE_MAP = (By.CSS_SELECTOR, 'div.col-12:nth-child(2) ul')
    REFERENCES_SITE_MAP = (By.CSS_SELECTOR, 'div.col-12:nth-child(2) ul a')
    REF_NEWS_PAGE_IN_SITE_MAP = (By.XPATH, '///div//h4/following::a[6]')
    TITLE_PAGE = (By.XPATH, '//div//h3')


