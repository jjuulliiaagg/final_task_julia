import allure
from pages.django_pages.main_page import MainPage
from time import sleep


@allure.story("Open admin")
def test_open_admin(browser):
    with allure.step('Open main page'):
        main_page = MainPage(browser)
    with allure.step('Open admin page'):
        main_page.open_base_page()
    print('ok')
    sleep(5)
