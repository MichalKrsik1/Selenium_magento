from selenium.webdriver.common.by import By
from page_objects.account_info_page import AccountInfoPage


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    first = (By.ID, "firstname")
    last = (By.ID, "lastname")
    email = (By.ID, "email_address")
    password = (By.ID, "password")
    conf_password = (By.ID, "password-confirmation")
    create_btn = (By.CLASS_NAME, "submit")

    def register(self):
        """ Manually change email before running the test! """
        self.driver.find_element(*RegistrationPage.first).send_keys("John9")
        self.driver.find_element(*RegistrationPage.last).send_keys("Doe9")
        self.driver.find_element(*RegistrationPage.email).send_keys("ydrummurdy9@gmail.com")
        self.driver.find_element(*RegistrationPage.password).send_keys("Ffdlgbzu123")
        self.driver.find_element(*RegistrationPage.conf_password).send_keys("Ffdlgbzu123")
        self.driver.find_element(*RegistrationPage.create_btn).click()
        account_info_page = AccountInfoPage(self.driver)
        return account_info_page
