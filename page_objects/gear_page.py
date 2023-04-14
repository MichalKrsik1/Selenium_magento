from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.shop_base_page import ShopBasePage

RANGE_OF_PRODUCTS_TO_PURCHASE = range(2, 4)


class GearPage(ShopBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def purchase_hot_sellers(self):
        for i in RANGE_OF_PRODUCTS_TO_PURCHASE:
            prod = self.driver.find_element(By.XPATH, f"(//img[@class='product-image-photo'])[{i}]")
            actions = ActionChains(self.driver)
            actions.move_to_element(prod).perform()

            add_to_cart_button = self.driver.find_element(By.XPATH, f"(//button[@title='Add to Cart'])[{i}]")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"(//button[@title='Add to Cart'])[{i}]"))
            )
            add_to_cart_button.click()
