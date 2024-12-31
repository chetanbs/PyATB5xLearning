import pytest


def method1():
    print("Hello World")

@pytest.mark.smoke
def test_method2():
    print("This is Pytest case")
    assert 1 - 1 == 2

# Assertion is a statement and checkes the condition

@pytest.mark.regression
def test_method3():
    print("test2")
    assert 1 + 1 == 2

# to run entire program clear then run with program path