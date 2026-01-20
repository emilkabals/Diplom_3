import pytest
import requests

from selenium import webdriver

from pages.auth_page import AuthPage
from urls import URL
from generators import generate_user_data


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL.MAIN_PAGE)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(URL.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_and_delete_user():
    user_data = generate_user_data()

    register_response = requests.post(URL.REGISTER_USER_URL, json=user_data)
    access_token = register_response.json()["accessToken"]

    user_data["token"] = f"Bearer {access_token}"

    yield user_data

    headers = {"Authorization": user_data["token"]}
    requests.delete(URL.USER_URL, headers=headers)

@pytest.fixture(scope="function")
def login_user(driver, create_and_delete_user):
    auth_page = AuthPage(driver)
    auth_page.open_auth_page()
    auth_page.auth(create_and_delete_user["email"], create_and_delete_user["password"])
    return driver
