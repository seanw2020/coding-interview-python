import pytest

from learning.foo import Solution


@pytest.fixture
def setup():
    return Solution.get()


def test_get(setup):
    assert setup == 42
