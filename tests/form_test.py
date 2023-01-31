import requests
from pages.form_page import FormPage
from pages.auth_page import AuthPage


class TestFormPage:

    def test_form(self, driver): #регистрация
        form_page = FormPage(driver, 'http://127.0.0.1:8000/signup/')
        form_page.open()
        data_user = [i for i in form_page.fill_fields_and_submit()]
        print(data_user)
        path = rf'/home/alexander96/Рабочий стол/final/people1.txt'
        file = open(path, 'w')
        for i in data_user:
            file.write(' ')
            file.write(i)
        file.close()
        auth_page = FormPage(driver, 'http://127.0.0.1:8000/login/')
        auth_page.open()
        auth_page.to_test_in()
        res = requests.get('http://127.0.0.1:8000/login/').status_code
        assert res == 200

class TestAuthPage:

    def test_come_in(self, driver): #вход
        auth_page = AuthPage(driver, 'http://127.0.0.1:8000/login/')
        auth_page.open()
        auth_page.to_come_in()
