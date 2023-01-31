from pages.chart.branches_func import BranchesFunction
from pages.chart.locators import NovelPageLocators
from selenium.common.exceptions import InvalidElementStateException

class NovelPage(BranchesFunction):
    def click_on_characteristic_element(self, characteristic_num, el_num): # Производится нажатие на содержимое под заданным номером из характеристики под назаднным номером
        self.should_be_characteristic(characteristic_num)
        self.is_characteristic_element_exist(characteristic_num, el_num)
        try:
            names_list = self.get_names_of_characteristics()
            spec_info = self.browser.find_elements(*NovelPageLocators.content(names_list[characteristic_num]))
            spec_info[el_num].click()
        except InvalidElementStateException:
            return "This characteristic is not clickable"

    def get_content_of_characteristic(self, characteristic_num): # Возвращает список содержимого, находящегося под заданной характеристикой
        self.should_be_characteristic(characteristic_num)
        names_list = self.get_names_of_characteristics()
        characteristics = self.browser.find_elements(*NovelPageLocators.content(names_list[characteristic_num]))
        info_list = [x.text for x in characteristics if len(x.text) > 0]
        return info_list

    def get_names_of_characteristics(self): # Возвращает список характеристик
        self.is_element_present(*NovelPageLocators.CHARACTERISTIC_ELEMS_LOCATOR)
        characteristics_names = self.browser.find_elements(*NovelPageLocators.CHARACTERISTIC_ELEMS_LOCATOR)
        names_list = [x.text for x in characteristics_names if len(x.text) > 0]
        return names_list

    def open_screenshot(self, scr_num): # Нажимаем на скриншот под заданным номером
        self.should_be_screenshot(scr_num)
        scr = self.browser.find_elements(*NovelPageLocators.SCREENSHOTS_LOCATOR)
        scr[scr_num].click()

    def get_screenshots_count(self): # Возвращает количество скриншотов на странице
        self.is_elements_present(*NovelPageLocators.SCREENSHOTS_LOCATOR)
        scr = self.browser.find_elements(*NovelPageLocators.SCREENSHOTS_LOCATOR)
        return len(scr)

    def should_be_screenshot(self, scr_num): # Проверка на то существует ли скриншот под заданным номером
        assert scr_num in range(0,
                                self.get_screenshots_count()), "The novel does not have a screenshot under this number"

    def should_be_characteristic(self, characteristic_num): # Проверка на существование заданной характеристики
        names_list = self.get_names_of_characteristics()
        assert characteristic_num in range(0, len(names_list)), "The novel has no such characteristic"

    def is_characteristic_element_exist(self, characteristic_name, el_num): # Проверка на существование элемента заданной характеристики
        assert el_num in range(0, len(
            self.get_content_of_characteristic(characteristic_name))), "There is no such characteristic of the novel"

    def switch_screenshot_left(self): # Открывает предыдущий скриншот
        self.is_element_present(*NovelPageLocators.ARROW_LEFT_LOCATOR)
        arrow_btn = self.browser.find_element(*NovelPageLocators.ARROW_LEFT_LOCATOR)
        arrow_btn.click()

    def switch_screenshot_right(self): # Открывает следующий скриншот
        self.is_element_present(*NovelPageLocators.ARROW_RIGHT_LOCATOR)
        arrow_btn = self.browser.find_element(*NovelPageLocators.ARROW_RIGHT_LOCATOR)
        arrow_btn.click()

    def get_screenshot_src(self): #Позволяет получить ссылку на скрин
        self.is_element_present(*NovelPageLocators.SCREENSHOT_SRC)
        screenshot_src = self.browser.find_element(*NovelPageLocators.SCREENSHOT_SRC)
        return screenshot_src.get_attribute("src")

    def close_shreenshot(self):
        self.is_element_present(*NovelPageLocators.CLOSE_BUTTON_LOCATOR, 5)
        btn_close = self.browser.find_element(*NovelPageLocators.CLOSE_BUTTON_LOCATOR)
        btn_close.click()
