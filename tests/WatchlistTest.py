from tests.BasePage import BasePage
from pages.WatchlistPage import WatchlistPage


class WatchlistTest(BasePage):
    def test_watchlist(self):
        obj_watchlist = WatchlistPage(self.driver)
        obj_watchlist.click_on_watchlist()
