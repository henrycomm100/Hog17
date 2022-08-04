import jsonpath
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
        assert r.json()['form']['name'] == 'henry'

    def test_post_json(self):
        payload = {
            'name': 'henry',
            'password': '123'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['name'] == 'henry'
        assert r.json()['json']['password'] == '123'

    def test_file_upload(self):
        files = {'file': open('chatbots3.json', 'rb')}
        r = requests.post('https://filebin.net/x80bumimyduabvuw/chatbots3.json', files=files)
        print(r.json())
        print(r.text)
        print(r.content)
        assert r.status_code == 201

    def test_hogwarts_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        # print(r.json())
        # print(r.json()['category_list']['categories'][0])
        assert r.json()['category_list']['categories'][0]['name'] == '提问区'

        print(jsonpath.jsonpath(r.json(), '$..name'))
        assert jsonpath.jsonpath(r.json(), '$..name')[0] == '提问区'
