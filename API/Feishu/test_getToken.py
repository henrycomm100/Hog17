import pytest
import requests


class TestGetToken:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_get_token(self):
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
        json = {
            "app_id": "cli_a0602868ba78500b",
            "app_secret": "r6vhO1ZyAW5sUgG9nbshhh8BSPJuD1pk"
        }
        r = requests.post(url, json=json)
        print('3')
        print(r.json()['tenant_access_token'])
        return r.json()['tenant_access_token']

    def test_get_department_list(self):
        url = f'https://open.feishu.cn/open-apis/contact/v3/departments'
        token = self.test_get_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8"
        }
        r = requests.get(url, headers=headers)

        print(r.json())
        return r.json()

    def test_add_calendar(self):
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars'
        json = {
            "summary": "测试日历",
            "description": "使用开放接口创建日历",
            "permissions": "private",
            "color": -1,
            "summary_alias": "日历备注名"
        }

        token = self.test_get_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8"
        }

        r = requests.post(url, headers=headers, json=json)

        print(r.json())
        return r.json()
