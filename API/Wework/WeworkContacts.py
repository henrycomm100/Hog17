import requests


class WeworkContacts:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            "corpid": "ww62b65a79dc7207eb",
            "corpsecret": "gbaKXEt4FDWWXGiuYgeskVsgSE75Cciiv8Psom78dRk"
        }
        r = self.s.get(url, params=params)
        return r.json()['access_token']

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
        r = self.s.post(url, json=data)
        return r.json()

    def get_contact(self, userid: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            "userid": userid
        }
        r = self.s.get(url, params=params)

        return r.json()

    def update_contact(self, userid: str, name: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name
        }
        r = self.s.post(url, json=data)
        return r.json()

    def delete_contact(self, userid: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {
            "userid": userid
        }
        r = self.s.get(url, params=params)

        return r.json()
