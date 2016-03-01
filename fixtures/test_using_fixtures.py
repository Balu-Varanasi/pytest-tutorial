"""
Three ways to use a fixture.

    1. name it from the test.
    2. using 'usefixtures' decorator
    3. autouse
"""

from __future__ import print_function

import pytest


# 'autouse' fixture
@pytest.fixture(autouse=True, scope='class')
def autouse_fixture():
    """'autouse' fixture example."""
    print("\n\nautouse_fixture")


# non autouse fixture
@pytest.fixture()
def non_autouse():
    """Sample fixture."""
    print('\n\tnon_autouse')


# 1. name it from the test.

def test_1(non_autouse):
    """Example 1."""
    print('\t\ttest_1()\n')


def test_2(non_autouse):
    """Example 2."""
    print('\t\ttest_2()\n')


# 2. using 'usefixtures' decorator

@pytest.mark.usefixtures("non_autouse")
def test_3():
    """Example 3."""
    print('\t\ttest_3()\n')


@pytest.mark.usefixtures("non_autouse")
def test_4():
    """Example 4."""
    print('\t\ttest_4()\n')


# 3. autouse

def test_5():
    """Example 5."""
    print('\ttest_5()\n')


class Test:
    """Example TestClass."""

    @pytest.mark.usefixtures("non_autouse")
    def test_1(self):
        """Class Test 1."""
        print('\t\tclass_test_1()')

    @pytest.mark.usefixtures("non_autouse")
    def test_2(self):
        """Class Test 2."""
        print('\t\tclass_test_2()')
