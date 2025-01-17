BASE_URL = "https://stellarburgers.nomoreparties.site"

# User URLs
CREATE_USER_URL = BASE_URL + "/api/auth/register"  # Создание пользователя
PROFILE_USER_URL = BASE_URL + "/api/auth/user"  #  Получения/удаление/обновления данных пользователя
LOGIN_USER_URL = BASE_URL + "/api/auth/login"  #  Авторизация пользователя

# Orders URLs
INGREDIENT_URL = BASE_URL + "/api/ingredients"  # Получение данных об ингредиентах
CREATE_ORDER_URL = BASE_URL + "/api/orders"  # Создание заказа
GET_USER_ORDERS_URL = BASE_URL + "/api/orders"  # Получить заказы конкретного пользователя