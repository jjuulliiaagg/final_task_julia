import allure
from framework.api.petstore_api_steps import PetstoreUser


@allure.story("User creation, login, get user info, logout and user delete")
def test_petstore_api(api_setup):
    user_data = api_setup
    p_user = PetstoreUser()
    with allure.step("Create User"):
        p_user.create_user(user_data)
    with allure.step("Login under created user"):
        p_user.user_login(user_data['username'], user_data['password'])
    with allure.step("Get user info"):
        p_user.get_correct_user_data(user_data)
    with allure.step("User logout"):
        p_user.user_logout()
    with allure.step("User delete"):
        p_user.delete_user(user_data['username'])
