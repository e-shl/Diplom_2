import pytest
import allure


from pages.order_api import OrderPage
from tests_data import HTTP_STATUS_OK, HTTP_STATUS_BAD, HTTP_STATUS_ERROR


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа под зарегистрированным пользователем")
    def test_create_order_auth(self, base_random_user):
        order_id = OrderPage.get_ingredients().json()["data"][0]["_id"]
        payload = {"ingredients": [order_id]}
        # Создание заказа под зарегистрированным пользователем
        response_create_order = OrderPage.create_order_auth(base_random_user[0],payload)[0]
        json = response_create_order.json()
        assert response_create_order.status_code == HTTP_STATUS_OK
        assert json["success"] is True
        assert json["order"]["number"]

    @allure.title("Создание заказа не зарегистрированным пользователем")
    def test_create_order_unauth(self):
        order_id = OrderPage.get_ingredients().json()["data"][0]["_id"]
        payload = {"ingredients": [order_id]}
        response_create_order = OrderPage.create_order(payload)
        json = response_create_order.json()
        assert response_create_order.status_code == HTTP_STATUS_OK
        assert json["success"] is True
        assert json["order"]["number"]

    @allure.title("Создание заказа без ингредиентов")
    def test_create_invalid_not_ingredient(self):
        payload = {"ingredients": ""}
        response_create_order = OrderPage.create_order(payload)
        json = response_create_order.json()
        assert response_create_order.status_code == HTTP_STATUS_BAD
        assert json["success"] is False
        assert json["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_invalid_hash_ingredient(self):
        payload = {"ingredients": "000xxx000"}
        response_create_order = OrderPage.create_order(payload)
        assert response_create_order.status_code == HTTP_STATUS_ERROR
