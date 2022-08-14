from tests.BasePage import BasePage
from pages.IndustrialsPage import IndustrialsPage


class CollectiblesAndArtTest(BasePage):
    def test_industrials(self):
        obj_industrials = IndustrialsPage(self.driver)
        obj_industrials.click_on_industrials()
