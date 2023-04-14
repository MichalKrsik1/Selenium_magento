from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.checkout_review_page import CheckoutReviewPage
from test_data.test_data_and_constants import TIME_UNTIL_LOADED


class CheckoutShippingPage:

    def __init__(self, driver):
        self.driver = driver

    _continue_btn = (By.XPATH, "//button[@class='button action continue primary']")

    def open_checkout_review_page(self):
        WebDriverWait(self.driver, TIME_UNTIL_LOADED).until(
            EC.element_to_be_clickable(CheckoutShippingPage._continue_btn))

        button = self.driver.find_element(*CheckoutShippingPage._continue_btn)
        self.driver.execute_script("arguments[0].click();", button)
        checkout_review_page = CheckoutReviewPage(self.driver)

        return checkout_review_page
