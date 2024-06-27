import pytest
import allure
import helper
from conftest import create_order


class TestCreateOrder:

    @allure.title("Проверка создания заказа с разными цветами")
    @pytest.mark.parametrize("color", [
        pytest.param('BLACK'),
        pytest.param('GREY'),
    ])
    def test_failed_create_booking_with_different_totalprice(self, create_order, color):
        body = helper.ChangeTestDataHelper.modify_create_order_body("color", color)

        created_order_request = create_order(body)
        # Преобразование ответа в JSON
        response = create_order
        data = response.json()
        # Проверка значения track и кода ответа

        assert created_order_request.status_code == 201 and data.get("track") == 124124
