from selenium.webdriver.common.by import By
from page_objects.account_info_page import AccountInfoPage

FIRST_NAME = "John9"
LAST_NAME = "Doe9"
EMAIL = "ydrummurdy9@gmail.com"
PASSWORD = "Ffdlgbzu123"


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    _first_name = (By.ID, "firstname")
    _last_name = (By.ID, "lastname")
    _email = (By.ID, "email_address")
    _password = (By.ID, "password")
    _conf_password = (By.ID, "password-confirmation")
    _create_btn = (By.CLASS_NAME, "submit")

    def register(self):
        self.driver.find_element(*RegistrationPage._first_name).send_keys(FIRST_NAME)
        self.driver.find_element(*RegistrationPage._last_name).send_keys(LAST_NAME)
        self.driver.find_element(*RegistrationPage._email).send_keys(EMAIL)
        self.driver.find_element(*RegistrationPage._password).send_keys(PASSWORD)
        self.driver.find_element(*RegistrationPage._conf_password).send_keys(PASSWORD)
        self.driver.find_element(*RegistrationPage._create_btn).click()
        return AccountInfoPage(self.driver)
