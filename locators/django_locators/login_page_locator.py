from selenium.webdriver.common.by import By


class LoginPageLocator:

    LOCATOR_LOGIN_TITLE = (By.XPATH, '//a[@href="/admin/"]')
    LOCATOR_USERNAME_FIELD = (By.XPATH, '//input[@id="id_username"]')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//input[@id="id_password"]')
    LOCATOR_LOG_IN_BTN = (By.XPATH, '//input[@type="submit"]')
