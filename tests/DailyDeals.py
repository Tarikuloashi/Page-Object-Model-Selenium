from tests.BasePage import BasePage
from pages.DailyDealsPage import DailyDealsPage


class DailyDeals(BasePage):
    def test_daily_deals(self):
        obj_daily_deals = DailyDealsPage(self.driver)
        obj_daily_deals.click_on_daily_deals()
        # obj_daily_deals.back()
        # obj_daily_deals.click_on_ship_to()
