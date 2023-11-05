import pytest


@pytest.fixture
def same_level_fixture():
    name = "henry"
    yield name
    get_id(name)

def test_get_level(same_level_fixture):
    print(same_level_fixture)

def get_id(name):
    if name == "henry":
        print(14)
    else:
        print(0)




# def test_get_user_name(get_name):
#     print(get_name)



# def test_get_user_id(get_guid):
#     print(get_guid)

