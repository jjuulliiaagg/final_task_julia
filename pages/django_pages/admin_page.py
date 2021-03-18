from pages.django_pages.base_page import BasePage
from locators.django_locators.admin_page_locator import AdminPageLocator


class AdminPage(BasePage):

    def admin_is_present(self):
        admin_f = self.find_element(AdminPageLocator.LOCATOR_ADMIN_TITLE).text
        assert admin_f == 'Site administration',\
            f"{admin_f} is not equal 'Site administration'"

    def open_groups(self):
        self.find_element(AdminPageLocator.LOCATOR_GROUPS_LINK).click()

    def groups_is_present(self):
        group_f = self.find_element(AdminPageLocator.LOCATOR_GROUPS_TITLE).text
        assert group_f == 'Select group to change',\
            f"{group_f} is not equal 'Select group to change'"

    def find_group_in_list(self, group_name, exist=False):
        group_list = self.find_elements(AdminPageLocator.LOCATOR_GROUPS_TABLE)
        for group in group_list:
            if group_name in group.text:
                exist = True
                break
        assert exist, f"{group_name} group is not found in the list"

        print(group_list)

    def open_add_user(self):
        add_user = self.find_element(AdminPageLocator.LOCATOR_ADD_USER)
        add_user.click()
