import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage(unittest.TestCase):
    @classmethod
    def setUp(cls):
        serv_obj = Service("/home/oashi/PycharmProjects/ebayAutomationProject/drivers/chromedriver")
        cls.driver = webdriver.Chrome(service=serv_obj)
        cls.driver.get("https://www.ebay.com/")
        cls.driver.implicitly_wait('10')
        cls.driver.maximize_window()
        print("Test Started")

    @classmethod
    def tearDown(cls):
        time.sleep(5)
        print(cls.driver.title)
        print(cls.driver.current_url)
        cls.driver.quit()
        print("Test Complete")
