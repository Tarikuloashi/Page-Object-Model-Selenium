from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class SportsPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(SportsPage, self).__init__(driver)

    def click_on_sports(self):
        self.find_element(*self.locator.sports_link).click()
