from selenium import webdriver
import pytest
import allure

@allure.title("Open the app.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Chrome()
    # 1. This code is translated into the API request
    # 2. POST request - browser driver(server)
    # 3. Where it will create a session or fresh copy browser (Chrome)
    # 4. Session ID - 16 digit (1340e10d18f334efa93b73105c5d56d2) will be created
    driver.get("https://app.vwo.com")
    print(driver.session_id)
    # 5. GET -> GET API request to navigate to particular page
    # 6. Browser will navigate to the URL

    # Source code(Client) -> API Request(W3C) -> Browser Driver(Server) -> Browser

