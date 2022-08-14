from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class HomeContactPage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(HomeContactPage, self).__init__(driver)

    def click_on_home_contact(self):
        self.find_element(*self.locator.home_contact_id).click()