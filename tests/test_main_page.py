from pages.main.main_page import MainPage
from pages.news.news_page import NewsPage
from pages.news.news_post.news_post_page import NewsPostPage
import pytest
import requests


def is_object_list_dif(list_obj1, list_obj2):
    res = set(list_obj1) & set(list_obj2)
    assert len(res) == 0, "News list not changed"

def is_status_code_200_url(urls):
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0', }
    for url in urls:
        response = requests.get(url, headers=header)
        assert response.status_code == 200, f'Failed url: {url}'


@pytest.mark.main_page
class TestCaseForMain:
    def test_status_code_200_for_url(self, url_list=['https://vn-russian.ru/', ]):
        is_status_code_200_url(url_list)

    def test_ref_in_site_map(self, browser):
        link = 'https://vn-russian.ru/'
        page = MainPage(browser, link)
        page.open()
        page.is_site_map_is_present()
        is_status_code_200_url(page.get_refs_site_map())

    def test_chang_news_list_page(self, browser, page_site, page_news_list):
        link = 'https://vn-russian.ru/news/all'
        page = NewsPage(browser, link)
        page.open()
        page.is_news_list_present()
        news_list = page.get_news_list()
        page.is_news_page_navbar_present()
        for number, el in enumerate(page.get_pagination_news()):
            page.change_news_pagination(number)
            new_news_list = page.get_news_list()
            is_object_list_dif(news_list, new_news_list)

    def test_back_to_main_from_news_post(self, browser):
        link = 'https://vn-russian.ru/'
        page = MainPage(browser, link)
        page.open()
        page.is_news_post_present(1)
        page.go_news_post(1)
        news_post_page = NewsPostPage(page.browser)
        news_post_page.go_to_main_page()

    def test_back_to_news_from_news_post(self, browser):
        link = 'https://vn-russian.ru/news/all'
        page = NewsPage(browser, link)
        page.open()
        page.is_news_post_present(1)
        page.go_news_post(1)
        news_post_page = NewsPostPage(page.browser)
        news_post_page.go_to_news_page()

