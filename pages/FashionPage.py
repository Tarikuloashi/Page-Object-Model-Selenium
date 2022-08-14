from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class FashionPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(FashionPage, self).__init__(driver)

    def click_on_fashion(self):
        self.find_element(*self.locator.fashion_link).click()
