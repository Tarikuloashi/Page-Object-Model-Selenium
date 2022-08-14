from Locators.Locators import HomeLocator
from pages.HomePage import HomePage


class MoneyBackGuaranteePage(HomePage):
    def __init__(self, driver):
        self.locator = HomeLocator
        self.driver = driver
        super(MoneyBackGuaranteePage, self).__init__(driver)

    def down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def click_on_money_back_guarantee(self):
        self.find_element(*self.locator.money_back_link).click()

