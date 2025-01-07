import pytest
import requests
import allure

from pages.order_api import OrderPage
from tests_data import HTTP_STATUS_OK, HTTP_STATUS_UNAUTHORIZED


@allure.suite("Получение заказов конкретного пользователя")
class TestGetUserOrder:

    @allure.title("Получение номера заказа зарегистрированного пользователя")
    def test_get_user_order_auth(self):
        order_id =  OrderPage.get_ingredients().json()["data"][0]["_id"]
        payload = {"ingredients": [order_id]}
        response_token_order = OrderPage.create_order_auth(payload)
        response_order_create =  response_token_order[0]
        token = response_token_order[1]
        response_get_order = OrderPage.get_user_orders_auth(token)
        assert response_get_order.status_code == HTTP_STATUS_OK
        assert response_get_order.json()["success"] is True
        assert response_get_order.json()['orders'][0]['number'] == response_order_create.json()['order']['number']

    @allure.title("Попытка получения заказов незарегистрированного пользователя")
    def test_get_user_order_unauth(self):
        response_get_order = OrderPage.get_user_orders_unauth()
        assert response_get_order.status_code == HTTP_STATUS_UNAUTHORIZED
        assert response_get_order.json()["success"] is False