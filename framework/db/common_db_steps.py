import allure
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class BaseDBSteps(object):
    def __init__(self, db_url):
        self.bind = create_engine(db_url)
        self.session = Session(bind=self.bind, autoflush=True, autocommit=True)

    @allure.step
    def fetch_all(self, sql, attach_to_report=False):
        if attach_to_report:
            allure.attach(str(sql), 'sql')
        return self.session.execute(sql).fetchall()

    def execute(self, sql, attach_to_report=False):
        if attach_to_report:
            allure.attach(str(sql), 'sql')

        self.session.execute(sql)
