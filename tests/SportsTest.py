from tests.BasePage import BasePage
from pages.SportsPage import SportsPage


class SportsTest(BasePage):
    def test_sports(self):
        obj_sports = SportsPage(self.driver)
        obj_sports.click_on_sports()
