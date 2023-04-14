from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data.test_data_and_constants import TIME_UNTIL_LOADED


class ShopBasePage:

    def __init__(self, driver):
        self.driver = driver

    _women = (By.ID, "ui-id-4")
    _men = (By.ID, "ui-id-5")
    _gear = (By.ID, "ui-id-6")
    _cart = (By.CLASS_NAME, "showcart")
    _view_checkout_button = (By.XPATH, "//a[@class='action viewcart']")
    _success_message = (By.CLASS_NAME, "page-title")

    def open_women_section(self):
        self.driver.find_element(*ShopBasePage._women).click()

    def open_man_section(self):
        self.driver.find_element(*ShopBasePage._men).click()

    def open_gear_section(self):
        self.driver.find_element(*ShopBasePage._gear).click()

    def open_cart(self):
        WebDriverWait(self.driver, TIME_UNTIL_LOADED).until(
            EC.element_to_be_clickable(ShopBasePage._cart))
        self.driver.find_element(*ShopBasePage._cart).click()
        WebDriverWait(self.driver, TIME_UNTIL_LOADED).until(
            EC.element_to_be_clickable(ShopBasePage._view_checkout_button))
        self.driver.find_element(*ShopBasePage._view_checkout_button).click()

    def get_confirmation_message(self):
        WebDriverWait(self.driver, TIME_UNTIL_LOADED).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='action primary continue']")))

        return self.driver.find_element(*ShopBasePage._success_message).text
