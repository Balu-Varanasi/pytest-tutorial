"""Basic Tests."""

import pytest

import example


def test_1_add():
    """Test 1."""
    assert example.add(3, 4) == 7


def test_2_subtract():
    """Test 1."""
    assert example.subtract(32, 20) == 12


def test_3_multiply():
    """Test 1."""
    assert example.multiply(3, 2) == 6


def test_4_divide():
    """Test 1."""
    assert example.divide(4, 2) == 2


def test_5_division_with_zero():
    """Test 1."""
    with pytest.raises(ZeroDivisionError):
        example.divide(1, 0)


def test_example_1():
    """Test Example 1."""
    with pytest.raises(ZeroDivisionError):
        1 / 0
