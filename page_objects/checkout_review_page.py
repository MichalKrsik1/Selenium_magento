from selenium.webdriver.common.by import By
from page_objects.shop_base_page import ShopBasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIME_UNTIL_LOADED = 20


class CheckoutReviewPage(ShopBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    button_place_order = (By.XPATH, "//button[@class='action primary checkout']")

    def place_order(self):
        WebDriverWait(self.driver, TIME_UNTIL_LOADED).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='action primary checkout']")))

        button = self.driver.find_element(*CheckoutReviewPage.button_place_order)
        self.driver.execute_script("arguments[0].click();", button)
