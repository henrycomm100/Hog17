import datetime

import pytest


@pytest.fixture
def login():
    print('login successfully')
    token = datetime.datetime.now()
    yield token  # 执行测试用例前，会先执行yield前面的代码。然后执行用例完了之后，再执行yield后面的代码
    print('logout successfully')


def test_cart(login):
    print(login)  # 会将login方法中返回 yield token的内容
    print(f'\nadd to the cart')
