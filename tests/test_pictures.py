from utilities.base_class import Base
from page_objects.home_page import HomePage
from utilities.conftest import setup
from test_data.random_data import tank_colors, hoodie_colors

EXPECTED_NUMBER_OF_PRODUCTS = 3


class TestPictures(Base):

    def test_colour_pictures_tank(self, setup):
        log = self.get_logger()
        home = HomePage(self.driver)
        image_names = home.get_image_names_for_tank()

        counter = 0
        for i in range(3):
            if tank_colors[i] in image_names[i]:
                counter += 1

        log.info(f"Final-tank-counter: {counter}")
        assert counter == EXPECTED_NUMBER_OF_PRODUCTS

    def test_colour_pictures_hoodie(self, setup):
        log = self.get_logger()
        home = HomePage(self.driver)
        image_names = home.get_image_names_for_hoodie()

        counter = 0
        for i in range(3):
            if hoodie_colors[i] in image_names[i]:
                counter += 1

        log.info(f"Final-hoodie-counter: {counter}")
        assert counter == EXPECTED_NUMBER_OF_PRODUCTS
