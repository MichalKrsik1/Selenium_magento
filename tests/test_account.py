from utilities.base_class import Base
from utilities.conftest import setup
from page_objects.home_page import HomePage


class TestAccountSettings(Base):
    def test_subscribe(self, setup):
        log = self.get_logger()
        home = HomePage(self.driver)
        acc_page = home.open_account()
        msg = acc_page.subscribe()
        log.info(msg)
        assert msg == "We have saved your subscription."

    def test_change_name(self, setup):
        log = self.get_logger()
        home = HomePage(self.driver)
        acc_page = home.open_account()
        msg = acc_page.change_name()
        log.info(msg)
        assert msg == "You saved the account information."
