import pytest
import allure

def method1():
    print("Hello World")

@allure.title("Verify create booking with valid data is working")
@allure.description("This testcase check for the positive create Booking")
@pytest.mark.positive
def test_create_booking_positive():
    print("This is Pytest case")
    assert 1 - 1 == 2

# Assertion is a statement and checkes the condition
@allure.title("Verify create booking with invalid data is working")
@allure.description("This testcase check for the negative create Booking")
@pytest.mark.negative
def test_create_booking_negative_1():
    print("test2")
    assert 1 + 1 == 2

@allure.title("Verify create booking with invalid data is working")
@allure.description("This testcase check for the negative create Booking")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("test2")
    assert 1 + 1 == 2

# to run entire program clear then run with program path