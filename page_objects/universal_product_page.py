import time
from selenium.webdriver.common.by import By


class UniversalProductPage:

    def __init__(self, driver):
        self._driver = driver

    _ratting = (By.XPATH, "//input[@id='Rating_4']")
    _reviews_tab = (By.ID, "tab-label-reviews-title")
    _summary = (By.ID, "summary_field")
    _review = (By.ID, "review_field")
    _submit_btn = (By.CLASS_NAME, "submit")
    _success_msg = (By.XPATH, "//div[contains(text(),'submitted')]")

    def write_review(self):
        self._driver.find_element(*UniversalProductPage._reviews_tab).click()
        time.sleep(2)
        ratting = self._driver.find_element(*UniversalProductPage._ratting)
        self._driver.execute_script("arguments[0].click();", ratting)
        self._driver.find_element(*UniversalProductPage._summary).send_keys("Summary of my review")
        self._driver.find_element(*UniversalProductPage._review).send_keys("Fine white shirt")
        self._driver.find_element(*UniversalProductPage._submit_btn).click()
        return self._driver.find_element(*UniversalProductPage._success_msg).text
