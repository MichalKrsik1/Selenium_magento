from selenium.webdriver.common.by import By
from page_objects.account_info_page import AccountInfoPage


class PostLogin:

    def __init__(self, driver):
        self.driver = driver

    open_menu = (By.CLASS_NAME, "switch")
    account = (By.LINK_TEXT, "My Account")
    sign_out = (By.LINK_TEXT, "Sign Out")

    def open_account(self):
        self.driver.find_element(*PostLogin.open_menu).click()
        self.driver.find_element(*PostLogin.account).click()
        acc_page = AccountInfoPage(self.driver)

        return acc_page

    def logout(self):
        self.driver.find_element(*PostLogin.open_menu).click()
        logout_page = self.driver.find_element(*PostLogin.sign_out).click()

        return logout_page
