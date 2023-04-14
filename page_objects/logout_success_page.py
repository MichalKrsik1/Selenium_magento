from selenium.webdriver.common.by import By


class LogoutSuccessPage:

    def __init__(self, driver):
        self.driver = driver

    _logout_confirmation_message = (By.CLASS_NAME, "base")

    def get_logout_confirmation(self):
        return self.driver.find_element(*LogoutSuccessPage._logout_confirmation_message).text
