import pytest


@pytest.fixture
def login():
    print('login')


def test_cart(login):
    print('cart')


def test_order():
    print('order')


def test_search():
    print('search')
