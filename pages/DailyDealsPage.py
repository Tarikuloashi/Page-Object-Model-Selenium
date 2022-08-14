from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class DailyDealsPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(DailyDealsPage, self).__init__(driver)

    def click_on_daily_deals(self):
        self.find_element(*self.locator.daily_deals_id).click()

    # def click_on_ship_to(self):
    #     self.find_element(*self.locator.ship_to_BTN).click()
    #
    # def back(self):
    #     self.driver.back()
