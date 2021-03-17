from framework.db.common_db_steps import BaseDBSteps
from sqlalchemy import text


class DBSteps(BaseDBSteps):
    def group_creation(self, group_name):
        sql = text(f"""
            insert into public.auth_group (name) values ('{group_name}')
            """)
        self.execute(sql)

    def get_user_in_group(self, group_name, username):
        sql = f"""
            SELECT aug.id FROM public.auth_user au
            left join public.auth_user_groups aug
                on au.id=aug.user_id 
            left join public.auth_group ag
                on ag.id=aug.group_id 
            WHERE au.username in ('{username}')
                and ag.name in ('{group_name}')
            """
        resp = self.fetch_all(sql)
        assert len(resp) != 0, f"user '{username}' is not in " \
            f"the group '{group_name}'"

    def user_group_delete(self, group_name, username):
        sql = text(f"""
            delete from public.auth_user_groups
            where id in (
                select aug.id
                from public.auth_group ag
                left join public.auth_user_groups aug on
                    ag.id = aug.group_id
                left join public.auth_user au on
                    au.id = aug.user_id
                where
                    ag.name = '{group_name}'
                    and au.username = '{username}')
            """)
        self.execute(sql)

    def group_delete(self, group_name):
        sql = text(f"""
            delete from public.auth_group where name = '{group_name}'
            """)
        self.execute(sql)

    def user_delete(self, username):
        sql = text(f"""
            delete from public.auth_user where username = '{username}'
            """)
        self.execute(sql)
