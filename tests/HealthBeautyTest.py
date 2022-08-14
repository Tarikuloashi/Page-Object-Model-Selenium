from tests.BasePage import BasePage
from pages.HealthBeautyPage import HealthBeautyPage


class HealthBeautyTest(BasePage):
    def test_health_beauty(self):
        obj_health_beauty = HealthBeautyPage(self.driver)
        obj_health_beauty.click_on_health_beauty()
