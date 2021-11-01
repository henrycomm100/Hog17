import pystache
import requests


class TestPostUser:
    def test_post_user(self):
        with open("userTemplate.json", encoding="utf8") as f:
            data = pystache.render(f.read(),
                                   {
                                       "user": "henry",
                                       "pwd": "123456"
                                   }
                                   )
        r = requests.post("https://httpbin.testing-studio.com/post", data=data)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
