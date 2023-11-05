import pytest


@pytest.fixture
def purge_messages():
    def _purge_messages(queue_name):
        print(f'\n purge messages for {queue_name} via factory done.')
        return queue_name

    yield _purge_messages
    print('\n teardown part')


# sanity test
def test_persistence(purge_messages):
    purge_messages('PersistenceQueue')
    print('\n Start consuming. Persistence consuming done.')

# # test_persistence without passing the queue_name
# def test_persistence_without_queue_name(purge_messages):
#     purge_messages() # this will cause error E       TypeError: purge_messages.<locals>._purge_messages() missing 1 required positional argument: 'queue_name'
#     print('\n Start consuming. Persistence consuming done.')



@pytest.fixture
def get_id():
    def _get_id(name):
        if name == "henry":
            id = 14
        else:
            id = 0
        return id

    yield _get_id
    print('\n teardown part')
    delete_id(id) # this is not working, because id is not defined in this scope



def delete_id(id):
    if id == 14:
        print("delete 14 successfully")

def test_get_id(get_id):
    id = get_id("henry")
    print(id)
    delete_id(id) # this is working, because id is defined in this scope