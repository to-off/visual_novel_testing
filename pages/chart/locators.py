from selenium.webdriver.common.by import By


class ChartPageLocators():
    BTNS_LOCATOR = (By.CSS_SELECTOR, ".btn-primary")
    IMGS_LOCATOR = (By.CSS_SELECTOR, ".poster-img")
    SORTING_LOCATOR = (By.CSS_SELECTOR, "[class='btn btn-default']")
    FILTER_LOCATOR = (By.CSS_SELECTOR, "a.dropdown-toggle")
    DD_ELEMS_LOCATOR = (By.CSS_SELECTOR, "div.open>ul>li")
    DROPDOWN_LOCATOR = (By.CSS_SELECTOR, ".open")
    NOVEL_COVER_LOCATOR = (By.CSS_SELECTOR, ".hero-feature")
    FILTER_SELECTED_LOCATOR = (By.CSS_SELECTOR, "div.open")
    def btn(number):
        return By.CSS_SELECTOR, f".btn-primary:nth-child({number+1})"

class BranchesLocator():
    CHART_LOCATOR = (By.CSS_SELECTOR, "div>h3>a:last-of-type")


class NovelPageLocators():
    CHARACTERISTIC_ELEMS_LOCATOR = (By.XPATH, "//span[contains(@class,'sh-desc')][not(child::strong)][not(child::img)]")
    SCREENSHOTS_LOCATOR = (By.CSS_SELECTOR, ".gallery-item")
    ARROW_LEFT_LOCATOR = (By.CSS_SELECTOR, "button.mfp-arrow-left")
    ARROW_RIGHT_LOCATOR = (By.CSS_SELECTOR, "button.mfp-arrow-right")
    CLOSE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button.mfp-close")
    SCREENSHOT_SRC = (By.CSS_SELECTOR, "img.mfp-img")

    def content(name):
        return By.XPATH, f"//*[contains(text(), '{name}')]/following-sibling::a"
