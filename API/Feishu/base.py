import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json; charset=utf-8"
        }

    def get_token(self):
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
        json = {
            "app_id": "cli_a0602868ba78500b",
            "app_secret": "r6vhO1ZyAW5sUgG9nbshhh8BSPJuD1pk"
        }
        r = self.s.post(url, json=json)
        print(r.json()['tenant_access_token'])
        return r.json()['tenant_access_token']

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)
