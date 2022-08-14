from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class ElectronicsPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(ElectronicsPage, self).__init__(driver)

    def click_on_electronics(self):
        self.find_element(*self.locator.electronics_link).click()
