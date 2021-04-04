import requests

from API.Wework.base import Base


class WeworkContacts(Base):
    def teardown(self):
        pass

    def add_contact(self, userid: str, name: str, mobile: str, department: list):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send('POST', url, json=data)
        return r.json()

    def get_contact(self, userid: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            "userid": userid
        }
        r = self.send('GET', url, params=params)

        return r.json()

    def update_contact(self, userid: str, name: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name
        }
        r = self.send('POST', url, json=data)
        return r.json()

    def delete_contact(self, userid: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {
            "userid": userid
        }
        r = self.send('GET', url, params=params)

        return r.json()
