from pages.main.main_page import MainPage
from pages.news.news_page import NewsPage
from pages.news.news_post.news_post_page import NewsPostPage
import pytest
import requests


def is_object_list_dif(list_obj1, list_obj2) -> bool:
    res = set(list_obj1) & set(list_obj2)
    return len(res) == 0


@pytest.mark.main_page
class TestCaseForMain:
    def test_status_code_200_for_url(self, url_list=['https://vn-russian.ru/', ]):
        header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0', }
        for url in url_list:
            response = requests.get(url, headers=header)
            assert response.status_code == 200, f'Failed url: {url}'

    def test_ref_in_site_map(self, browser):
        link = 'https://vn-russian.ru/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_main_page()
        self.test_status_code_200_for_url(page.get_refs_site_map())

    @pytest.mark.parametrize('page_site', [(MainPage, ''), (NewsPage, 'news/all')])
    @pytest.mark.parametrize('page_news_list', [
        pytest.param(1, marks=pytest.mark.xfail(reason="We start with '1' page =>  news list don't change")),
        2,
        pytest.param(5, marks=pytest.mark.xfail(reason="This page is not exists"))])
    def test_chang_news_list_page(self, browser, page_site, page_news_list):
        link = 'https://vn-russian.ru/' + page_site[1]
        page = page_site[0](browser, link)
        page.open()
        first_news_list = [el.text for el in page.get_news_list()]
        page.change_news_pagination(page_news_list)
        second_news_list = [el.text for el in page.get_news_list()]
        assert is_object_list_dif(first_news_list, second_news_list)

    @pytest.mark.parametrize('page_site', [(MainPage, ''), (NewsPage, 'news/all')])
    def test_back_to_news_from_news_post(self, browser, page_site):
        link = 'https://vn-russian.ru/' + page_site[1]
        page = page_site[0](browser, link)
        page.open()
        page.go_news_post(1)
        news_post_page = NewsPostPage(page.browser)
        news_post_page.go_to_news_page()

