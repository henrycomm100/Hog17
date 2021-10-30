import pytest
import allure

from API.apitest_cicd.library.httpclient import HttpClient


@allure.feature('Test Weather API')
class TestWeather:
    def setup(self):
        self.host = 'http://www.weather.com.cn'
        self.endpoint_path = '/data/cityinfo'
        self.client = HttpClient()

    def get_weather(self, city_code, expected_city):
        url = f'{self.host}{self.endpoint_path}/{city_code}.html'
        response = self.client.get(url=url)
        actual_city = response.json()['weatherinfo']['city']
        print(f'Expected City = {expected_city}, while Actual City is {actual_city}')
        assert response.status_code == 200
        assert actual_city == expected_city

    @allure.story('Test of Shanghai')
    def test_shanghai(self):
        city_code = '101020100'
        expected_city = '上海'
        self.get_weather(city_code, expected_city)

    @allure.story('Test of Hangzhou')
    def test_hangzhou(self):
        city_code = '101210101'
        expected_city = '杭州'
        self.get_weather(city_code, expected_city)

    @allure.story('Test of Beijing')
    def test_beijing(self):
        city_code = '101010100'
        expected_city = '北京'
        self.get_weather(city_code, expected_city)

    @allure.story('Test of Shenzhen')
    def test_shenzhen(self):
        city_code = '101280601'
        expected_city = '深圳'
        self.get_weather(city_code, expected_city)
