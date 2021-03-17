from selenium.webdriver.common.by import By


class AddUserPageLocator:

    LOCATOR_ADD_USER_TITLE = (By.XPATH, '//div[@id="content"]/h1')
    LOCATOR_CHANGE_USER_TITLE = (By.XPATH, '//div[@id="content"]/h1')
    LOCATOR_USERNAME_FIELD = (By.XPATH, '//input[@name="username"]')
    LOCATOR_PASSWD_FIELD = (By.XPATH, '//input[@name="password1"]')
    LOCATOR_C_PASSWD_FIELD = (By.XPATH, '//input[@name="password2"]')
    LOCATOR_SAVE_BTN = (By.XPATH, '//input[@class="default"]')
    LOCATOR_GROUPS_LIST = (By.XPATH, '//select[@id="id_groups_from"]')
    LOCATOR_ADD_CHOSEN_GROUP = (By.XPATH, '//a[@id="id_groups_add_link"]')
