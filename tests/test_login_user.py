import pytest
import allure

from pages.user_api import UserPage
from tests_data import User, HTTP_STATUS_UNAUTHORIZED, HTTP_STATUS_OK


@allure.suite("Авторизация пользователя")
class TestLoginUser:

    @allure.title("Тест логин под существующим пользователем")
    def test_success_login(self):
        # Создание пользователя
        payload = User.new_user_payload_registration()
        UserPage.create_user(payload)
        # Авторизация пользователя
        response = UserPage.login_user(payload)
        json = response.json()
        assert response.status_code == HTTP_STATUS_OK
        assert json["success"] is True
        assert json["accessToken"]
        assert json["refreshToken"]
        assert json["user"]["email"] is not None and json["user"]["name"]
        token = json["accessToken"]
        UserPage.delete_user(token)

    @allure.title("Тест логин с неверным логином и паролем")
    def test_unsuccessful_login(self):
        # Авторизация с незарегистрированными логином и паролем
        response = UserPage.login_user(User.new_user_payload_login_whiteout_registration())
        json = response.json()
        assert response.status_code == HTTP_STATUS_UNAUTHORIZED
        assert json["success"] is False
        assert json["message"] == "email or password are incorrect"