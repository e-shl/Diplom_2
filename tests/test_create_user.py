import pytest
import allure

from pages.user_api import UserPage
from tests_data import User, HTTP_STATUS_OK, HTTP_STATUS_FORBIDDEN


@allure.suite("Создание пользователя")
class TestCreateUser:

    @allure.title("Тест создать уникального пользователя")
    def test_create_unique_user(self):
        response = UserPage.create_user(User.new_user_payload_registration())
        json = response.json()
        assert response.status_code == HTTP_STATUS_OK
        assert json["success"] is True
        assert json["user"]["email"] is not None and json["user"]["name"]
        assert json["accessToken"]
        assert json["refreshToken"]
        token = json["accessToken"]
        UserPage.delete_user(token)

    @allure.title("Тест создать пользователя, который уже зарегистрирован")
    def test_create_duplicate_user(self):
        payload = User.new_user_payload_registration()
        response1 = UserPage.create_user(payload)
        token = response1.json()["accessToken"]
        response2 = UserPage.create_user(payload)
        json2 = response2.json()
        assert response2.status_code == HTTP_STATUS_FORBIDDEN
        assert json2["success"] is False
        assert json2["message"] == "User already exists"
        UserPage.delete_user(token)

    @pytest.mark.parametrize('remove_fields', ['email', 'password', 'name'])
    @allure.title("Тест создать пользователя и не заполнить одно из обязательных полей: {remove_fields}")
    @allure.description("если одного из полей нет, запрос возвращает ошибку")
    def test_create_remove_fields_courier_error_missing(self, remove_fields):
        # Удаление одного из полей запроса
        user_payload_no_fields = User.new_user_payload_registration().pop(remove_fields)
        response  = UserPage.create_user(user_payload_no_fields)
        json = response.json()
        assert response.status_code == HTTP_STATUS_FORBIDDEN
        assert json["success"] is False
        assert json["message"] == "Email, password and name are required fields"


