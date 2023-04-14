from selenium.webdriver.common.by import By

NOT_SUBSCRIBED = "You aren't subscribed to our newsletter."
ALREADY_SUBSCRIBED = "Already subscribed"


class AccountInfoPage:
    def __init__(self, driver):
        self.driver = driver

    _success_message = (By.XPATH, "//div[@data-ui-id='message-success']/div")
    _sub_message = (By.XPATH, "//p[not(@*)]")
    _btn_edit = (By.XPATH, "//span[text()='Edit']")
    _checkbox = (By.ID, "subscription")
    _btn_save = (By.XPATH, "//span[text()='Save']")
    _first_name = (By.ID, "firstname")

    def get_reg_message(self):
        return self.driver.find_element(*AccountInfoPage._success_message).text

    def subscribe(self):
        if self.driver.find_elements(*AccountInfoPage._sub_message)[1].text == NOT_SUBSCRIBED:
            self.driver.find_elements(*AccountInfoPage._btn_edit)[1].click()
            self.driver.find_element(*AccountInfoPage._checkbox).click()
            self.driver.find_element(*AccountInfoPage._btn_save).click()

            message = self.driver.find_element(*AccountInfoPage._success_message).text
            return message
        else:
            return ALREADY_SUBSCRIBED

    def change_name(self):
        self.driver.find_element(*AccountInfoPage._btn_edit).click()
        new_name = self.driver.find_element(*AccountInfoPage._first_name).get_attribute("value") + "X"
        self.driver.find_element(*AccountInfoPage._first_name).clear()
        self.driver.find_element(*AccountInfoPage._first_name).send_keys(new_name)
        self.driver.find_element(*AccountInfoPage._btn_save).click()
        message = self.driver.find_element(*AccountInfoPage._success_message).text
        return message
