from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from page_objects.registration_page import RegistrationPage
from page_objects.post_login_page import PostLogin
from page_objects.shop_base_page import ShopBasePage
from page_objects.search_results_page import SearchResultsPage
from test_data.test_data_and_constants import TIME_UNTIL_LOADED


class HomePage(PostLogin, ShopBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _register = (By.LINK_TEXT, "Create an Account")
    _title = (By.XPATH, "//strong[@class='title']")
    _prod_names = (By.CLASS_NAME, "product-item-link")
    _search_bar = (By.ID, "search")
    _search_options = (By.XPATH, "//ul[@role='listbox']/li/span[2]")
    _breathe_easy_tank_picture = (By.XPATH, "//img[@alt='Breathe-Easy Tank']")
    _tank_buttons = [(By.XPATH, "(//div[@id='option-label-color-93-item-57'])[2]"),
                     (By.ID, "option-label-color-93-item-59"),
                     (By.ID, "option-label-color-93-item-60")]
    _hero_hoodie_picture = (By.XPATH, "//img[@alt='Hero Hoodie']")
    _hoodie_buttons = [(By.ID, "option-label-color-93-item-49"),
                       (By.XPATH, "(//div[@id='option-label-color-93-item-52'])[2]"),
                       (By.ID, "option-label-color-93-item-53")]

    def open_registration(self):
        self.driver.find_element(*HomePage._register).click()
        return RegistrationPage(self.driver)

    def get_title(self):
        try:
            return self.driver.find_element(*HomePage._title).text
        except NoSuchElementException:
            return ""

    def get_hot_products(self):
        product_list_names = []

        products = self.driver.find_elements(*HomePage._prod_names)

        for prod in products:
            product_list_names.append(prod.text)

        return product_list_names

    def search_product(self, name="pants"):
        max_val = 0
        self.driver.find_element(*HomePage._search_bar).clear()
        self.driver.find_element(*HomePage._search_bar).send_keys(name)
        products = self.driver.find_elements(*HomePage._search_options)

        for prod in products:
            max_val = max(max_val, int(prod.text))

        for prod in products:
            if int(prod.text) == max_val:
                prod.click()
                break

        return SearchResultsPage(self.driver)

    def get_image_names_for_product(self, product):
        image_names_list = []

        product_mapping = {
            'tank_top': {
                'buttons': HomePage._tank_buttons,
                'picture': HomePage._breathe_easy_tank_picture
            },
            'hoodie': {
                'buttons': HomePage._hoodie_buttons,
                'picture': HomePage._hero_hoodie_picture
            }
        }

        if product not in product_mapping:
            return []

        buttons = product_mapping[product]['buttons']
        picture = product_mapping[product]['picture']

        for button in buttons:
            current_image_src = self.driver.find_element(*picture).get_attribute("src")
            self.driver.find_element(*button).click()

            def image_src_changed(driver):
                new_image_src = driver.find_element(*picture).get_attribute("src")
                return new_image_src != current_image_src

            WebDriverWait(self.driver, TIME_UNTIL_LOADED).until(image_src_changed)
            image_names_list.append(self.driver.find_element(*picture).get_attribute("src"))

        return image_names_list
