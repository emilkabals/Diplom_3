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
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import os

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "firefox":
        # Укажите явный путь к geckodriver
        gecko_path = os.path.join(os.path.dirname(__file__), "geckodriver.exe")
        service = Service(executable_path=gecko_path)
        
        options = webdriver.FirefoxOptions()
        # Добавьте опции для стабильности
        options.add_argument("--headless")  # для безголового режима (опционально)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        browser = webdriver.Firefox(service=service, options=options)
    
    elif browser_name == "chrome":
        # Аналогично для Chrome если нужно
        from selenium.webdriver.chrome.service import Service as ChromeService
        chrome_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
        service = ChromeService(executable_path=chrome_path)
        
        options = webdriver.ChromeOptions()
        browser = webdriver.Chrome(service=service, options=options)
    
    browser.maximize_window()
    yield browser
    browser.quit()