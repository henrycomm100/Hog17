import pytest


@pytest.fixture(autouse=True)
def login():
    print('login')


@pytest.fixture()
def get_username():
    name = 'henry'
    print(name)
    return name




def test_cart(login):
    print('cart')


def test_order(login, get_username):
    print('order')


def test_search():
    print('search')


@pytest.mark.usefixtures('login')
def test_change_password():
    print('change password')
