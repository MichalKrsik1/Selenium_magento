import time
from selenium.webdriver.common.by import By
from page_objects.registration_page import RegistrationPage
from page_objects.post_login_home_page import PostLogin
from page_objects.shop_base_page import ShopBasePage
from page_objects.search_results_page import SearchResultsPage


class HomePage(PostLogin, ShopBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    register = (By.LINK_TEXT, "Create an Account")
    title = (By.XPATH, "//strong[@class='title']")
    prod_names = (By.CLASS_NAME, "product-item-link")
    search_bar = (By.ID, "search")
    search_options = (By.XPATH, "//ul[@role='listbox']/li/span[2]")
    breathe_easy_tank_picture = (By.XPATH, "//img[@alt='Breathe-Easy Tank']")
    tank_buttons = [(By.XPATH, "(//div[@id='option-label-color-93-item-57'])[2]"),
                    (By.ID, "option-label-color-93-item-59"),
                    (By.ID, "option-label-color-93-item-60")]
    hero_hoodie_picture = (By.XPATH, "//img[@alt='Hero Hoodie']")
    hoodie_buttons = [(By.ID, "option-label-color-93-item-49"),
                      (By.XPATH, "(//div[@id='option-label-color-93-item-52'])[2]"),
                      (By.ID, "option-label-color-93-item-53")]

    def open_registration(self):
        self.driver.find_element(*HomePage.register).click()
        reg_page = RegistrationPage(self.driver)
        return reg_page

    def get_title(self):
        return self.driver.find_element(*HomePage.title).text

    def get_hot_products(self):
        product_list_names = []

        products = self.driver.find_elements(*HomePage.prod_names)

        for prod in products:
            product_list_names.append(prod.text)

        return product_list_names

    def search_product(self, name="pants"):
        max_val = 0
        self.driver.find_element(*HomePage.search_bar).clear()
        self.driver.find_element(*HomePage.search_bar).send_keys(name)
        products = self.driver.find_elements(*HomePage.search_options)

        for prod in products:
            max_val = max(max_val, int(prod.text))

        for prod in products:
            if int(prod.text) == max_val:
                prod.click()
                break

        search_result_page = SearchResultsPage(self.driver)

        return search_result_page

    def get_image_names_for_tank(self):
        image_names_list = []

        for button in HomePage.tank_buttons:
            self.driver.find_element(*button).click()
            time.sleep(2)
            image_names_list.append(self.driver.find_element(*HomePage.breathe_easy_tank_picture).get_attribute("src"))

        return image_names_list

    def get_image_names_for_hoodie(self):
        image_names_list = []

        for button in HomePage.hoodie_buttons:
            self.driver.find_element(*button).click()
            time.sleep(2)
            image_names_list.append(self.driver.find_element(*HomePage.hero_hoodie_picture).get_attribute("src"))

        return image_names_list
