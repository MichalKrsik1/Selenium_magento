from selenium.webdriver.common.by import By


class CompareProductsPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.CLASS_NAME, "info")

    def get_product_count(self):
        prods = self.driver.find_elements(*CompareProductsPage.products)

        return len(prods)


