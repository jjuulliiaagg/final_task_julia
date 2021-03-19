import pytest
import time
import json
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import DB_URL
from framework.db.postgres.db_steps import DBSteps


db_steps = DBSteps(DB_URL)


@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
    # browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture
def setup_teardown_django():
    json_string = open('./resources/data_for_django.json', 'r').read()
    # json_string = open('../../resources/data_for_django.json', 'r').read()
    config = json.loads(json_string)

    group_name = 'gr-' + str(time.time())
    username = 'user-' + str(time.time())
    password = 'pass' + str(randint(100000, 999999))

    db_steps.group_creation(group_name)
    yield group_name, username, password, config

    db_steps.user_group_delete(group_name, username)
    db_steps.group_delete(group_name)
    db_steps.user_delete(username)


@pytest.fixture
def api_setup():
    json_string = open('./resources/data_for_petstore.json', 'r').read()
    # json_string = open('../../resources/data_for_petstore.json', 'r').read()
    user_data = json.loads(json_string)
    yield user_data
