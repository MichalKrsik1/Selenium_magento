from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.shop_base_page import ShopBasePage
from test_data.test_data_and_constants import TIME_UNTIL_LOADED

PRODUCTS_TO_PURCHASE = range(1, 5)


class MenPage(ShopBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver

    def purchase_hot_sellers(self):
        for i in PRODUCTS_TO_PURCHASE:
            self._driver.find_element(By.XPATH, f"(//div[text()='XS' or text()='32'])[{i}]").click()
            self._driver.find_element(By.XPATH, f"(//div[@class='swatch-option color'][@index='0'])[{i}]").click()
            WebDriverWait(self._driver, TIME_UNTIL_LOADED).until(
                EC.element_to_be_clickable((By.XPATH, f"(//button[@title='Add to Cart'])[{i}]")))
            self._driver.find_element(By.XPATH, f"(//button[@title='Add to Cart'])[{i}]").click()
