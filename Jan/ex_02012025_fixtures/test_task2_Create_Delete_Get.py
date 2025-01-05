# Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

import allure
import pytest
import requests

from Jan.ex_02012025_fixtures.test_fixture_Demo2 import create_booking_id

# Create Token - POST
base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}


def get_token():
    base_path = "/auth"
    full_url = base_url + base_path
    json_payload_auth = {
        "username" : "admin",
        "password" : "password123"
    }
    response_data = requests.post(url=full_url, headers=headers, json=json_payload_auth)
    print(response_data)

    assert response_data.status_code == 200
    response_data_json  = response_data.json()
    token = response_data_json["token"]
    print(token)

    assert type(token) == str
    assert len(token) > 0

    return token


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
    DELETE_URL = URL + str(2359)
    cookie_value = "token=" + get_token()
    headers = {
        "Content-Type" : "application/json",
        "Cookie" : cookie_value
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 404


def test_get_booking_id():
    #del_booking_id = create_booking()
    #print(del_booking_id)
    url = "https://restful-booker.herokuapp.com/booking/"
    #base_path = str(del_booking_id)
    base_path = str(2359)
    #print(base_path)
    full_url_del = url + base_path

    get_response = requests.get(url = full_url_del)
    print(get_response.text)       # text should be not found
    #assert get_response is not None
    assert get_response.status_code == 404