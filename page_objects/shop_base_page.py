import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIME_UNTIL_LOADED = 20


class ShopBasePage:

    def __init__(self, driver):
        self.driver = driver

    women = (By.ID, "ui-id-4")
    men = (By.ID, "ui-id-5")
    gear = (By.ID, "ui-id-6")
    cart = (By.CLASS_NAME, "showcart")
    view_checkout_button = (By.XPATH, "//a[@class='action viewcart']")
    success_message = (By.CLASS_NAME, "page-title")

    def open_women_section(self):
        self.driver.find_element(*ShopBasePage.women).click()

    def open_man_section(self):
        self.driver.find_element(*ShopBasePage.men).click()

    def open_gear_section(self):
        self.driver.find_element(*ShopBasePage.gear).click()

    def open_cart(self):
        time.sleep(2)
        self.driver.find_element(*ShopBasePage.cart).click()
        time.sleep(1)
        self.driver.find_element(*ShopBasePage.view_checkout_button).click()

    def get_confirmation_message(self):
        WebDriverWait(self.driver, TIME_UNTIL_LOADED).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='action primary continue']")))

        return self.driver.find_element(*ShopBasePage.success_message).text
