import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.log_page import LoginPage
from page_objects.post_login_home_page import PostLogin


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://magento.softwaretestingboard.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver

    login = (By.LINK_TEXT, "Sign In")

    driver.find_element(*login).click()
    log_page = LoginPage(driver)
    log_page.login()
    yield
    post_login_page = PostLogin(driver)
    post_login_page.logout()
    time.sleep(2)
    driver.close()


@pytest.fixture(scope="class")
def setup_nolog(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://magento.softwaretestingboard.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()
