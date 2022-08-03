import jsonpath
import requests
from hamcrest import *
from jsonpath import jsonpath


class TestHamcrest:
    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        # print(r.json())
        # print(r.json()['category_list']['categories'][0])
        # assert r.json()['category_list']['categories'][0]['name'] == '提问区'

        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('提问区'))
        # assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('提问区1'))

        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '提问区'
        assert_that('提问区', is_in(jsonpath(r.json(), '$..name')))
