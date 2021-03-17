from pages.django_pages.base_page import BasePage
from locators.django_locators.main_page_locator import MainPageLocator


class MainPage(BasePage):

    def open_login_page(self):
        admin = self.find_element(
            MainPageLocator.LOCATOR_GO_TO_ADMIN_BTN)
        admin.click()
