from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class SellPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(SellPage, self).__init__(driver)

    def click_on_sell(self):
        self.find_element(*self.locator.sell_link).click()
