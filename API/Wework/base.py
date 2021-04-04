import requests


class Base:
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

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)
