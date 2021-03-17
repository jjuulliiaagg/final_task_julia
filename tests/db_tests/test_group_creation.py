from conftest import db_steps
from pages.django_pages.main_page import MainPage
from pages.django_pages.login_page import LoginPage
from pages.django_pages.admin_page import AdminPage
from time import sleep


def test_group_create(browser):
    group_exist = db_steps.check_group_exist()
    if group_exist:
        db_steps.group_delete()
        print('Group deleted')
    db_steps.group_creation()
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.open_login_page()
    login_page = LoginPage(browser)
    login_page.login_is_present()
    sleep(1)
    login_page.login()
    admin_page = AdminPage(browser)
    admin_page.admin_is_present()
    sleep(1)
    admin_page.open_groups()
    sleep(1)
    admin_page.groups_is_present()
    admin_page.find_group_in_list()
    sleep(5)
