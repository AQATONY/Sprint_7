import allure

import helper


class TestCreateCourier:

    @allure.title("Проверка успешности создания курьера")
    @allure.description("Создание курьера, проверка статуса ответа")
    def test_success_create_courier(self):
        response = helper.ChangeTestDataHelper.default_courier()
        assert response.status_code == 201

    @allure.title("Проверка успешности создания курьера с теми же данными")
    @allure.description("Создание курьера, проверка статуса ответа")
    def test_create_duplicate_courier(self):
        response = helper.ChangeTestDataHelper.default_courier()
        assert response.status_code == 409

    @allure.title("Проверка успешности создания курьера с пустым телом запроса")
    @allure.description("Создание курьера, проверка статуса ответа")
    def test_create_courier_empty_payload(self):
        response = helper.ChangeTestDataHelper.empty_payload_create()
        assert response.status_code == 400

    @allure.title("Проверка успешности создания курьера с пустым login")
    @allure.description("Создание курьера, проверка статуса ответа")
    def test_create_courier_empty_login(self):
        response = helper.ChangeTestDataHelper.empty_login_create()
        assert response.status_code == 400
