from tests.BasePage import BasePage
from pages.FashionPage import FashionPage


class FashionTest(BasePage):
    def test_fashion(self):
        obj_fashion = FashionPage(self.driver)
        obj_fashion.click_on_fashion()
