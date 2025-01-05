# Create a BOOKING, Delete It

import allure
import pytest
import requests

from Jan.ex_02012025_fixtures.test_task2_Create_Delete_Get import get_token


def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"

    full_url = base_url + base_path_post
    headers = {
        "Content-Type": "application/json"
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
    responses_data_json = responses_data.json()
    bookingid = responses_data_json["bookingid"]
    print(bookingid)


def test_delete():
    URL = "https://result-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    DELETE_URL = URL + str(2134)
    cookie_value = "token=" + get_token()
    headers = {
        "Content-Type" : "application/json",
        "Cookie" : cookie_value
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 404