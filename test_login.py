import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import Config
from utils.exceptions import LoginException

class TestLogin:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get(Config.URL)
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_login_valid(self, setup):
        login_page = LoginPage(self.driver)
        login_page.enter_username(Config.USERNAME)
        login_page.enter_password(Config.PASSWORD)
        login_page.click_login()
        
        # Add a check to verify login, e.g., by checking for a certain element
        try:
            assert "dashboard" in self.driver.current_url
        except AssertionError:
            raise LoginException("Login failed with valid credentials")

