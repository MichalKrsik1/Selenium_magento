import time

from selenium.webdriver.common.by import By
from page_objects.account_info_page import AccountInfoPage


class PostLogin:

    def __init__(self, driver):
        self.driver = driver

    _open_menu = (By.CLASS_NAME, "switch")
    _account = (By.LINK_TEXT, "My Account")
    _sign_out = (By.LINK_TEXT, "Sign Out")

    def open_account_page(self):
        self.driver.find_element(*PostLogin._open_menu).click()
        self.driver.find_element(*PostLogin._account).click()
        acc_page = AccountInfoPage(self.driver)

        return acc_page

    def logout(self):
        time.sleep(2)
        self.driver.find_element(*PostLogin._open_menu).click()
        logout_page = self.driver.find_element(*PostLogin._sign_out).click()

        return logout_page
