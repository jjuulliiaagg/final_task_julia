from selenium.webdriver.common.by import By


class AdminPageLocator:

    LOCATOR_ADMIN_TITLE = (By.XPATH, '//div[@id="content"]/h1')
    LOCATOR_GROUPS_LINK = (By.XPATH, '//a[@href="/admin/auth/group/"]')
    LOCATOR_GROUPS_TITLE = (By.XPATH, '//div[@id="content"]/h1')
    LOCATOR_GROUPS_TABLE = (By.CLASS_NAME, 'field-__str__')
    LOCATOR_ADD_USER = (By.XPATH, '//a[@href="/admin/auth/user/add/"]')
