import pytest
from selenium import webdriver
from pages.reg_page import RegistrationPage


def generate_string(num):
    return "а" * num


@pytest.mark.parametrize("first_name", ['Aa-Aа', generate_string(2), generate_string(3), generate_string(15),
                                        generate_string(29), generate_string(30)],
                         ids=['с дефисом', '2 символа', '3 символа', '15 символов', '29 символов', '30 символов'])
def test_first_name_field_positive(first_name):
    """Позитивные проверки для поля ввода имени """
    web_browser = webdriver.Chrome()
    page = RegistrationPage(web_browser)
    web_browser.implicitly_wait(10)
    page.register_link.click()
    page.wait_page_loaded()
    page.first_name_field.send_keys(first_name)
    page.data_field.click()
    assert page.warning_message_names.get_text() == ''
    page.close()


@pytest.mark.parametrize("first_name", [generate_string(1), generate_string(31), "latin"],
                         ids=["1 символ", "31 символ", "латинские буквы"])
def test_first_name_field_negative(first_name):
    """Негативные проверки для поля ввода имени """
    web_browser = webdriver.Chrome()
    page = RegistrationPage(web_browser)
    web_browser.implicitly_wait(10)
    page.register_link.click()
    page.wait_page_loaded()
    page.first_name_field.send_keys(first_name)
    page.data_field.click()
    assert page.warning_message_names.get_text() != ''
    print(page.warning_message_names.get_text())
    page.close()


@pytest.mark.parametrize("last_name", [generate_string(2), generate_string(3), generate_string(15),
                                       generate_string(29), generate_string(30), "аа-аа"],
                         ids=['2 символа', '3 символа', '15 символов', '29 символов', '30 символов','с дефисом'])
def test_last_name_field_positive(last_name):
    """Позитивные проверки для поля ввода фамилии"""
    web_browser = webdriver.Chrome()
    page = RegistrationPage(web_browser)
    web_browser.implicitly_wait(10)
    page.register_link.click()
    page.wait_page_loaded()
    page.last_name_field.send_keys(last_name)
    page.data_field.click()
    assert page.warning_message_names.get_text() == ''
    page.close()


@pytest.mark.parametrize("last_name", [generate_string(1), generate_string(31), "latin"],
                         ids=['1 символ', '31 символ', 'латинские буквы'])
def test_last_name_fields_negative(last_name):
    """Негативные проверки для поля ввода фамилии"""
    web_browser = webdriver.Chrome()
    page = RegistrationPage(web_browser)
    web_browser.implicitly_wait(10)
    page.register_link.click()
    page.wait_page_loaded()
    page.last_name_field.send_keys(last_name)
    page.data_field.click()
    assert page.warning_message_names.get_text() != ''
    print(page.warning_message_names.get_text())
    page.close()


@pytest.mark.parametrize("data", ["mail12345@mail.ru", "+79990000000", "+375123456789"],
                         ids=["корректный адрес", "корректный рос-номер", "корректный бел-номер"])
def test_data_field_positive(data):
    """Позитивные проверки для полей ввода адреса электронной почты или номера телефона"""
    web_browser = webdriver.Chrome()
    page = RegistrationPage(web_browser)
    web_browser.implicitly_wait(10)
    page.register_link.click()
    page.wait_page_loaded()
    page.data_field.send_keys(data)
    page.password_input.click()
    assert page.warning_message_data.get_text() == ''
    page.close()


@pytest.mark.parametrize("data", ["mail12345@@mail.ru", "+7999000000", "+37512345678", "+3751234567890"],
                         ids=["некорректный адрес", "некорректный рос-номер(10 цифр)",
                              "некорректный бел-номер(8 цифр)",
                              "некорректный формат бел-номера(10 цифр)"])
def test_data_field_negative(data):
    """Негативные проверки для полей ввода адреса электронной почты или номера телефона"""
    web_browser = webdriver.Chrome()
    page = RegistrationPage(web_browser)
    web_browser.implicitly_wait(10)
    page.register_link.click()
    page.wait_page_loaded()
    page.data_field.send_keys(data)
    page.password_input.click()
    assert page.warning_message_data.get_text() != ' '
    print(page.warning_message_data.get_text())
    page.close()


@pytest.mark.parametrize("password", ["Pa$sword1", "Password1", "Password11Password1"],
                         ids=["спецсимвол и состоит из 9 символов", "цифра и состоит из 9 символов", "19 символов"])
def test_password_field_positive(password):
    """Позитивная проверка поля ввода пароля"""
    web_browser = webdriver.Chrome()
    page = RegistrationPage(web_browser)
    web_browser.implicitly_wait(10)
    page.register_link.click()
    page.wait_page_loaded()
    page.password_input.send_keys(password)
    page.password_confirm.click()
    page.register_button.click()
    assert page.warning_message_pass.get_text() == ''
    page.close()


@pytest.mark.parametrize("password", ["passwor", "password", "password11", "парольпа", "Password11Password111"],
                         ids=["менее 8 символов", "нет спецсимвола или цифры", "без заглавной буквы",
                              "символы кириллицы", "более 20 символов"])
def test_password_field_negative(password):
    """Негативная проверка поля ввода пароля"""
    web_browser = webdriver.Chrome()
    page = RegistrationPage(web_browser)
    web_browser.implicitly_wait(10)
    page.register_link.click()
    page.wait_page_loaded()
    page.password_input.send_keys(password)
    page.password_confirm.click()
    assert page.warning_message_confirm_pass.get_text() != ' '
    print(page.warning_message_confirm_pass.get_text())
    page.close()


@pytest.mark.parametrize("password", ["Password11", "Password1"], ids=["корректный пароль", "некорректный пароль"])
def test_password_confirmed(password):
    """Проверка поля ввода пароля и подтверждения пароля"""
    web_browser = webdriver.Chrome()
    page = RegistrationPage(web_browser)
    web_browser.implicitly_wait(10)
    page.register_link.click()
    page.wait_page_loaded()
    page.password_input.send_keys("Password11")
    page.password_confirm.send_keys(password)
    page.register_button.click()
    if password == 'Password11':
        assert page.password_confirm.get_text() == ''
        print(page.password_confirm.get_text())
    else:
        assert page.warning_message_confirm_pass.get_text() != ''
        print(page.warning_message_confirm_pass.get_text())
    page.close()