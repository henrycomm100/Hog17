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


@pytest.fixture()
def get_instance():
    print("start the calculation ---")
    cal = Calculator()
    yield cal
    print("calculation completed ----")


@allure.epic("计算器功能")
class TestCaculator:

    @allure.feature("相加功能")
    @pytest.mark.search
    @pytest.mark.parametrize("a, b, result", get_data('add')[0], ids=get_data('add')[1])
    def test_add(self, get_instance, a, b, result):
        res = get_instance.add(a, b)
        res = round(res, 2)  # 需要进行精度控制，比如 0.1+0.2会算出来0.30000000000000004，直接进行比较会出现不匹配的问题
        assert result == res

    @allure.feature("减法")
    def test_substract(self, get_instance):
        assert 1 == get_instance.subtract(2, 1)

    @allure.feature("乘法")
    def test_multiply(self, get_instance):
        assert 2 == get_instance.multiply(1, 2)

    @allure.feature("除法")
    @pytest.mark.parametrize("a, b, result", get_data('divide')[0], ids=get_data('divide')[1])
    def test_divide(self, get_instance, a, b, result):
        try:
            res = get_instance.divide(a, b)
            res = round(res, 2)
            assert result == res
            print(result)
        except Exception as e:
            print(e)
            print("You can't divide by zero")
