from selene import browser, have

def test_successful_login():
    browser.open('https://school.qa.guru')
    # Ввести адрес электронной почты
    browser.element("[name=email]").type("fobozzz@yandex.ru")
    # Ввести пароль
    browser.element("[name=password]").type("33p4AC&A")
    # Нажать кнопку "Войти"
    browser.element(".btn-success").click()
    # Проверить успешную авторизацию
    browser.element(".page-header").should(have.text("Список тренингов"))

def test_successful_login_akk():
    browser.open("https://school.qa.guru/cms/system/login")
    # Проверить успешную авторизацию аккаунтом
    browser.element(".logined-form").should(have.text("Здравствуйте, Artur"))
    browser.quit()


def test_negative_login():
    browser.open("https://school.qa.guru")
    # Ввести адрес электронной почты
    browser.element("[name=email]").type("fobozzz@yandex.ru")
    # Ввести пароль
    browser.element("[name=password]").type("33p4AC&Artrt")
    # Нажать кнопку "Войти"
    browser.element(".btn-success").click()
    # Проверить не удачную авторизацию с неверным паролем
    browser.element(".btn-error").should(have.text("Неверный пароль"))
    browser.quit()


def test_negative_empty_login():
    browser.open("https://school.qa.guru")
    # Нажать на Вход
    browser.element(".btn-success").click()
    # Проверить не удачную авторизацию с незаполненным логином
    browser.element(".btn-error").should(have.text("Не заполнено поле E-Mail"))
    browser.quit()
