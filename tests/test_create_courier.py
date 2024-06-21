from conftest import default_courier
from conftest import empty_payload_create
import allure


class TestCreateCourier:

    @allure.title("Проверка успешности создания курьера")
    @allure.description("Создание курьера, проверка статуса ответа")
    def test_success_create_courier(self, default_courier):
        response = default_courier
        assert response.status_code == 201

    @allure.title("Проверка успешности создания курьера с теми же данными")
    @allure.description("Создание курьера, проверка статуса ответа")
    def test_create_duplicate_courier(self, default_courier):
        response = default_courier
        assert response.status_code == 409

    @allure.title("Проверка успешности создания курьера с пустым телом запроса")
    @allure.description("Создание курьера, проверка статуса ответа")
    def test_create_courier_empty_payload(self, empty_payload_create):
        response = empty_payload_create
        assert response.status_code == 400