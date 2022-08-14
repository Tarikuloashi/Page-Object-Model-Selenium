from tests.BasePage import BasePage
from pages.ShipToPage import ShipToPage


class ShipToTest(BasePage):
    def test_ship_to(self):
        obj_ship_to = ShipToPage(self.driver)
        obj_ship_to.click_on_ship_to()
