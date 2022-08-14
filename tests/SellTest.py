from tests.BasePage import BasePage
from pages.SellPage import SellPage


class SellTest(BasePage):
    def test_sell(self):
        obj_sell = SellPage(self.driver)
        obj_sell.click_on_sell()
