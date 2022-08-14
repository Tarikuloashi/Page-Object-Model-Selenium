from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Driver:
serv_obj = Service("/home/oashi/PycharmProjects/ebayAutomationProject/drivers/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.ebay.com/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.find_element(By.ID, "gh-p-1").click()
print(driver.title)
