import allure
import helper


class TestLoginCourier:

    @allure.title("Проверка успешности логина курьера")
    @allure.description("Логин курьера, проверка статуса ответа и значения id")
    def test_login_courier(self):
        response = helper.ChangeTestDataHelper.login_courier
        # Преобразование ответа в JSON
        data = response.json()
        # Проверка значения id и кода ответа
        assert response.status_code == 200 and data.get("id") == 332818

    @allure.title("Проверка успешности логина курьера с пустым телом запроса")
    @allure.description("Создание курьера, проверка статуса ответа")
    def test_login_courier_empty_payload(self):
        response = helper.ChangeTestDataHelper.login_empty_payload
        assert response.status_code == 400

    @allure.title("Проверка успешности логина курьера с несуществующим логином и паролем")
    @allure.description("Создание курьера, проверка статуса ответа")
    def test_login_non_exist_login_password(self):
        response = helper.ChangeTestDataHelper.login_non_exist
        assert response.status_code == 404


    @allure.title("Проверка успешности создания курьера с пустым password")
    @allure.description("Создание курьера, проверка статуса ответа")
    def test_login_courier_empty_payload(self):
        response = helper.ChangeTestDataHelper.login_non_exist_password
        assert response.status_code == 400

