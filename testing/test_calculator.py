import allure
import yaml

from pythoncode.Calculator import Calculator

import pytest


def get_data(func):
    data = yaml.safe_load(open("../data/dataForCalculator.yaml"))
    # func: str = func
    numbers = data[func]['number']
    ids = data[func]['id']
    print(data)
    print(data['add']['number'])
    print(data['add']['id'])
    print(data['divide'])
    return numbers, ids


@allure.epic("计算器功能")
class TestCaculator:

    def setup(self):
        self.cal = Calculator()
        print("start the calculation ---")

    @allure.feature("相加功能")
    @pytest.mark.search
    @pytest.mark.parametrize("a, b, result", get_data('add')[0], ids=get_data('add')[1])
    def test_add(self, a, b, result):
        res = self.cal.add(a, b)
        res = round(res, 2)
        assert result == res

    @allure.feature("减法")
    def test_substract(self):
        assert 1 == self.cal.subtract(2, 1)

    @allure.feature("乘法")
    def test_multiply(self):
        assert 2 == self.cal.multiply(1, 2)

    @allure.feature("除法")
    @pytest.mark.parametrize("a, b, result", get_data('divide')[0], ids=get_data('divide')[1])
    def test_divide(self, a, b, result):
        try:
            res = self.cal.divide(a, b)
            res = round(res, 2)
            assert result == res
            print(result)
        except Exception as e:
            print(e)
            print("You can't divide by zero")

        # if b == 0:
        #     try:
        #         self.cal.divide(a, b)
        #     except ZeroDivisionError as e:
        #         print("You can't divide by zero")
        # else:
        #     res = self.cal.divide(a, b)
        #     res = round(res, 2)
        #     assert result == res
        #     print(result)

    def teardown(self):
        print("calculation completed ----")
