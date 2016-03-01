"""Request Object."""

import pytest


@pytest.fixture()
def my_fixture(request):
    """My test fixture."""
    print('\n-----------------')
    print('fixturename : %s' % request.fixturename)
    print('scope       : %s' % request.scope)
    print('function    : %s' % request.function.__name__)
    print('cls         : %s' % request.cls)
    print('module      : %s' % request.module.__name__)
    print('fspath      : %s' % request.fspath)
    print('-----------------')

    if request.function.__name__ == 'test_three':
        request.applymarker(pytest.mark.xfail)


def test_one(my_fixture):
    """Test 1."""
    print('test_one():')
