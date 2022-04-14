# Тестирование API

Цель:
Поучиться тестировать API сервисов на основе их документации.

Описание/Пошаговая инструкция выполнения домашнего задания:
Тестирование каждого api оформить в отдельном тестовом модуле.

###Тестирование REST сервиса 1 
Написать минимум 5 тестов для REST API сервиса: https://dog.ceo/dog-api/. Как минимум 2 из 5 должны использовать параметризацию. Документация к API есть на сайте. Тесты должны успешно проходить.
###Тестирование REST сервиса 2 
Написать минимум 5 тестов для REST API сервиса: https://www.openbrewerydb.org/. Как минимум 2 из 5 должны использовать параметризацию. Документация к API есть на сайте. Тесты должны успешно проходить.
###Тестирование REST сервиса 3. 
Написать минимум 5 тестов для REST API сервиса: https://jsonplaceholder.typicode.com/. Как минимум 2 из 5 должны использовать параметризацию. Документация к API есть на сайте. Тесты должны успешно проходить.<br>
Реализуйте в отдельном модуле (файле) тестовую функцию которая будет принимать 2 параметра: url - должно быть значение по умолчанию https://ya.ru status_code - значение по умолчанию 200 Параметры должны быть реализованы через pytest.addoption. Можно положить фикcтуру и тестовую функцию в один файл. Основная задача чтобы ваш тест проверял по переданному урлу статус ответа тот который передали, т.е. по адресу https://ya.ru/sfhfhfhfhfhfhfhfh должен быть валидным ответ 404 пример запуска pytest test_module.py --url=https://mail.ru --status_code=200
