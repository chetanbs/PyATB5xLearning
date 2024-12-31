import pytest
import allure
import requests

from Nov.ex_09112024_Literals_Variables.Lab025_Strings import first_name, last_name


@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"

    full_url = base_url + base_path_post
    headers = {
        "Content-Type" : "application/json"
    }
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    responses_data = requests.post(url=full_url, headers=headers, json=payload)

    # Status Code verification
    assert responses_data.status_code == 200

    # Booking ID > 0, firstname == Jim
    responses_data_json = responses_data.json()
    bookingid = responses_data_json["bookingid"]
    print(bookingid)
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = responses_data_json["booking"]["firstname"]
    assert firstname == "Jim"
    assert type(firstname) == str

    lastname = responses_data_json["booking"]["lastname"]
    totalprice = responses_data_json["booking"]["totalprice"]
    depositpaid = responses_data_json["booking"]["depositpaid"]

    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

    # https:// jsonpathfinder.com
    # x.booking.bookingdates.checkin
    # response_data_json["booking"]["bookingdates"]["checkin"]
    checkin = responses_data_json["booking"]["bookingdates"]["checkin"]
    checkout = responses_data_json["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    time = responses_data.elapsed.total_seconds()
    assert time < 3


@allure.title("TC#2 - Create Booking CRUD Positive")
@allure.description("Verify that invalid payload Booking is not created!")
@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 500
    print(response.text)

    assert response.text == "Internal Server Error"