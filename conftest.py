import allure
import pytest
import requests
import urls










@allure.step("Отправка запроса на создание заказа")
@pytest.fixture(scope='function')
def create_order(body):
    return requests.post(urls.CREATE_ORDER_ENDPOINT, json=body)
