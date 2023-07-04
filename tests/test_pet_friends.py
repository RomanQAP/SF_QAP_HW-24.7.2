from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password

pf = PetFriends()

""" 
В данной библиотеке тестов, только 1, 12, 13 тесты будут пройдены успешно, остальные тесты заведомо заваленные, 
т.к. на сайте есть баги :(

Если хотите проверить результат работы тестов непосредственно на сайте, закомментируйте метод teardown в конце кода.

Список тестов:
1) Запрос API ключа с неверными email и password.
2) Создание питомца с пустыми полями.
3) Поле "Имя питомца" на максимальное допустимое значение.
4) Поле "Имя питомца" на ввод цифр.
5) Поле "Имя питомца" на ввод спецсимволов.
6) Поле "Порода" на максимальное допустимое значение.
7) Поле "Порода" на ввод цифр.
8) Поле "Порода" на ввод спецсимволов.
9) Поле "Возраст" на максимальное допустимое значение.
10) Поле "Возраст" на ввод букв.
11) Поле "Возраст" на отрицательный возраст.

Тесты не реализованные в модуле из-за отсутствия нереализованных методов в модуле.
12) Создание питомца без фото с валидным email и password.
13) Добавление фото к существующему питомцу.
"""


# Тест 1
def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """Проверяем, что API ключ невозможно получить с неверным email и password"""

    # Делаем вызов из библиотеки и полученные результаты сохраняем в переменные
    status, result = pf.get_api_key(email, password)

    # Сверяем полученный результат с нашими ожиданиями
    assert status == 403
    assert 'key' not in result


# Тест 2
def test_not_add_new_pet_without_photo_with_emperty_fields(name='', animal_type='', age=''):
    """Проверяем, что нельзя создать питомца с пустыми полями"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем статус код и, что поле name не является пустым, если вернется в ответе.
    assert status == 403
    assert result['name'] != ''


# Тест 3
def test_field_name_pet_max_value(animal_type='Кот', age='1'):
    """Проверяем максимальное кол-во символов в поле 'Имя питомца'"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Генерируем 256 символов, что бы не забивать в ручную. (4 символа в 'cat_' * 64 == 256 символов)
    name = 'cat_' * 64

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем статус код
    assert status == 403


# Тест 4
def test_field_name_pet_no_numbers(name='123', animal_type='Кот', age='1'):
    """Проверяем, что в поле 'Имя питомца' нельзя вписать цифры"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем статус код и полученный ответ с ожидаемым результатом
    assert status == 403
    assert result['name'] != '123'


# Тест 5
def test_field_name_pet_special_characters(name='!&^', animal_type='Кот', age='1'):
    """Проверяем, что в поле 'Имя питомца' нельзя вписать спец. символы"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем статус код и полученный ответ с ожидаемым результатом
    assert status == 403
    assert result['name'] != '!&^'


# Тест 6
def test_field_animal_type_max_value(name='Котэ', age='1'):
    """Проверяем максимальное кол-во символов в поле 'Порода'"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Генерируем 256 символов, что бы не забивать в ручную. (4 символа в 'кот_' * 64 == 256 символов)
    animal_type = 'кот_' * 64

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем статус код
    assert status == 403


# Тест 7
def test_field_animal_type_no_numbers(name='Котэ', animal_type='123', age='1'):
    """Проверяем, что в поле 'Порода' нельзя вписать цифры"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем статус код и полученный ответ с ожидаемым результатом
    assert status == 403
    assert result['animal_type'] != '123'


# Тест 8
def test_field_animal_type_special_characters(name='Котэ', animal_type='!&^', age='1'):
    """Проверяем, что в поле 'Порода' нельзя вписать спец. символы"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем статус код и полученный ответ с ожидаемым результатом
    assert status == 403
    assert result['animal_type'] != '!&^'


# Тест 9
def test_field_age_type_max_value(name='Котэ', animal_type='Кот'):
    """Проверяем максимальное кол-во символов в поле 'Возраст'"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Генерируем 256 символов, что бы не забивать в ручную. (4 символа в '123_' * 64 == 256 символов)
    age = '123_' * 64

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем статус код
    assert status == 403


# Тест 10
def test_field_age_no_letters(name='Котэ', animal_type='кот', age='абв'):
    """Проверяем, что в поле 'возраст' нельзя вписать буквы"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем статус код и полученный ответ с ожидаемым результатом
    assert status == 403
    assert result['age'] != 'абв'


# Тест 11
def test_field_age_negative_numbers(name='Котэ', animal_type='кот', age='-1'):
    """Проверяем, что в поле 'возраст' нельзя вписать отрицательное значение"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем статус код
    assert status == 403
    assert result['age'] < 0


# Тест 12
def test_add_new_pet_without_photo(name='Котэ', animal_type='Кот', age='2'):
    """Проверяем возможность создания питомца без фото с валидным email и password"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


# Тест 13
def test_add_photo_of_pet(pet_photo='images\cat1.jpg'):
    """Проверяем возможность добавления фото к существующему питомцу"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем наличие питомца, иначе создаем нового без фото.
    if len(my_pets['pets']) == 0:
        pf.add_new_pet_without_photo(auth_key, "Суперкот", "кот", "3")

    # Вновь запрашиваем список питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Берем ID питомца и отправляет запрос на добавление фото.
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)

    # Проверяем что статус ответа равен 200 и наличие фото.
    assert status == 200
    assert result['pet_photo'] != ""


# Создаем метод teardown, что бы в конце тестов удалить всех питомцев из списка, бережем память серверов :)
def teardown(self):
    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    while len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
        status, _ = pf.delete_pet(auth_key, pet_id)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    print(f'Питомцы удалены в списке: {len(my_pets["pets"])}')
