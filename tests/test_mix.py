from utilities.base_class import Base
from page_objects.home_page import HomePage
from utilities.conftest import setup
from test_data.test_data_and_constants import expected_product_list, search_result_message, review_success_msg
from page_objects.women_page import WomenPage

EXPECTED_NUMBER_OF_PRODUCTS = 4


class TestMix(Base):

    def test_hot_sellers(self, setup):
        log = self.get_logger()
        home = HomePage(self.driver)
        prod_list = home.get_hot_products()
        log.info(f"Product list: {prod_list}")
        assert prod_list == expected_product_list

    def test_open_account(self, setup):
        home = HomePage(self.driver)
        home.open_account_page()

    def test_open_women(self, setup):
        home = HomePage(self.driver)
        home.open_women_section()

    def test_search(self, setup):
        home = HomePage(self.driver)
        search_page = home.search_product("pants")
        msg = search_page.get_search_message()
        assert msg == search_result_message

    def test_compare_products(self, setup):
        log = self.get_logger()
        home = HomePage(self.driver)
        home.open_women_section()
        women = WomenPage(self.driver)
        women.select_all_products()
        compare_page = women.open_compare_products()
        size = compare_page.get_product_count()
        log.info(f"Number of products: {size}")
        assert size == EXPECTED_NUMBER_OF_PRODUCTS

    def test_write_review(self, setup):
        home = HomePage(self.driver)
        home.open_women_section()
        women = WomenPage(self.driver)
        product = women.open_shirt_breathe_easy()
        msg = product.write_review()
        assert msg == review_success_msg
