from tests.BasePage import BasePage
from pages.HomeContactPage import HomeContactPage


class HomeContactTest(BasePage):
    def test_home_contact(self):
        obj_home_contact = HomeContactPage(self.driver)
        obj_home_contact.click_on_home_contact()
