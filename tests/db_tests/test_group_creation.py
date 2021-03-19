from pages.django_pages.main_page import MainPage
from pages.django_pages.login_page import LoginPage
from pages.django_pages.admin_page import AdminPage
from time import sleep
import allure


@allure.story("Check that created group in DB is isplayed in groups list")
def test_group_create(browser, setup_teardown):
    group_name, username, password, config = setup_teardown
    main_page = MainPage(browser)
    with allure.step("Open base page"):
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
    with allure.step("Open group list"):
        admin_page.open_groups()
    with allure.step("Check that page with groups is presented"):
        admin_page.groups_is_present()
    with allure.step("Check that created group from db is in group on UI"):
        admin_page.find_group_in_list(group_name)
