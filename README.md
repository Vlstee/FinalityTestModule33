# FinalityTestModule33
Итоговый проект Ростелеком.
Протестирован новый интерфейс регистрации/авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии.
Требования заказчика:https://docs.google.com/document/d/1qMwOxHAvL_u4LGKqaH7LpRDgS7JKUydB/edit?usp=sharing&ouid=111121881214509205181&rtpof=true&sd=true
Объект тестирования: https://b2c.passport.rt.ru
Тестирование документации: https://docs.google.com/spreadsheets/d/1nysUrjredVeNI9qEc5vWkPS09U2CDznc4a0ra7Jzs6k/edit?usp=sharing
Bugreport: https://docs.google.com/spreadsheets/d/1mrgAHug8-E6SOK0-7gQqGoB1S_SEkT4t9z1sEV0wvGo/edit?usp=sharing
Test case: https://docs.google.com/spreadsheets/d/1hgivCrq-PIDNC-wukvC-JatwnhCnO-TQmISPfGJRRd0/edit?usp=sharing


Папка pages содержит 4 файла:
-auth_page.py класс страницы авторизации сайта Ростелеком;
-reg_page.py класс страницы регистрации сайта;
-base_page.py базовый класс страницы и методы для тестирования;
-elements.py классы методов для взаимодействия с веб-элементами на странице.
Папка tests содержит 2 файла:
-test_auth_page.py автоматизированные тесты для страницы авторизации сайта;
-test_reg_page.py автоматизированные тесты для страницы регистрации;
Остальные файлы:
-conftest.py данные для проведения тестирования;
-requirments зависимости для запуска проекта;
-settings.py валидные данные для тестирования;
Инструменты для тестирования:
-Selenium WebDriver для автотестов.
Применимые техники тест-дизайна:
Классы эквивалентности, граничные значения применимы для полей ввода «Имя», «Фамилия», «Телефон», «Пароль».
