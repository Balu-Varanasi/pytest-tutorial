"""Basic Fixtures Example."""

from __future__ import print_function
import pytest


@pytest.fixture()
def hello_world():
    """Sample fixture."""
    print('\nexample: executes before each test')
    return "=====> \t\tHello World!"


def test_1(hello_world):
    """Test fixture 1."""
    print('\ttest_1()')


def test_2(hello_world):
    """Test fixture 2."""
    print('\ttest_2()')
    print(hello_world)
