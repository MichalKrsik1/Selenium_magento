import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.shop_base_page import ShopBasePage
from page_objects.compare_products_page import CompareProductsPage
from page_objects.universal_product_page import UniversalProductPage


class WomenPage(ShopBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    compare_btn = (By.XPATH, "//a[@class='action compare primary']")
    shirt_breathe_easy = (By.LINK_TEXT, "Breathe-Easy Tank")

    def select_all_products(self):
        for i in range(1, 5):
            prod = self.driver.find_element(By.XPATH, "(//img[@class='product-image-photo'])" + "[" + str(i) + "]")
            a = ActionChains(self.driver)
            a.move_to_element(prod).perform()
            self.driver.find_element(By.XPATH, "(//a[@class='action tocompare'])" + "[" + str(i) + "]").click()

    def purchase_hot_sellers(self):
        for i in range(1, 5):
            self.driver.find_element(By.XPATH, "(//div[text()='XS' or text()='28'])" + "[" + str(i) + "]").click()
            self.driver.find_element(By.XPATH,
                                     "(//div[@class='swatch-option color'][@index='0'])" + "[" + str(i) + "]").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "(//button[@title='Add to Cart'])" + "[" + str(i) + "]").click()

    def open_compare_products(self):
        self.driver.find_element(*WomenPage.compare_btn).click()
        compare_page = CompareProductsPage(self.driver)

        return compare_page

    def open_shirt_breathe_easy(self):
        self.driver.find_element(*WomenPage.shirt_breathe_easy).click()
        universal_product_page = UniversalProductPage(self.driver)

        return universal_product_page
