import requests
import allure

from urls import *


class UserPage:

    @staticmethod
    @allure.step("Создание пользователя")
    def create_new_user(email_password_name):
        # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
        response = requests.post(CREATE_USER_URL, data=email_password_name, timeout=20)
        return response

    @staticmethod
    @allure.step("Удаление курьера")
    def delete_user(token):
        # отправляем запрос на удаление курьера и сохраняем ответ в переменную response
        response = requests.delete(PROFILE_USER_URL, headers={"Authorization": token}, timeout=20)
        return response

    @staticmethod
    @allure.step("Авторизация курьера")
    def login_user(email_password):
        # отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response
        response = requests.post(LOGIN_USER_URL, data=email_password, timeout=20)
        return response