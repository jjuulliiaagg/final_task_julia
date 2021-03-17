from pages.django_pages.base_page import BasePage
from locators.django_locators.admin_page_locator import AdminPageLocator


class AdminPage(BasePage):

    def admin_is_present(self):
        admin_f = self.find_element(AdminPageLocator.LOCATOR_ADMIN_TITLE).text
        assert admin_f == 'Site administration'

    def open_groups(self):
        self.find_element(AdminPageLocator.LOCATOR_GROUPS_LINK).click()

    def groups_is_present(self):
        group_f = self.find_element(AdminPageLocator.LOCATOR_GROUPS_TITLE).text
        assert group_f == 'Select group to change'

    #def find_group_in_list(self, group_name, exist=False):
    def find_group_in_list(self, exist=False):
        group_list = self.find_elements(AdminPageLocator.LOCATOR_GROUPS_TABLE)
        for group in group_list:
            if 'test' in group.text:
                exist = True
        # assert group_name in group_list
        assert exist, "group not found"

        print(group_list)

    def open_add_user(self):
        add_user = self.find_element(AdminPageLocator.LOCATOR_ADD_USER)
        add_user.click()
