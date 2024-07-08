import allure
import requests
import data
import urls


class ChangeTestDataHelper:

    @staticmethod
    @allure.step("Создание заказа")
    def modify_create_order_body(key, value):
        body = data.TestDataCreateOrder.CREATE_ORDER_BODY.copy()
        body[key] = value

        return body

    @staticmethod
    @allure.step("Создание заказа без цвета")
    def create_no_color(key, value):
        body = data.TestDataCreateOrder.CREATE_ORDER_NOCOLOR.copy()
        body[key] = value

        return body

    @allure.step("Создание курьера")
    def default_courier(self):
        payload = data.TestDataCreateOrder.CREATE_COURIER_DETAILS
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        return response

    @allure.step("Создание курьера с пустым payload")
    def empty_payload_create(self):
        payload = {}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        return response

    @allure.step("Создание курьера с пустым login")
    def empty_login_create(self):
        payload = data.TestDataCreateOrder.CREATE_ORDER_EMPTY_LOGIN
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        return response

    @allure.step("Логин курьера")
    def login_courier(self):
        payload = data.TestDataCreateOrder.LOGIN
        response = requests.post(urls.URL_LOGIN_COURIER, data=payload)
        return response

    @allure.step("Логин курьера с пустым payload")
    def login_empty_payload(self):
        payload = {}
        response = requests.post(urls.URL_LOGIN_COURIER, data=payload)
        return response

    @allure.step("Логин курьера с пустым password")
    def login_non_exist_password(self):
        payload = data.TestDataCreateOrder.LOGIN_EMPY_PASSWORD
        response = requests.post(urls.URL_LOGIN_COURIER, data=payload)
        return response

    @allure.step("Логин курьера с несуществующим логином и паролем")
    def login_non_exist(self):
        payload = data.TestDataCreateOrder.LOGIN_NON_EXIST_LOGIN_PASS
        response = requests.post(urls.URL_LOGIN_COURIER, data=payload)
        return response
