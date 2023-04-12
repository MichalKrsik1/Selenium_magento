from utilities.base_class import Base
from page_objects.home_page import HomePage
from utilities.conftest import setup_nolog


class TestRegistration(Base):

    def test_registration(self, setup_nolog):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        reg_page = home_page.open_registration()
        account_profile_page = reg_page.register()
        message = account_profile_page.get_reg_message()
        log.info(f"Reg. message -> {message}")

        assert message == "Thank you for registering with Main Website Store."
