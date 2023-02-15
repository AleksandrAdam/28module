from time import sleep
from base_data import *
from data import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### 1. Для тест-кейса TC-rt-001. Проверка успешного входа в аккаунт по логину.

def test_001(selenium):
    form = Auth(selenium)

    # ввод телефона
    form.username.send_keys(valid_login)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'
    
 ### 2. Для тест-кейса TC-rt-001. Проверка возникновения ошибки авторизации при введении неверного пароля.
def test_001_wrong(selenium):
    form = Auth(selenium)

    # ввод телефона
    form.username.send_keys(valid_login)
    form.password.send_keys(wrong_pass)
    sleep(5)
    form.btn_click()

    text_wrong = form.driver.find_element(By.ID, 'form-error-message')
    assert text_wrong.text == 'Неверный логин или пароль'
    
 

### 3. Для тест-кейса TC-rt-003. Проверка успешного входа в аккаунт по номеру телефона.

def test_003(selenium):
    form = Auth(selenium)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'

### 4. Для тест-кейса TC-rt-003. Проверка возникновения ошибки авторизации при введении неверного пароля.
def test_003_wrong(selenium):
    form = Auth(selenium)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(wrong_pass)
    sleep(5)
    form.btn_click()

    text_wrong = form.driver.find_element(By.ID, 'form-error-message')
    assert text_wrong.text == 'Неверный логин или пароль'
    
### 5. Для тест-кейса TC-rt-004. Проверка успешного входа в аккаунт по электронной почте.

def test_004(selenium):
    form = Auth(selenium)

    # ввод телефона
    form.username.send_keys(valid_email)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'
    
### 6. Для тест-кейса TC-rt-004. Проверка возникновения ошибки авторизации при введении неверного пароля.
def test_004_wrong(selenium):
    form = Auth(selenium)

    # ввод телефона
    form.username.send_keys(valid_email)
    form.password.send_keys(wrong_pass)
    sleep(5)
    form.btn_click()

    text_wrong = form.driver.find_element(By.ID, 'form-error-message')
    assert text_wrong.text == 'Неверный логин или пароль'
    
 ### 7. Для тест-кейса TC-rt-005. Проверка успешного входа в аккаунт по номеру лицевого счёта.

def test_005(selenium):
    form = Auth(selenium)

    # ввод телефона
    form.username.send_keys(valid_personalnum)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'
    
### 8. Для тест-кейса TC-rt-005. Проверка возникновения ошибки авторизации при введении неверного пароля.
def test_005_wrong(selenium):
    form = Auth(selenium)

    # ввод телефона
    form.username.send_keys(valid_personalnum)
    form.password.send_keys(wrong_pass)
    sleep(5)
    form.btn_click()

    text_wrong = form.driver.find_element(By.ID, 'form-error-message')
    assert text_wrong.text == 'Неверный логин или пароль'
    
 
### 9. Для тест-кейса TC-rt-002. Проверка автоматической смены таба ввода авторизации.
def test_002(selenium):
    form = Auth(selenium)

    # ввод логина
    form.username.send_keys(valid_login)
    form.password.send_keys('_')
    sleep(5)

    assert form.place.text == 'Логин'

    # Удаление введенных данных
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод почты
    form.username.send_keys(valid_email)
    form.password.send_keys('_')
    sleep(5)

    assert form.place.text == 'Электронная почта'

    # Удаление введенных данных
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод лицевого счета
    form.username.send_keys(valid_personalnum)
    form.password.send_keys('_')
    sleep(5)

    assert form.place.text == 'Лицевой счёт'
    
    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys('_')
    sleep(5)

    assert form.place.text == 'Мобильный телефон'
 
### 10. Для тест-кейса TC-rt-006. Проверка перехода в форму регистрации
def test_006(selenium):
    form = Auth(selenium)

    # "Зарегистрироваться"
    form.register.click()
    sleep(5)

    final_h = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert final_h.text == 'Регистрация'

### 11. Для тест-кейса TC-rt-007. Проверка перехода в форму восстановления
def test_007(selenium):
    form = Auth(selenium)

    # "Забыл пароль"
    form.forgotpass.click()
    sleep(5)

    final_h = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert final_h.text == 'Восстановление пароля'

### 12. Для тест-кейса TC-rt-011. Проверка получения временного кода на телефон в системе Старт WEB
def test_011_phone(selenium):
    form = Code(selenium)

    # ввод номера телефона
    form.address.send_keys(valid_phone)
    sleep(30)
    form.get_click()

    rt_code = form.driver.find_element(By.ID, 'rt-code-0')

    assert rt_code

    ### 13. Для тест-кейса TC-rt-011. Проверка получения временного кода на электронную почту в системе Старт WEB
def test_011_email(selenium):
    form = Code(selenium)

    # ввод номера телефона
    form.address.send_keys(valid_email)
    sleep(30)
    form.get_click()

    rt_code = form.driver.find_element(By.ID, 'rt-code-0')

    assert rt_code

### 14. Для тест-кейса TC-rt-015. Проверка получения временного кода на электронную почту в системе KEY WEB
def test_011_email(selenium):
    form = Code2(selenium)

    # ввод номера телефона
    form.address.send_keys(valid_email)
    sleep(30)
    form.get_click()

    rt_code = form.driver.find_element(By.ID, 'rt-code-0')

    assert rt_code
  
### 15. Для тест-кейса TC-rt-015. Проверка получения временного кода на телефон в системе KEY WEB
def test_011_phone(selenium):
    form = Code2(selenium)

    # ввод номера телефона
    form.address.send_keys(valid_phone)
    sleep(30)
    form.get_click()

    rt_code = form.driver.find_element(By.ID, 'rt-code-0')

    assert rt_code

