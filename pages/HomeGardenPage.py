from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class HomeGardenPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(HomeGardenPage, self).__init__(driver)

    def click_on_home_garden(self):
        self.find_element(*self.locator.home_garden_link).click()
