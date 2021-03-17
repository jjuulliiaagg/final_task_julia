from pages.django_pages.base_page import BasePage
from locators.django_locators.login_page_locator import LoginPageLocator


class LoginPage(BasePage):

    def login_is_present(self):
        login_f = self.find_element(LoginPageLocator.LOCATOR_LOGIN_TITLE).text
        assert login_f == 'Django administration'

    #def login(self, user_name, user_passwd):
    def login(self):
        username = self.find_element(LoginPageLocator.LOCATOR_USERNAME_FIELD)
        username.send_keys('admin')
        passwd = self.find_element(LoginPageLocator.LOCATOR_PASSWORD_FIELD)
        passwd.send_keys('password')
        sign_btn = self.find_element(LoginPageLocator.LOCATOR_LOG_IN_BTN)
        sign_btn.click()
