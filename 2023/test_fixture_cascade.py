import pdb
import pytest



@pytest.fixture
def fix0():
    # pdb.set_trace()
    print('\n ======== fix0===========')
    yield
    print('\n ======== fix0 teardown ======== ')




@pytest.fixture
def fix1(fix0):
    def _fix1(name):        
        # pdb.set_trace()
        print('\n ======== fix1===========')
        return name
    yield _fix1
    print('\n ======== fix1 teardown ======== ')

@pytest.fixture
def fix2(fix1):
    # pdb.set_trace()
    print('\n ======== fix2===========')
    yield
    print('\n ======== fix2 teardown ======== ')
    fix1('henry')


def test_fix(fix2):
    print('\n ======== test_fix===========')

test_fix(fix2)