import time
from selenium.webdriver.common.by import By


class AccountInfoPage:

    def __init__(self, driver):
        self.driver = driver

    NOT_SUBSCRIBED = "You aren't subscribed to our newsletter."
    ALREADY_SUBSCRIBED = "Already subscribed"

    success_message = (By.XPATH, "//div[@data-ui-id='message-success']/div")
    sub_message = (By.XPATH, "//p[not(@*)]")
    btn_edit = (By.XPATH, "//span[text()='Edit']")
    checkbox = (By.ID, "subscription")
    btn_save = (By.XPATH, "//span[text()='Save']")
    first_name = (By.ID, "firstname")

    def get_reg_message(self):
        return self.driver.find_element(*AccountInfoPage.success_message).text

    def subscribe(self):
        if self.driver.find_elements(*AccountInfoPage.sub_message)[1].text == \
                AccountInfoPage.NOT_SUBSCRIBED:
            self.driver.find_elements(*AccountInfoPage.btn_edit)[1].click()
            self.driver.find_element(*AccountInfoPage.checkbox).click()
            self.driver.find_element(*AccountInfoPage.btn_save).click()

            message = self.driver.find_element(*AccountInfoPage.success_message).text
            return message
        else:
            return AccountInfoPage.ALREADY_SUBSCRIBED

    def change_name(self):
        self.driver.find_element(*AccountInfoPage.btn_edit).click()
        new_name = self.driver.find_element(*AccountInfoPage.first_name).get_attribute("value") + "X"
        time.sleep(2)
        self.driver.find_element(*AccountInfoPage.first_name).clear()
        time.sleep(2)
        self.driver.find_element(*AccountInfoPage.first_name).send_keys(new_name)
        time.sleep(2)
        self.driver.find_element(*AccountInfoPage.btn_save).click()
        message = self.driver.find_element(*AccountInfoPage.success_message).text
        return message
