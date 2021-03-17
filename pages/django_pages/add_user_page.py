from pages.django_pages.base_page import BasePage
from locators.django_locators.add_user_locator import AddUserPageLocator
from selenium.webdriver.support.ui import Select


class AddUserPage(BasePage):

    def adduser_is_present(self):
        adduser_f = self.find_element(AddUserPageLocator.LOCATOR_ADD_USER_TITLE).text
        assert adduser_f == 'Add user', f'{adduser_f} not equal Add user'

    def add_user_and_group(self):
        usrname = self.find_element(AddUserPageLocator.LOCATOR_USERNAME_FIELD)
        usrname.send_keys('julia')
        pswd = self.find_element(AddUserPageLocator.LOCATOR_PASSWD_FIELD)
        pswd.send_keys('11111qwe')
        c_pswd = self.find_element(AddUserPageLocator.LOCATOR_C_PASSWD_FIELD)
        c_pswd.send_keys('11111qwe')
        save = self.find_element(AddUserPageLocator.LOCATOR_SAVE_BTN)
        save.click()
        select_group = Select(self.find_element(AddUserPageLocator.LOCATOR_GROUPS_LIST))
        select_group.select_by_visible_text('test')
        user_to_group = self.find_element(AddUserPageLocator.LOCATOR_ADD_CHOSEN_GROUP)
        user_to_group.click()
        save = self.find_element(AddUserPageLocator.LOCATOR_SAVE_BTN)
        save.click()
