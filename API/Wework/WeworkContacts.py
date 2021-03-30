import requests


class WeworkContacts:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            "corpid": "ww62b65a79dc7207eb",
            "corpsecret": "gbaKXEt4FDWWXGiuYgeskVsgSE75Cciiv8Psom78dRk"
        }
        r = requests.get(url, params=params)
        return r.json()['access_token']

    def teardown(self):
        pass

    def add_contact(self, userid: str, name: str, mobile: str, department: list):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        params = {"access_token": self.token}
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(url, params=params, json=data)
        return r.json()

    def get_contact(self, userid: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            "access_token": self.token,
            "userid": userid
        }
        r = requests.get(url, params=params)

        return r.json()

    def update_contact(self, userid: str, name: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        params = {
            "access_token": self.token
        }
        data = {
            "userid": userid,
            "name": name
        }
        r = requests.post(url, params=params, json=data)
        return r.json()

    def delete_contact(self, userid: str):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {
            "access_token": self.token,
            "userid": userid
        }
        r = requests.get(url, params=params)

        return r.json()
