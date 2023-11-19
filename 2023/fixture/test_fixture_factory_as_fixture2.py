import pytest


@pytest.fixture
def purge_messages2():
    a = "333"
    def _purge_messages2(queue_name):
        print(f'\n purge messages for {queue_name} via factory done.')
        return a

    yield _purge_messages2
    print('\n teardown part')


# sanity test
def test_persistence(purge_messages2):
    b =  purge_messages2('PersistenceQueue')
    print(f'\n b is {b}.')



