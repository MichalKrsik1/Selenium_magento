from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.shop_base_page import ShopBasePage


class GearPage(ShopBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def purchase_hot_sellers(self):
        for i in range(2, 4):
            prod = self.driver.find_element(By.XPATH, "(//img[@class='product-image-photo'])" + "[" + str(i) + "]")
            actions = ActionChains(self.driver)
            actions.move_to_element(prod).perform()
            self.driver.find_element(By.XPATH, "(//button[@title='Add to Cart'])" + "[" + str(i) + "]").click()


