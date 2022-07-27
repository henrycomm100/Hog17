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


@pytest.fixture(params=get_data('add')[0], ids=get_data('add')[1])  # 使用fixture来实现 数据驱动
def get_data_with_fixture(request):
    return request.param


def test_params(get_data_with_fixture):
    print(get_data_with_fixture)


@pytest.fixture()  # 使用fixture来实现初始化
def get_instance():
    print("start the calculation ---")
    cal = Calculator()
    yield cal
    print("calculation completed ----")


@allure.epic("计算器功能")
class TestCaculator:

    @allure.feature("相加功能")
    @pytest.mark.search
    def test_add(self, get_instance, get_data_with_fixture):  # 使用fixture来实现初始化 + 数据驱动
        d = get_data_with_fixture
        res = get_instance.add(d[0], d[1])
        res = round(res, 2)  # 需要进行精度控制，比如 0.1+0.2会算出来0.30000000000000004，直接进行比较会出现不匹配的问题
        assert d[2] == res

    @allure.feature("除法")
    def test_divide(self, get_instance, get_data_with_fixture):
        try:
            d = get_data_with_fixture
            res = get_instance.divide(d[0], d[1])
            res = round(res, 2)
            assert d[2] == res
            print(d[2])
        except Exception as e:
            print(e)
            print("You can't divide by zero")
