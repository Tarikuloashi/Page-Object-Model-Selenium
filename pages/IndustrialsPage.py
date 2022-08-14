from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class IndustrialsPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(IndustrialsPage, self).__init__(driver)

    def click_on_industrials(self):
        self.find_element(*self.locator.industrials_link).click()
