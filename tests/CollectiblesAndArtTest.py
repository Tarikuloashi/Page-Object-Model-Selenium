from tests.BasePage import BasePage
from pages.CollectiblesAndArtPage import CollectiblesAndArtPage


class CollectiblesAndArtTest(BasePage):
    def test_collectivles(self):
        obj_collectivles = CollectiblesAndArtPage(self.driver)
        obj_collectivles.click_on_collectivles_and_art()
