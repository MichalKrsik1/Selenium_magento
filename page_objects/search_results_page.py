from selenium.webdriver.common.by import By


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    search_message = (By.CLASS_NAME, "base")

    def get_search_message(self):
        return self.driver.find_element(*SearchResultsPage.search_message).text
