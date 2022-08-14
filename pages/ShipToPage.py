from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class ShipToPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(ShipToPage, self).__init__(driver)

    def click_on_ship_to(self):
        self.find_element(*self.locator.ship_to_BTN).click()