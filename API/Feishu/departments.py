import requests

from API.Feishu.base import Base


class FeishuDepartments(Base):
    def teardown(self):
        pass

    def add_department(self, userid: str, name: str, mobile: str, department: list):
        url = f'https://open.feishu.cn/open-apis/contact/v3/departments'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send('POST', url, json=data)
        return r.json()

    def get_department_list(self, userid: str):
        url = f'https://open.feishu.cn/open-apis/contact/v3/departments'
        r = self.send('GET', url)

        return r.json()

    def get_department(self, userid: str):
        url = f'https://open.feishu.cn/open-apis/contact/v3/departments/:department_id'
        params = {
            "userid": userid
        }
        r = self.send('GET', url, params=params)

        return r.json()

    def update_department(self, userid: str, name: str):
        url = f'https://open.feishu.cn/open-apis/contact/v3/departments/:department_id'
        data = {
            "userid": userid,
            "name": name
        }
        r = self.send('POST', url, json=data)
        return r.json()

    def delete_department(self, userid: str):
        url = f'https://open.feishu.cn/open-apis/contact/v3/departments/:department_id'
        params = {
            "userid": userid
        }
        r = self.send('GET', url, params=params)

        return r.json()
