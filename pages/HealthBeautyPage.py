from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class HealthBeautyPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(HealthBeautyPage, self).__init__(driver)

    def click_on_health_beauty(self):
        self.find_element(*self.locator.health_beauty_link).click()
