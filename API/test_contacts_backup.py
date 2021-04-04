import requests


class TestContacts:
    def setup(self):
        self.token = self.get_token()

    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww62b65a79dc7207eb&corpsecret=gbaKXEt4FDWWXGiuYgeskVsgSE75Cciiv8Psom78dRk'
        r = requests.get(url)
        return r.json()['access_token']

    def teardown(self):
        pass

    def test_add_contact(self):
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data = {
            "userid": "ericmurphy87",
            "name": "eric",
            "mobile": "+86 13800000000",
            "department": [1]
        }
        r = requests.post(url, json=data, proxies=proxies, verify=False)
        print(r.json())
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'created'

    def test_get_contact(self):
        userid = 'ericmurphy87'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}'
        r = requests.get(url)

        print(r.json())
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'ok'
        assert r.json()['userid'] == 'ericmurphy87'

    def test_update_contact(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": "ericmurphy87",
            "name": "ericmurphy87_updated",
            "mobile": "+86 13800000011"
        }
        r = requests.post(url, json=data)
        print(r.json())
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'updated'

    def test_delete_contact(self):
        userid = 'ericmurphy87'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}'
        r = requests.get(url)

        print(r.json())
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == 'deleted'
