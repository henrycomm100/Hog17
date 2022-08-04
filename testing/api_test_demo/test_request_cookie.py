import requests


class TestRequestCookie:
    def test_headers(self):
        headers = {
            'user-agent': 'my-app/1.0.1'
        }
        r = requests.get('https://httpbin.testing-studio.com/get', headers=headers)
        print('status code - ', r.status_code)
        print(r.text)
        print(r.content)
        assert r.status_code == 200

    def test_get_cookies(self):
        session = requests.Session()
        r = session.get('https://www.google.com')
        # print('status code - ', r.status_code)
        print(r.cookies)
        print(r.cookies.get_dict())
        print(r.cookies.items())
        print(r.cookies.keys())
        # print(r.text)
        assert r.status_code == 200

    def test_set_cookie_sanity(self):
        url = 'https://httpbin.testing-studio.com/cookies/set/abc/111'

        session = requests.Session()
        session.cookies.set('vip_level', 'diamond')  # 通过session去设置cookie就可以了

        r = session.get(url)

        print(r.text)
        print('headers in the request: ', r.request.headers)
        print('headers in the response: ', r.headers)  # 通过response的headers里面去取cookie,是取不到的。
        print('cookies in the response: ', r.cookies.items())  # 通过response里面去取cookie,是取不到的。
        print(session.cookies.items())  # 通过session去取就能看到设置的cookie, 有2个，一个是我们通过session设置进去的，一个是我们调用URL设置进去的
        assert r.status_code == 200

    def test_set_cookies(self):
        session = requests.Session()
        session.cookies.set('token_10100007',
                            'eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNyc2Etc2hhMjU2IiwidHlwIjoiSldUIn0.eyJqdGkiOiIxNzgxZDk5Yi1hMzE0LTQyNmYtYjAwNS0zMzgzYmM1NDIwOGQiLCJhZ2VudElkIjoiMGIxMDVmODAtYWVhMC00ZTQxLThmMDQtYjEyYThhNDI0ZTQ0Iiwic2l0ZUlkIjoiMTAxMDAwMDciLCJ0aHVtYnByaW50IjoiOEE2OEE5OEFDODQxQjVBNzk4RDlGQTUxNjVBRTQ3OTc0RURGQjJGNiIsInN1Y2Nlc3MiOiJUcnVlIiwibmJmIjoxNjU5NjA0NDk2LCJleHAiOjE2NTk2MTE2OTYsImlzcyI6ImRhc2gxMS5jb21tMTAwLmlvIn0.N0bMgJRzJAleU-xfYL50pD60WN5hE6wKnaqWV41-PNAfKFHiHeChr8jhojHdGc7iC5rLZyfGCaFPu6MB7kiEv_qYoTuokGzdApFnocCIi5qkrHCuzFij3BoaHMgc9GoxlPtmWizYJm-Hl6ZVRHCZ5eEiAAgsc-AV_3xo_vv0oYaghkOmeS1U47JPZMiJYeAlymQ7GbqBqJyFPTAMzvNasvEtGUjT4IMpbiB8LtSb2Vmvhx2h8onYtPBJl1Hlmmo_CMvcTKXYBI8l_0TDVujc04AT2a-KW_nqccLQnZlmhXVUsaGKX26AmgXHPaNDQA1RaMnTDjqjqABXQHmENVfVRg')

        r = session.get(
            'https://dash11.comm100.io/api/global/api/site/DefaultVariable?siteId=10100007')  # 当在cookie设置了token之后，这个接口就可以正常返回数据了
        print(r.text)
        print('headers in the request: ', r.request.headers)
        print('headers in the response: ', r.headers)  # 通过response的headers里面去取cookie,是取不到的。
        print('cookies in the response: ', r.cookies.items())  # 通过response里面去取cookie,是取不到的。
        print(session.cookies.items())  # 通过session去取就能看到设置的cookie, 有2个，一个是我们通过session设置进去的，一个是我们调用URL设置进去的
        assert r.status_code == 200
