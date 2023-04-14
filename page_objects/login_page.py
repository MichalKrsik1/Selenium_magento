from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects.home_page import HomePage

DEFAULT_EMAIL = "ydrummurdy1@gmail.com"
DEFAULT_PASSWORD = "Ffdlgbzu123"


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    _email = (By.ID, "email")
    _password = (By.ID, "pass")
    _login_btn = (By.ID, "send2")

    def login(self, email=DEFAULT_EMAIL, password=DEFAULT_PASSWORD):
        self.driver.find_element(*LoginPage._email).send_keys(email)
        self.driver.find_element(*LoginPage._password).send_keys(password, Keys.RETURN)

        return HomePage(self.driver)
