import time
from utilities.base_class import Base
from page_objects.home_page import HomePage
from page_objects.women_page import WomenPage
from page_objects.men_page import MenPage
from page_objects.gear_page import GearPage
from page_objects.cart_page import CartPage
from utilities.conftest import setup
from test_data.random_data import success_order_message


class TestPictures(Base):

    def test_big_shopping(self, setup):
        log = self.get_logger()
        home = HomePage(self.driver)

        # Step1:  Get all products into cart
        home.open_women_section()
        women = WomenPage(self.driver)
        women.purchase_hot_sellers()
        women.open_man_section()
        men = MenPage(self.driver)
        men.purchase_hot_sellers()
        men.open_gear_section()
        gear = GearPage(self.driver)
        gear.purchase_hot_sellers()
        time.sleep(3)

        # Step2: Remove one from each category in cart
        women.open_cart()
        cart = CartPage(self.driver)
        cart.remove_prods()
        time.sleep(3)

        # Step3: Checkout process and purchase
        checkout_shipping = cart.open_checkout_shipping()
        checkout_review = checkout_shipping.click_next()
        checkout_review.place_order()
        message = checkout_review.get_confirmation_message()
        log.info(message)

        assert message == success_order_message
