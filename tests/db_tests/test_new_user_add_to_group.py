from conftest import db_steps
from pages.django_pages.main_page import MainPage
from pages.django_pages.login_page import LoginPage
from pages.django_pages.admin_page import AdminPage
from pages.django_pages.add_user_page import AddUserPage
from time import sleep
import allure


@allure.story("Check that Group assigned to User is sent to DB")
def test_add_user_to_group(browser, setup_teardown):
    group_name, username, password, config = setup_teardown
    with allure.step("Open base page"):
        main_page = MainPage(browser)
        main_page.open_base_page()
    with allure.step("Open login page"):
        main_page.open_login_page()
        login_page = LoginPage(browser)
    with allure.step("Check that login page is presented"):
        login_page.login_is_present()
        sleep(1)
    with allure.step("Login to the system"):
        login_page.login(config)
        admin_page = AdminPage(browser)
    with allure.step("Check that admin page is presented"):
        admin_page.admin_is_present()
        sleep(1)
    with allure.step("Open add user page"):
        admin_page.open_add_user()
        adduser_page = AddUserPage(browser)
    with allure.step("Check that add user page is presented"):
        adduser_page.adduser_is_present()
    with allure.step("Add new user to group"):
        adduser_page.add_user_and_group(username, group_name, password)
    with allure.step("Check that added user to group is displayed in DB"):
        db_steps.get_user_in_group(group_name, username)
