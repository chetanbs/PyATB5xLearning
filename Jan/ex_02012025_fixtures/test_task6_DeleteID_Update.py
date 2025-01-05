#  Trying to Update on a Delete ID -> 404
# Wrong → {} , { “ name” : “Pramod”}

import allure
import pytest
import requests

from Jan.ex_02012025_fixtures.test_task2_Create_Delete_Get import create_booking, get_token

# Create Token - POST
base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}


def create_token():
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
    return token

def test_create_booking():
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


def test_delete():
    URL = "https://result-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + get_token()
    headers = {
        "Content-Type" : "application/json",
        "Cookie" : cookie_value
    }
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 404


def test_update_deleted_request():
    booking_id = create_booking()
    print(booking_id)
    token = create_token()
    url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" +str(booking_id)
    full_url_patch = url + base_path
    cookie = "token="+token
    header = {
        "Content-Type": "application/json",
        "Cookie": cookie

    }
    json_payload = {
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
    response = requests.put(url=full_url_patch, headers=header, json=json_payload)
    print(response.text)
    assert response.status_code == 405
