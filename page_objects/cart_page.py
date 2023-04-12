import time
from selenium.webdriver.common.by import By
from page_objects.checkout_shipping_page import CheckoutShippingPage


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    proceed_checkout_btn = (By.XPATH, "//button[@data-role='proceed-to-checkout']")

    def remove_prods(self):
        """ Remove first product from each category (Women, Men, Gear) """
        for x in [9, 5, 1]:
            self.driver.find_element(By.XPATH, "(//a[@class='action action-delete'])" + "[" + str(x) + "]").click()
            time.sleep(1)

    def open_checkout_shipping(self):
        self.driver.find_element(*CartPage.proceed_checkout_btn).click()
        checkout_shipping_page = CheckoutShippingPage(self.driver)

        return checkout_shipping_page
