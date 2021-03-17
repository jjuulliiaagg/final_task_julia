import requests

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

params = {
            "username": "julia_g",
            "password": "Ty4kayes"
        }


class PetstoreUser:
    def get_headers(self):
        headers = {
            'Accept': 'application/json'
        }
        return headers

    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2/user'
        self.headers = self.get_headers()

    def create_user(self, user_data):
        url = self.base_url
        json = user_data
        response = requests.request("POST", url, json=json)
        json_response = response.json()
        assert json_response['code'] == 200,\
            f'{json_response["code"]} not equal code 200'
        print('created')
        return json_response

    def user_login(self, params):
        url = self.base_url + '/login'
        params = params
        response = requests.request("GET", url, headers=self.headers,
                                    params=params)
        json_response = response.json()
        assert json_response['code'] == 200 \
               and 'logged in user session' in json_response['message'],\
            f'{json_response["code"]} not equal code 200 or no success message'
        print('logged')
        return json_response

    def get_correct_user_data(self, username):
        url = self.base_url + f'/{username}'
        response = requests.request("GET", url, headers=self.headers)
        json_response = response.json()
        assert json_response == user_data, f'{json_response} invalid user_data'
        print('data')
        return json_response

    def get_invalid_user_data(self, username):
        url = self.base_url + f'/{username}'
        response = requests.request("GET", url, headers=self.headers)
        json_response = response.json()
        assert json_response['message'] == 'User not found',\
            f'{json_response} invalid user_data'
        return json_response

    def user_logout(self):
        url = self.base_url + '/logout'
        response = requests.request("GET", url, headers=self.headers)
        json_response = response.json()
        assert json_response['code'] == 200 and \
            json_response['message'] == 'ok', \
            f'{json_response["code"]} not equal code 200 or no ok message'
        print('logout')
        return json_response

    def correct_delete_user(self, username):
        url = self.base_url + f'/{username}'
        response = requests.request("DELETE", url, headers=self.headers)
        json_response = response.json()
        assert json_response['code'] == 200 \
            and json_response['message'] == f'{username}',\
            f'{json_response["code"]} not equal 200 or no {username} message'
        print('deleted')
        return json_response


# usr = PetstoreUser()
# usr.create_user(user_data)
# usr.user_login(params)
# usr.get_correct_user_data(user_data['username'])
# usr.get_invalid_user_data(user_data['firstName'])
# usr.user_logout()
# usr.correct_delete_user(user_data['username'])
