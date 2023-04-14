from selenium.webdriver.common.by import By


class CompareProductsPage:

    def __init__(self, driver):
        self.driver = driver

    _products = (By.CLASS_NAME, "info")

    def get_product_count(self):
        return len(self.driver.find_elements(*CompareProductsPage._products))
