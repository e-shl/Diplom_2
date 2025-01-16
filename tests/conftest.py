import pytest
import requests

from pages.user_api import UserPage
from tests_data import User
from urls import CREATE_USER_URL


@pytest.fixture
def base_random_user():
    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    email_password_name = User.new_user_payload_registration()
    response = UserPage.create_new_user(email_password_name)
    yield response, email_password_name
    UserPage.delete_user(response.json()["accessToken"])