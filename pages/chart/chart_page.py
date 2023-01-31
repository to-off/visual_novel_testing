from pages.general_func import GeneralFunction
from .locators import ChartPageLocators
from selenium.common.exceptions import NoSuchAttributeException


class ChartPage(GeneralFunction):
    def click_on_filter(self, filter_num):  # Находим и выполняем нажатие на фильтр под заданным номером
        self.is_filters_menu_element_exists(filter_num)
        dropdown_list = self.browser.find_elements(*ChartPageLocators.FILTER_LOCATOR)
        dropdown_list[filter_num].click()

    def click_on_filter_type(self, filter_type_num):  # Находим и выполняем нажатие на тип фильтра под заданным номером
        self.is_filter_type_exists(filter_type_num)
        ftype_list = self.browser.find_elements(*ChartPageLocators.DD_ELEMS_LOCATOR)
        ftype_list[filter_type_num].click()

    def go_to_novel_page_by_btn(self, title_num):  # Переход на новеллу под заданным номером по кнопке
        self.is_novel_exists(title_num)
        try:
            btn = self.browser.find_element(*ChartPageLocators.btn(title_num))

            #_ = btn.location_once_scrolled_into_view
            #self.browser.execute_script("return arguments[0].scrollIntoView(true);", novels_btn_list[title_num])
            #self.browser.execute_script("window.scrollBy(0, 100);")
            btn.click()
        except NoSuchAttributeException:
            return "This element is not clickable now"

    def go_to_novel_page_by_img(self, title_num):  # Переход на новеллу под заданным номером по постеру
        self.is_novel_exists(title_num)
        try:
            novels_img_list = self.browser.find_elements(*ChartPageLocators.IMGS_LOCATOR)
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", novels_img_list[title_num])
            novels_img_list[title_num].click()
        except NoSuchAttributeException:
            return "This element is not clickable now"

    def filter_by(self, filter_num, filter_type_num):  # Сортировка по
        self.click_on_filter(filter_num)
        self.click_on_filter_type(filter_type_num)

    def get_sort_menu(self):  # Возвращает список с названиями элементов сортировочного меню
        self.is_element_present(*ChartPageLocators.SORTING_LOCATOR)
        sorting_list = self.browser.find_elements(*ChartPageLocators.SORTING_LOCATOR)
        sort_menu = [x.text for x in sorting_list if len(x.text) > 0]
        return sort_menu

    def get_filters_menu(self):  # Возвращает список с названиями элементов меню фильтрации
        self.is_element_present(*ChartPageLocators.DROPDOWN_LOCATOR)
        dropdown_list = self.browser.find_elements(*ChartPageLocators.FILTER_LOCATOR)
        filter_menu = [x.text for x in dropdown_list if len(x.text) > 0]
        return filter_menu

    def get_filter_types(self):  # Возвращает список с названиями типов выбранного фильтра
        self.is_filter_selected()
        ftype_list = self.browser.find_elements(*ChartPageLocators.DD_ELEMS_LOCATOR)
        type_list = [x.text for x in ftype_list if len(x.text) > 0]
        return type_list

    def get_novels_count(self):  # Возвращает количество новелл на данной странице
        novels = self.browser.find_elements(*ChartPageLocators.IMGS_LOCATOR)
        return len(novels)

    def is_filters_menu_element_exists(self,
                                       filter_num):  # Проверяет существует ли фильтр из списка под заданным номером
        assert filter_num in range(0, len(self.get_filters_menu())), "The number of this filter does not exists"

    def is_filter_type_exists(self,
                              filter_type_num):  # Проверяет существует ли тип выбранного фильтра под заданным номером
        self.is_filter_selected()
        assert filter_type_num in range(0,
                                        len(self.get_filter_types())), "The number of this filter type does not exists"

    def is_sorting_exists(self,
                          sorting_type_num):  # Проверяет существует ли данный номер сортировки в панеле сортировок
        assert sorting_type_num in range(0, len(self.get_sort_menu())), "The number of this sort does not exist"

    def is_novel_exists(self,
                        title_num):  # Проверяет существует ли данный номер новеллы в диапазоне от 0 до числа новелл на странице
        assert title_num in range(0, self.get_novels_count()), "There is no novel under this number"

    def is_sorted_link_correct(self):  # Проверяет на то выполняется ли сортировка
        assert "?sort=" in self.browser.current_url, "This page is not sorted"

    def is_filter_selected(self):  # Проверяет выбран ли фильтр
        self.is_element_present(*ChartPageLocators.FILTER_SELECTED_LOCATOR)

    def is_sorted_in_descending_order(
            self):  # Функция возвращает True в случае если отсортированно по убыванию или False в обратном случае
        self.is_sorted_link_correct()  # Перед выполнением необходимо проверить выполнена ли вообще сортировка
        if "?sort=-" in self.browser.current_url:
            return True
        return False

    def should_be_chart_page_url(self):  # проверка правильности URL страницы чарта
        assert "/chart" in self.browser.current_url, "This is not a chart page"

    def sort_by(self, sorting_type_num):  # Сортировка по
        self.is_sorting_exists(sorting_type_num)
        sorting_list = self.browser.find_elements(*ChartPageLocators.SORTING_LOCATOR)
        sorting_list[sorting_type_num].click()
