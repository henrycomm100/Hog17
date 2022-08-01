import pytest


@pytest.mark.parametrize('name', ['亨利', '温格'])
def test_encode(name):
    print(name)
