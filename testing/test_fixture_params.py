#     :param params:
#         An optional list of parameters which will cause multiple invocations
#         of the fixture function and all of the tests using it. The current
#         parameter is available in ``request.param``.

import pytest


@pytest.fixture(params=['henry', 'eric'], ids=['testcase1', 'testcase2'])
def login(request):
    print('login successfully')
    return request.param


def test_order(login):
    print(login)
    print('making order')
