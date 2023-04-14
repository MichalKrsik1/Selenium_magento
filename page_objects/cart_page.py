import time
from selenium.webdriver.common.by import By
from page_objects.checkout_shipping_page import CheckoutShippingPage

INDEXES_OF_PRODUCTS_TO_BE_REMOVED = [9, 5, 1]


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    _proceed_checkout_btn = (By.XPATH, "//button[@data-role='proceed-to-checkout']")

    def remove_prods(self):
        for x in INDEXES_OF_PRODUCTS_TO_BE_REMOVED:
            self.driver.find_element(By.XPATH, f"(//a[@class='action action-delete'])[{x}]").click()
            time.sleep(1)

    def open_checkout_shipping_page(self):
        self.driver.find_element(*CartPage._proceed_checkout_btn).click()
        checkout_shipping_page = CheckoutShippingPage(self.driver)
        return checkout_shipping_page
