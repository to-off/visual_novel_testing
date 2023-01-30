
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def pytest_addoption(parser):
    parser.addoption('--resolution', action='store', default="def",
                     help="Choose resolution browser: def or max")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: en, es, fr, ru... etc")


@pytest.fixture(scope="function")
def browser(request):
    resolution = request.config.getoption("resolution")
    language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print(f'\nstart browser for test (lenguage={language}, resolution={resolution})')

    browser = webdriver.Chrome()
    if resolution == 'max':
        browser.maximize_window()

    yield browser
    print("\nquit browser..")
    browser.quit()

    
@pytest.fixture
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()
