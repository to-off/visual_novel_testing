from selenium import webdriver
from selenium.webdriver.common.by import By

class BaseChartLocators():
    CHART_LOCATOR = (By.CSS_SELECTOR, "div>h3>a:last-of-type")

class ChartPageLocators():
    BTNS_LOCATOR = (By.CSS_SELECTOR, ".btn-primary")
    IMGS_LOCATOR = (By.CSS_SELECTOR, ".poster-img")
    SORTING_LOCATOR = (By.CSS_SELECTOR, "[class='btn btn-default']")
    FILTER_LOCATOR = (By.CSS_SELECTOR,"a.dropdown-toggle")
    DD_ELEMS_LOCATOR = (By.CSS_SELECTOR, "div.open>ul>li")
        
        
class ChartFilteredPageLocators():
    pass
    

class ChartNovelPageLocators():
    SPEC_ELEMS_LOCATOR = (By.XPATH,"//span[contains(@class,'sh-desc')][not(child::strong)][not(child::img)]")
    SCREENSHOTS_LOCATOR = (By.XPATH,".gallery-item")
    def spec_elems(spec_elem):
        return (By.XPATH, f"//*[contains(text(), '{spec_elem}')]/following-sibling::a")
    