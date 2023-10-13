import pytest

@pytest.fixture()
def print_user1():
    print("1")

@pytest.fixture()
def print_user2():
    print("2")


@pytest.fixture()
def print_user3():
    print("3")


def test_fixure_order(print_user1, print_user2, print_user3):
    print("test")


def test_fixure_order2(print_user1, print_user3, print_user2):
    print("test2")


def test_fixure_order3(print_user3, print_user2, print_user1):
    print("test3")
