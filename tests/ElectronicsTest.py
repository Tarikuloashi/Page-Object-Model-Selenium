from tests.BasePage import BasePage
from pages.ElectronicsPage import ElectronicsPage


class ElectronicsTest(BasePage):
    def test_electronics(self):
        obj_electronics = ElectronicsPage(self.driver)
        obj_electronics.click_on_electronics()
