from selenium.webdriver.common.by import By
from page_objects.home_page import HomePage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.ID, "email")
    password = (By.ID, "pass")
    login_btn = (By.ID, "send2")

    def login(self):
        email = "ydrummurdy1@gmail.com"
        password = "Ffdlgbzu123"

        self.driver.find_element(*LoginPage.email).send_keys(email)
        self.driver.find_element(*LoginPage.password).send_keys(password)
        self.driver.find_element(*LoginPage.login_btn).click()

        home_page = HomePage(self.driver)
        return home_page
