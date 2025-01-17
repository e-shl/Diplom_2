import requests
import allure

from pages.user_api import UserPage
from tests_data import User
from urls import *


class OrderPage:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        response = requests.post(CREATE_ORDER_URL, data=payload, timeout=20)
        return response

    @staticmethod
    @allure.step("Создание заказа под зарегистрированным пользователем")
    def create_order_auth(user, payload):
        json = user.json()
        token = json["accessToken"]
        # отправляем запрос на создание заказа под зарегистрированным пользователем и сохраняем ответ в переменную response
        response_create_order = requests.post(CREATE_ORDER_URL, data=payload, headers={"Authorization": token}, timeout=20)
        return response_create_order, token

    @staticmethod
    @allure.step("Получение ингридиентов")
    def get_ingredients():
        return requests.get(INGREDIENT_URL)

    @staticmethod
    @allure.step("Получить заказы конкретного пользователя под зарегистрированным пользователем")
    def get_user_orders_auth(token):
        return requests.get(GET_USER_ORDERS_URL, headers={"Authorization": token})

    @staticmethod
    @allure.step("Получить заказы конкретного пользователя")
    def get_user_orders_unauth():
        return requests.get(GET_USER_ORDERS_URL)

