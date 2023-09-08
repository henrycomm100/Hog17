import pytest




@pytest.fixture()
def get_username():
    name = 'henry'
    print("this is printed: " + name)
    return name


@pytest.fixture()
def get_username_from_type(request):
    if request.param == 'male':
        return 'henry'
    else:
        return 'Mary'

@pytest.mark.parametrize('get_username_from_type', ['male'], indirect=True)
def test_user(get_username_from_type):
    print(get_username_from_type)

def test_user2(get_username_from_type):
    print(get_username_from_type)