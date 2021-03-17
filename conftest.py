import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import DB_URL
from framework.db.postgres.db_steps import DBSteps


@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    # browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

#
# def conn():
#     pass
#
#
# def create_group_db(conn):
#     pass

db_steps = DBSteps(DB_URL)

