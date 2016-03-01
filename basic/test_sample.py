"""'py.test'."""

import pytest


def test_1_add():
    """Test 1."""
    print "hello world"
    assert (3 + 4) == 7


def test_2_subtract():
    """Test 2."""
    assert (32 - 20) == 12


def test_3_multiply():
    """Test 3."""
    assert 3 * 2 == 6


def test_4_divide():
    """Test 4."""
    assert 4 / 2 == 2


def test_5_division_with_zero():
    """Test Zero division error."""
    with pytest.raises(ZeroDivisionError):
        1 / 0
