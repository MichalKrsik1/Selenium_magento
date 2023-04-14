from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.shop_base_page import ShopBasePage
from page_objects.compare_products_page import CompareProductsPage
from page_objects.universal_product_page import UniversalProductPage
from test_data.test_data_and_constants import TIME_UNTIL_LOADED

PRODUCTS_TO_PURCHASE = range(1, 5)


class WomenPage(ShopBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _compare_btn = (By.XPATH, "//a[@class='action compare primary']")
    _shirt_breathe_easy = (By.LINK_TEXT, "Breathe-Easy Tank")

    def select_all_products(self):
        for i in range(1, 5):
            prod = self.driver.find_element(By.XPATH, f"(//img[@class='product-image-photo'])[{i}]")
            a = ActionChains(self.driver)
            a.move_to_element(prod).perform()
            self.driver.find_element(By.XPATH, f"(//a[@class='action tocompare'])[{i}]").click()

    def purchase_hot_sellers(self):
        for i in PRODUCTS_TO_PURCHASE:
            self.driver.find_element(By.XPATH, f"(//div[text()='XS' or text()='28'])[{i}]").click()
            self.driver.find_element(By.XPATH, f"(//div[@class='swatch-option color'][@index='0'])[{i}]").click()

            add_to_cart_button = WebDriverWait(self.driver, TIME_UNTIL_LOADED).until(
                EC.element_to_be_clickable((By.XPATH, f"(//button[@title='Add to Cart'])[{i}]")))
            add_to_cart_button.click()

    def open_compare_products(self):
        self.driver.find_element(*WomenPage._compare_btn).click()
        compare_page = CompareProductsPage(self.driver)

        return compare_page

    def open_shirt_breathe_easy(self):
        self.driver.find_element(*WomenPage._shirt_breathe_easy).click()
        universal_product_page = UniversalProductPage(self.driver)

        return universal_product_page
