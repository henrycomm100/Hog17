import json

from jsonschema import validate
import requests
from requests.auth import HTTPBasicAuth


class TestJsonSchema:
    auth = requests.auth.HTTPBasicAuth('henry@x2.com', '4012075db78c4a33935acb9b78da9afc')
    shift_url = 'https://api11.comm100.io/v4/livechat/shifts?siteId=10100007'
    headers = {
        'Content-Type': 'application/json'
    }

    def test_create_shift_jsonschema(self):
        data = {"timeZone": "China Standard Time", "autoDetectDayLightSavingsTime": "false", "name": "shift"}
        body_data = json.dumps(data)  # 注意，这里要将python对象转换为 JSON字符串

        r = requests.post(self.shift_url, auth=self.auth, data=body_data, headers=self.headers)
        response_data = r.json()
        print(response_data)
        assert r.status_code == 201
        shift_schema = json.load(open('shift_jsonschema.json', 'r'))  # 注意，这里要将一个文件流 转换成 python对象

        validate(instance=response_data, schema=shift_schema)

    def test_jsonschema_sanity(self):
        schema = {
            "type": "object",
            "properties": {
                "price": {"type": "number"},
                "name": {"type": "string"},
            },
        }

        instance = {"name": "Eggs", "price": 34.99}
        validate(instance, schema)

        wrong_instance = {"name": "Eggs", "price": "Invalid"}
        validate(wrong_instance, schema)
