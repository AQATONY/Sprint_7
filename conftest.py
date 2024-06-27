import allure
import pytest
import requests
import urls



@pytest.fixture(scope='function')
def default_courier():
    payload = {"login": "testinnng17", "password": "1456789", "firstName": "Anton"}
    response = requests.post(urls.URL_CREATE_COURIER, data=payload)
    return response


@pytest.fixture(scope='function')
def empty_payload_create():
    payload = {}
    response = requests.post(urls.URL_CREATE_COURIER, data=payload)
    return response


@pytest.fixture(scope='function')
def login_courier():
    payload = {"login": "testinnng17", "password": "1456789"}
    response = requests.post(urls.URL_LOGIN_COURIER, data=payload)
    return response


@pytest.fixture(scope='function')
def login_empty_payload():
    payload = {}
    response = requests.post(urls.URL_LOGIN_COURIER, data=payload)
    return response


@pytest.fixture(scope='function')
def login_non_exist():
    payload = {"login": "fdadsx", "password": "1434389"}
    response = requests.post(urls.URL_LOGIN_COURIER, data=payload)
    return response


@allure.step("Отправка запроса на создание заказа")
@pytest.fixture(scope='function')
def create_order(body):
    return requests.post(urls.CREATE_ORDER_ENDPOINT, json=body)
