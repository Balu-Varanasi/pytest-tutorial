"""Demonstrate setup and teardown funtions."""

import examples


# module level setups

def setup_module(module):
    """Module level setup function."""
    print ("setup_module module:%s\n" % module.__name__)


def teardown_module(module):
    """Module level teardown function."""
    print ("teardown_module module:%s\n" % module.__name__)


# function level setups

def setup_function(function):
    """Function level setup function."""
    print ("\tsetup_function function:%s\n" % function.__name__)


def teardown_function(function):
    """Function level teardown function."""
    print ("\tteardown_function function:%s\n" % function.__name__)


# tests

#  functions
def test_numbers_3_4():
    """Test multiplication of two numbers."""
    print '\t\t\ttest_numbers_3_4 <==================== actual test code\n'
    assert examples.multiply(3, 4) == 12


def test_strings_a_3():
    """Test multiplication of a string by a number."""
    print '\t\t\ttest_strings_a_3 <==================== actual test code\n'
    assert examples.multiply('a', 3) == 'aaa'


#  classes
class TestEmptyTestsClass:
    """Example for a TestEmptyTestsClass."""

    def setup(self):
        """Class level setup."""
        print ("\t\tsetup class:TestEmptyTestsClass\n")

    def teardown(self):
        """Class level teardown."""
        print ("\t\tteardown class:TestEmptyTestsClass\n")


class TestUM:
    """This is a TestClass."""

    # class level methods
    @classmethod
    def setup_class(cls):
        """Class level setup."""
        print ("\t\tsetup class:TestUM\n")

    @classmethod
    def teardown_class(cls):
        """Class level teardown."""
        print ("\t\tteardown class:TestUM\n")

    # method level methods
    def setup_method(self, method):
        """Method level setup."""
        print ('\t\t\tsetup_method')

    def teardown_method(self, method):
        """Metthod level setup."""
        print ('\t\t\tteardown_method')

    # actual test methods
    def test_numbers_3_4(self):
        """Test multiplication of two numbers."""
        print '\t\t\t\ttest_numbers_3_4 <================== actual test code\n'
        assert examples.multiply(3, 4) == 12

    def test_strings_a_3(self):
        """Test multiplication of a string by a number."""
        print '\t\t\t\ttest_strings_a_3 <================== actual test code\n'
        assert examples.multiply('a', 3) == 'aaa'
