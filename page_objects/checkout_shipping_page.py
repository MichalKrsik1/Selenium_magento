from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.checkout_review_page import CheckoutReviewPage

TIME_UNTIL_LOADED = 20


class CheckoutShippingPage:

    def __init__(self, driver):
        self.driver = driver

    """
    first_name = (By.ID, "IKK7AVX")
    last_name = (By.ID, "JBJEEQP")
    street_address = (By.ID, "XM900LH")
    city = (By.ID, "Y246W2I")
    country = (By.ID, "FU0VT9T")  # value: "CZ"
    zip_code = (By.ID, "YETKO27")
    phone_number = (By.ID, "PJOVVAF")
    """
    continue_btn = (By.XPATH, "//button[@class='button action continue primary']")

    def click_next(self):
        WebDriverWait(self.driver, TIME_UNTIL_LOADED).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='button action continue primary']")))

        button = self.driver.find_element(*CheckoutShippingPage.continue_btn)
        self.driver.execute_script("arguments[0].click();", button)
        checkout_review_page = CheckoutReviewPage(self.driver)

        return checkout_review_page
