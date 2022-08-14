from tests.BasePage import BasePage
from pages.HomeGardenPage import HomeGardenPage


class HealthBeautyTest(BasePage):
    def test_home_garden(self):
        obj_home_garden = HomeGardenPage(self.driver)
        obj_home_garden.click_on_home_garden()
