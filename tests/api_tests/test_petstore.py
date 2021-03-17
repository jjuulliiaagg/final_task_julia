from framework.api.petstore_api_steps import PetstoreUser


params = {
            "username": "julia_g",
            "password": "Ty4kayes"
        }


def test_petstore_api():
    user_data = {
        "id": 1,
        "username": "julia_g",
        "firstName": "Julia",
        "lastName": "Gahovich",
        "email": "Ty4kayes@yandex.ru",
        "password": "Ty4kayes",
        "phone": "+375298259568",
        "userStatus": 0
    }
    p_user = PetstoreUser()
    p_user.create_user(user_data)
    p_user.user_login(params)
    p_user.get_correct_user_data(user_data['username'])
    p_user.user_logout()
    p_user.correct_delete_user(user_data['username'])
