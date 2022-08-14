from tests.BasePage import BasePage
from pages.MoneyBackGuaranteePage import MoneyBackGuaranteePage


class MoneyBackGuaranteeTest(BasePage):
    def test_money_back_guarantee(self):
        obj_money_back_guarantee = MoneyBackGuaranteePage(self.driver)
        obj_money_back_guarantee.down()
        obj_money_back_guarantee.click_on_money_back_guarantee()

