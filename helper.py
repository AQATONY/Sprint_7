import data
import allure


class ChangeTestDataHelper:

    @staticmethod
    @allure.step("Создание заказа")
    def modify_create_order_body(key, value):
        body = data.TestDataCreateOrder.CREATE_ORDER_BODY.copy()
        body[key] = value

        return body
