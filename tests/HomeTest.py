from tests.BasePage import BasePage
from pages.HomePage import HomePage


class HomeTest(BasePage):
    def test_home_page(self):
        login = HomePage(self.driver)
        print("Test Home")
