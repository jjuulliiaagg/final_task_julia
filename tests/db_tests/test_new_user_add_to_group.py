from conftest import db_steps
from pages.django_pages.main_page import MainPage
from pages.django_pages.login_page import LoginPage
from pages.django_pages.admin_page import AdminPage
from pages.django_pages.add_user_page import AddUserPage
from time import sleep


def test_add_user_to_group(browser, setup_teardown):
    group_name, username, password, config = setup_teardown

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
    admin_page.open_add_user()
    adduser_page = AddUserPage(browser)
    adduser_page.adduser_is_present()
    adduser_page.add_user_and_group(username, group_name, password)
    db_steps.get_user_in_group(group_name, username)
