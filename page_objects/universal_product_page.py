import time
from selenium.webdriver.common.by import By


class UniversalProductPage:

    def __init__(self, driver):
        self.driver = driver

    ratting = (By.XPATH, "//input[@id='Rating_4']")
    reviews_tab = (By.ID, "tab-label-reviews-title")
    summary = (By.ID, "summary_field")
    review = (By.ID, "review_field")
    submit_btn = (By.CLASS_NAME, "submit")
    success_msg = (By.XPATH, "//div[contains(text(),'submitted')]")

    def write_review(self):
        self.driver.find_element(*UniversalProductPage.reviews_tab).click()
        time.sleep(2)
        ratting = self.driver.find_element(*UniversalProductPage.ratting)
        self.driver.execute_script("arguments[0].click();", ratting)
        self.driver.find_element(*UniversalProductPage.summary).send_keys("Summary of my review")
        time.sleep(2)
        self.driver.find_element(*UniversalProductPage.review).send_keys("Fine white shirt")
        time.sleep(2)
        self.driver.find_element(*UniversalProductPage.submit_btn).click()
        time.sleep(2)
        return self.driver.find_element(*UniversalProductPage.success_msg).text

