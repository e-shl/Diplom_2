import pytest
import allure
import requests

from pages.user_api import UserPage
from tests_data import User, HTTP_STATUS_OK, HTTP_STATUS_UNAUTHORIZED
from urls import PROFILE_USER_URL


@allure.suite("Изменение данных пользователя")
class TestUpdateDataUser:

    @pytest.mark.parametrize('changed_fields', ['email', 'name'])
    @allure.title("Изменение {changed_fields} авторизованного пользователя")
    def test_update_data_user_auth(self, changed_fields, base_random_user):
        # Создание пользователя
        registration_response = base_random_user[0]
        # Получение токена авторизации
        token = registration_response.json()["accessToken"]
        # Данные для обновления
        payload = {changed_fields: User.new_user_payload_registration()[changed_fields]}
        response = requests.patch(PROFILE_USER_URL, headers={"Authorization": token}, data=payload)
        json = response.json()
        assert response.status_code == HTTP_STATUS_OK
        assert json["success"] is True
        assert json["user"][changed_fields] == payload[changed_fields]

    @allure.title("Изменение password авторизованного пользователя")
    def test_update_password_user_auth(self, base_random_user):
        # Создание пользователя
        registration_response = base_random_user[0]
        # Получение токена авторизации
        token = registration_response.json()["accessToken"]
        # Данные для обновления
        payload = {"password": User.new_user_payload_registration()["password"]}
        response = requests.patch(PROFILE_USER_URL, headers={"Authorization": token}, data=payload)
        json = response.json()
        assert response.status_code == HTTP_STATUS_OK
        assert json["success"] is True

    @pytest.mark.parametrize('changed_fields', ['email', 'name'])
    @allure.title("Изменение {changed_fields} не авторизованного пользователя")
    def test_update_data_user_unauth(self, changed_fields):
        payload = {changed_fields: User.new_user_payload_registration()[changed_fields]}
        response = requests.patch(PROFILE_USER_URL, data=payload)
        json = response.json()
        assert response.status_code == HTTP_STATUS_UNAUTHORIZED
        assert json["success"] is False
        assert json["message"] == "You should be authorised"

