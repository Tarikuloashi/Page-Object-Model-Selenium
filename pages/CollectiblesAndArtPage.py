from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class CollectiblesAndArtPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(CollectiblesAndArtPage, self).__init__(driver)

    def click_on_collectivles_and_art(self):
        self.find_element(*self.locator.collectibles_and_art).click()
