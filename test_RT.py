# python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_SF_RT_passport.py


from time import sleep
from base_data import *
from data import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### 1. Для тест-кейса TC-rt-001. Проверка успешного входа в аккаунт по логину.

def test_001(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_login)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'
    
 ### 2. Для тест-кейса TC-rt-001. Проверка возникновения ошибки авторизации при введении неверного пароля.
def test_001_wrong(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_login)
    form.password.send_keys(wrong_pass)
    sleep(5)
    form.btn_click()

    text_wrong = form.driver.find_element(By.ID, 'form-error-message')
    assert text_wrong.text == 'Неверный логин или пароль'
    
 

### 3. Для тест-кейса TC-rt-003. Проверка успешного входа в аккаунт по номеру телефона.

def test_003(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'

### 4. Для тест-кейса TC-rt-003. Проверка возникновения ошибки авторизации при введении неверного пароля.
def test_003_wrong(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(wrong_pass)
    sleep(5)
    form.btn_click()

    text_wrong = form.driver.find_element(By.ID, 'form-error-message')
    assert text_wrong.text == 'Неверный логин или пароль'
    
### 5. Для тест-кейса TC-rt-004. Проверка успешного входа в аккаунт по электронной почте.

def test_004(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_email)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'
    
### 6. Для тест-кейса TC-rt-004. Проверка возникновения ошибки авторизации при введении неверного пароля.
def test_004_wrong(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_email)
    form.password.send_keys(wrong_pass)
    sleep(5)
    form.btn_click()

    text_wrong = form.driver.find_element(By.ID, 'form-error-message')
    assert text_wrong.text == 'Неверный логин или пароль'
    
 ### 7. Для тест-кейса TC-rt-005. Проверка успешного входа в аккаунт по номеру лицевого счёта.

def test_005(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_personalnum)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'
    
### 8. Для тест-кейса TC-rt-005. Проверка возникновения ошибки авторизации при введении неверного пароля.
def test_005_wrong(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_personalnum)
    form.password.send_keys(wrong_pass)
    sleep(5)
    form.btn_click()

    text_wrong = form.driver.find_element(By.ID, 'form-error-message')
    assert text_wrong.text == 'Неверный логин или пароль'
    
 
### 9. Для тест-кейса TC-rt-002. Проверка автоматической смены таба ввода авторизации.
def test_002(selenium):
    form = AuthForm(selenium)

    # ввод логина
    form.username.send_keys(valid_login)
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Логин'

    # Удаление введенных данных
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод почты
    form.username.send_keys(valid_email)
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Электронная почта'

    # Удаление введенных данных
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод лицевого счета
    form.username.send_keys(valid_personalnum)
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Лицевой счёт'
    
    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Мобильный телефон'
 









### тест EXP-016 - проверка получения временного кода на телефон и открытия формы для ввода кода
def test_016_get_code(selenium):
    form = CodeForm(selenium)

    # ввод телефона
    form.address.send_keys(valid_phone)

    # длительная пауза предназначена для ручного ввода капчи при необходимости
    sleep(30)
    form.get_click()

    rt_code = form.driver.find_element(By.ID, 'rt-code-0')

    assert rt_code


### тест EXP-020 - проверка перехода в форму восстановления пароля и её открытия
def test_020_forgot_pass(selenium):
    form = AuthForm(selenium)

    # клик по надписи "Забыл пароль"
    form.forgot.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Восстановление пароля'


### тест EXP-021 - проверка перехода в форму регистрации и её открытия
def test_021_register(selenium):
    form = AuthForm(selenium)

    # клик по надписи "Зарегистрироваться"
    form.register.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Регистрация'
