import requests


class TestRequest:
    def test_request(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.json())
        print(r.text)
        print(r.status_code)
        print(r.request)
        assert r.status_code == 200
        assert r.json()['headers']['Host'] == 'httpbin.testing-studio.com'

    def test_query(self):
        payload = {
            'name': 'henry',
            'game': 'football'
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            'name': 'henry',
            'password': '123'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            'name': 'henry',
            'password': '123'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200

    def test_file_upload(self):
        files = {'file': open('chatbots3.json', 'rb')}
        r = requests.post('https://filebin.net/x80bumimyduabvuw/chatbots3.json', files=files)
        print(r.json())
        print(r.text)
        print(r.content)
        assert r.status_code == 201

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
        session = requests.session()
        r = session.get('https://www.google.com')
        print('status code - ', r.status_code)
        print(r.cookies)
        print(r.cookies.get_dict())
        print(r.cookies.keys())
        print(r.text)
        assert r.status_code == 200

    def test_set_cookies(self):
        cookies = dict(
            token='33eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNyc2Etc2hhMjU2IiwidHlwIjoiSldUIn0.eyJqdGkiOiJjNDEzODQwYy02NmI3LTQwNDMtYTI0OC1mYjY4M2VjM2ZlZWUiLCJhZ2VudElkIjoiMGIxMDVmODAtYWVhMC00ZTQxLThmMDQtYjEyYThhNDI0ZTQ0Iiwic2l0ZUlkIjoiMTAxMDAwMDciLCJ0aHVtYnByaW50IjoiOEE2OEE5OEFDODQxQjVBNzk4RDlGQTUxNjVBRTQ3OTc0RURGQjJGNiIsInN1Y2Nlc3MiOiJUcnVlIiwibmJmIjoxNjM0NjI0NTE2LCJleHAiOjE2MzQ2MzE3MTYsImlzcyI6ImRhc2gxMS5jb21tMTAwLmlvIn0.60u9z1o7_NAva8TcrzLtfG3pUBSrrqpAvn1L949rwraCK_Ue5jkEQIfkr_JMcRamNJlmXorjgMUdQ4DBEBZlBChUrc2FTCY6z1fGcreSBbz28gbs-DnCFUhYOlv1us6AWpUyQREhCFb1tStFcELOTxaEoFO73VxWg3_Dcf-DO6TK4qyukiuIlwyx335L63WXetkTb6r4gzgHyCBl63gG6P8FDvpUsUfxq_jahZMIZKNJIANJKs6wfbERwjblsssDMfDi0KY9RnI7fDYYMOPuV2CuIV54QctdokozWGC0xEY632mQbzxWws6goU_p9ICuI3Szie6lpZvAP77hQiY0xg')
        session = requests.session()
        r = requests.get('https://dash11.comm100.io/ui/10100007/livechat/maximumon/', cookies=cookies)
        print('status code - ', r.status_code)
        print(r.cookies)
        print(r.cookies.keys())
        print(r.text)
        assert r.status_code == 200
