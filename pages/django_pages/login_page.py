from pages.django_pages.base_page import BasePage
from locators.django_locators.login_page_locator import LoginPageLocator


class LoginPage(BasePage):

    def login_is_present(self):
        login_f = self.find_element(LoginPageLocator.LOCATOR_LOGIN_TITLE).text
        assert login_f == 'Django administration',\
            f"{login_f} is not equal 'Django administration'"

    def login(self, config):
        username = self.find_element(LoginPageLocator.LOCATOR_USERNAME_FIELD)
        username.send_keys(config['ID'])
        passwd = self.find_element(LoginPageLocator.LOCATOR_PASSWORD_FIELD)
        passwd.send_keys(config['PW'])
        sign_btn = self.find_element(LoginPageLocator.LOCATOR_LOG_IN_BTN)
        sign_btn.click()
