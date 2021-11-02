# todo
# use comm100 shifts as example, using mustache,
import pystache
import requests
from requests.auth import HTTPBasicAuth


class TestShifts:
    auth = requests.auth.HTTPBasicAuth('henry@x2.com', '4012075db78c4a33935acb9b78da9afc')
    shift_url = 'https://api11.comm100.io/v4/livechat/shifts?siteId=10100007'

    def test_get_shifts(self):
        r = requests.get(self.shift_url, auth=self.auth)
        print(r.text)

    def test_create_shift(self):
        data = {
            "timeZone": "China Standard Time",
            "shiftName": "shift 22"
        }
        data2 = pystache.Renderer().render_name('shift', data)
        print(data2)
        r = requests.post(self.shift_url, auth=self.auth, data=data2)
        print(r.json())
        assert r.status_code == 201
