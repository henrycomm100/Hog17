from datetime import datetime

import pytest


@pytest.fixture(scope="session")
def login():
    print('conftest - login successfully')
    token = datetime.now()
    yield token  # 执行测试用例前，会先执行yield前面的代码。然后执行用例完了之后，再执行yield后面的代码
    print('conftest - logout successfully')
