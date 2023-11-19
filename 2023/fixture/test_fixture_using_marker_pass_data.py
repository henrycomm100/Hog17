import pytest

@pytest.fixture()
def purge_messages():
    print('\n purge messages done.')


# def test_persistence(purge_messages):
#     print('\n persistence consuming done.')


@pytest.fixture()
def purge_messages_marker(request):
    marker = request.node.get_closest_marker('queue_name')
    if marker is None:
        # Handle missing marker in some way...
        data = None
    else:
        data = marker.args[0]
    print('\n purge messages via marker done.', f'and the marker is: {data}')


@pytest.mark.queue_name('PersistenceQueue')
def test_persistence_marker(purge_messages_marker):
    print('\n persistence consuming done.')