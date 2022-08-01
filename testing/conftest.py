from datetime import datetime
from typing import List

import pytest


@pytest.fixture(scope="session")
def login():
    print('conftest - login successfully')
    token = datetime.now()
    yield token  # 执行测试用例前，会先执行yield前面的代码。然后执行用例完了之后，再执行yield后面的代码
    print('conftest - logout successfully')


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)

    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        print(item.name)
        print(item._nodeid)

        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)

    items.reverse()  # 翻转 测试用例顺序
