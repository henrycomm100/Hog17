import pytest


@pytest.fixture
def purge_messages():
    def _purge_messages(queue_name):
        print(f'\n purge messages for {queue_name} via factory done.')

    return _purge_messages


def test_persistence(purge_messages):
    purge_messages('PersistenceQueue')
    print('\n Start consuming. Persistence consuming done.')

# test_persistence without passing the queue_name
def test_persistence_without_queue_name(purge_messages):
    purge_messages() # this will cause error E       TypeError: purge_messages.<locals>._purge_messages() missing 1 required positional argument: 'queue_name'
    print('\n Start consuming. Persistence consuming done.')