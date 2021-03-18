from pages.django_pages.main_page import MainPage
from pages.django_pages.login_page import LoginPage
from pages.django_pages.admin_page import AdminPage
from time import sleep


def test_group_create(browser, setup):
    group_name, username, password, config = setup
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.open_login_page()
    login_page = LoginPage(browser)
    login_page.login_is_present()
    sleep(1)
    login_page.login(config)
    admin_page = AdminPage(browser)
    admin_page.admin_is_present()
    sleep(1)
    admin_page.open_groups()
    admin_page.groups_is_present()
    admin_page.find_group_in_list(group_name)
