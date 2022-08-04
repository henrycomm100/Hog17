# use comm100 shifts as example, using mustache,
import json

import chevron
import requests
from requests.auth import HTTPBasicAuth


class TestShifts:
    auth = requests.auth.HTTPBasicAuth('henry@x2.com', '4012075db78c4a33935acb9b78da9afc')
    shift_url = 'https://api11.comm100.io/v4/livechat/shifts?siteId=10100007'
    headers = {
        'Content-Type': 'application/json'
    }

    def test_get_shifts(self):
        r = requests.get(self.shift_url, auth=self.auth)
        print(r.text)

    def test_create_shift_using_json(self):
        data = {
            "timeZone": "China Standard Time",
            "shiftName": "shift 23"
        }
        with open('shift.mustache', 'r') as f:
            data2 = json.loads(chevron.render(f.read(), data))  # 将mustache模板引擎转换后的字符串转成json, 然后再传入json字段
            print(data2)
            r = requests.post(self.shift_url, auth=self.auth, json=data2)
            print(r.json())
            assert r.status_code == 201

    def test_create_shift(self):
        data = {
            "timeZone": "China Standard Time",
            "shiftName": "shift 23"
        }
        with open('shift.mustache', 'r') as f:
            data2 = chevron.render(f.read(), data)
            print(data2)
            r = requests.post(self.shift_url, auth=self.auth, data=data2,
                              headers=self.headers)  # 必须要添加这个headers, 不然会有报错

            print(r.json())
            assert r.status_code == 201

    def test_create_shift_sanity(self):
        data = {
            "timeZone": "China Standard Time",
            "name": "shift 23"
        }

        r = requests.post(self.shift_url, auth=self.auth, json=data)
        print(r.json())
        assert r.status_code == 201

    def test_create_shift_sanity_using_data(self):
        data = {
            "timeZone": "China Standard Time",
            "name": "shift 23"
        }

        r = requests.post(self.shift_url, auth=self.auth, data=json.dumps(data), headers=self.headers)
        print(r.json())
        assert r.status_code == 201
