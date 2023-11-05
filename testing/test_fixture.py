import pdb
import pytest


@pytest.fixture(autouse=True)
def login():
    print('\n ======== login===========')
    a = 3
    yield a
    print('\n ======== logout ======== ')


@pytest.fixture()
def get_username():
    name = 'henry'
    print(name)
    return name


def get_henry(get_username):
    name = 'henry'
    print(name)
    return name



def test_cart(login):
    print('\n ======== cart ======== ')
    pdb.set_trace()
    print('after pdb breakpoint')


# def test_order(login, get_username):
#     print('order')


# def test_search():
#     print('search')


# @pytest.mark.usefixtures('login')
# def test_change_password():
#     print('change password')
