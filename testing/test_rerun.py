import random

import pytest


def test_rerun():
    assert 1 == 1


@pytest.mark.flaky(reruns=5)
def test_random():
    assert random.choice([False, False, False])


def test_pytest_assume():
    assert 1 == 1
    pytest.assume(1 == 2)
    pytest.assume(1 == 4)
    pytest.assume(3 == 3)
    assert 3 == 3
