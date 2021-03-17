from framework.api.petstore_api_steps import PetstoreUser


def test_petstore_api(api_setup):
    user_data = api_setup
    p_user = PetstoreUser()
    p_user.create_user(user_data)
    p_user.user_login(user_data['username'], user_data['password'])
    p_user.get_correct_user_data(user_data)
    p_user.user_logout()
    p_user.delete_user(user_data['username'])
