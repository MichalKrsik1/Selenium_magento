import time
from selenium.webdriver.common.by import By
from page_objects.shop_base_page import ShopBasePage


class MenPage(ShopBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def purchase_hot_sellers(self):
        for i in range(1, 5):
            self.driver.find_element(By.XPATH, "(//div[text()='XS' or text()='32'])" + "[" + str(i) + "]").click()
            self.driver.find_element(By.XPATH,
                                     "(//div[@class='swatch-option color'][@index='0'])" + "[" + str(i) + "]").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "(//button[@title='Add to Cart'])" + "[" + str(i) + "]").click()
