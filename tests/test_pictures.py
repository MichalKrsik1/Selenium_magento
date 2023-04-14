from utilities.base_class import Base
from page_objects.home_page import HomePage
from utilities.conftest import setup
from test_data.test_data_and_constants import tank_colors, hoodie_colors

EXPECTED_NUMBER_OF_PRODUCTS = 3


class TestPictures(Base):

    def check_color_pictures(self, product_type, color_list):
        log = self.get_logger()
        home = HomePage(self.driver)
        image_names = home.get_image_names_for_product(product_type)
        log.info(image_names)

        counter = 0
        for i in range(3):
            if color_list[i] in image_names[i]:
                counter += 1

        log.info(f"Final-{product_type}-counter: {counter}")
        assert counter == EXPECTED_NUMBER_OF_PRODUCTS

    def test_colour_pictures_tank(self, setup):
        self.check_color_pictures("tank_top", tank_colors)

    def test_colour_pictures_hoodie(self, setup):
        self.check_color_pictures("hoodie", hoodie_colors)
