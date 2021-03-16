# content of test_sample.py
import pytest


def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (1,2),
    (10, 20),
    ('a','a1'),
    (3,4),
    (5,6)
])
def test_answer(a,b):
    assert func(a) == b


def test_answer2():
    assert func(0) == 1

@pytest.fixture()
def login():
    print("I'm going to login")
    username = 'Jerry'
    return  username;

class TestDemo():
    def test_a(self,login):
        print(f"a login is {login}")

    def test_b(self):
        print("b")

    def test_c(self,login):
        print(f"c login is {login}")


if __name__ == '__main__':
    # pytest.main(['test_pytestdemo.py'])
    pytest.main(['test_pytestdemo.py::TestDemo', '-v'])
