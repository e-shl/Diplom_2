from faker import Faker

fake = Faker() # создали объект-генератор

class User:

    @staticmethod
    def new_user_payload_registration():
        payload = {
            "email": f"{fake.name().replace(" ", "")}{fake.email()}",
            "password": fake.password(),
            "name": fake.name()
        }
        return payload

    @staticmethod
    def new_user_payload_login_whiteout_registration():
        payload = {
            "email": f"{fake.name().replace(" ", "")}{fake.email()}",
            "password": fake.password(),
        }
        return payload


# Ожидаемые статусы для различных сценариев
HTTP_STATUS_OK = 200           # универсальный статус удачного запроса
HTTP_STATUS_FORBIDDEN = 403           # статус ошибки в полях запроса
HTTP_STATUS_UNAUTHORIZED = 401           # статус ошибка авторизации
HTTP_STATUS_BAD = 400           # пустые данные
HTTP_STATUS_ERROR = 500           # неверные дынные
