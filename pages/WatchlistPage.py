from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class WatchlistPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(WatchlistPage, self).__init__(driver)

    def click_on_watchlist(self):
        self.find_element(*self.locator.watchlist_link).click()
