import pdb
import pytest


# 定义一个有参数的fixture，参数名为username。但这种写法是有问题的。
@pytest.fixture()
def login(username):    # this would cause error - E       fixture 'username' not found
    print(f'\n ======== login using {username}===========')
    yield username
    print('\n ======== logout ======== ')



def test_cart(login):
    login("henry")
    print('\n ======== cart ======== ')


# # 普通方法定义如下：
# def login_with(username, password):
#     print(f'logged in with {username} and {password}')

# def test_cart_with():
#     login_with("henry", "123456")
#     print('\n ======== test cart with login_with ======== ')