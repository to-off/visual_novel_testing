from selenium.webdriver.common.by import By

class NewsPostPageLocators():
    MAIN = (By.CSS_SELECTOR, 'div>h3>a:first-of-type')
    NEWS = (By.CSS_SELECTOR, 'div>h3>a:nth-child(2)')    	
    REFERENCES_ON_DESCRIPTION_NEWS = (By.CSS_SELECTOR, 'div.row:nth-child(2)  > div:nth-child(1) a')
    TITLE_NEWS_POST = (By.XPATH, '//div/h3/text()[2]')
