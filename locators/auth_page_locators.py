from selenium.webdriver.common.by import By


class AuthPageLocators:

    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") # поле ввода email
    PASSWORD = (By.NAME, "Пароль") # поле ввода password
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка Войти в форме авторизации