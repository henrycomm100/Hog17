import pytest


@pytest.fixture()
def login():
    print('conftest in xueqiu - login successfully')
    token = datetime.datetime.now()
    yield token  # 执行测试用例前，会先执行yield前面的代码。然后执行用例完了之后，再执行yield后面的代码
    print('conftest in xueqiu - logout successfully')
