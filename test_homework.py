from datetime import time

def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if 22 <= current_time.hour or current_time.hour  < 6:
        should_use_dark_theme = True
    else:
        should_use_dark_theme = False
    is_dark_theme =should_use_dark_theme
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток, но учтите что темная тема может быть включена вручную
    is_night = 22 <= current_time.hour or current_time.hour < 6
    if dark_theme_enabled_by_user is not None:
        should_use_dark_theme = dark_theme_enabled_by_user
    else:
        should_use_dark_theme = is_night

    is_dark_theme = should_use_dark_theme
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    user = next((u for u in users if u["name"] == "Olga"), None)
    suitable_users = user
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    filtered_users = list(filter(lambda u: u["age"] < 20, users))
    suitable_users = filtered_users
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    readable_name = open_browser.__name__.replace('_', ' ').title()
    args_str = f"[{browser_name}]"
    actual_result = f"{readable_name} {args_str}"
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    readable_name = go_to_companyname_homepage.__name__.replace('_', ' ').title()
    args_str = f"[{page_url}]"
    actual_result = f"{readable_name} {args_str}"
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    readable_name = find_registration_button_on_login_page.__name__.replace('_', ' ').title()
    args_str = f"[{page_url}, {button_text}]"
    actual_result = f"{readable_name} {args_str}"
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
    return (actual_result)