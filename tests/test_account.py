from utilities.base_class import Base
from utilities.conftest import setup
from page_objects.home_page import HomePage


class TestAccount(Base):
    def test_subscribe(self, setup):
        log = self.get_logger()
        home = HomePage(self.driver)
        account_page = home.open_account_page()
        message = account_page.subscribe()
        log.info(f"Subscription message: {message}")
        assert message == "We have saved your subscription."

    def test_change_name(self, setup):
        log = self.get_logger()
        home = HomePage(self.driver)
        account_page = home.open_account_page()
        message = account_page.change_name()
        log.info(f"Account information update message: {message}")
        assert message == "You saved the account information."
