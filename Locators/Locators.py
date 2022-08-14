from selenium.webdriver.common.by import By


class HomeLocator(object):
    daily_deals_id = (By.ID, "gh-p-1")
    home_contact_id = (By.ID, "gh-p-3")
    ship_to_BTN = [By.XPATH, "//*[@id='gh-shipto-click']/div/button/span"]
    money_back_link = (By.XPATH, "//*[@id='gf-BIG']/table/tbody/tr/td[1]/ul/li[2]/a")
    sell_link = (By.XPATH, "//*[@id='gh-p-2']/a")
    watchlist_link = (By.XPATH, "//*[@id='gh-wl-click']/div/a[1]")
    electronics_link = (By.XPATH, "//*[@id='mainContent']/div[1]/ul/li[3]")
    fashion_link = (By.XPATH, "//*[@id='mainContent']/div[1]/ul/li[4]")
    health_beauty_link = (By.XPATH, "//*[@id='mainContent']/div[1]/ul/li[5]/a")
    home_garden_link = (By.XPATH, "//*[@id='mainContent']/div[1]/ul/li[6]/a")
    sports_link = (By.XPATH, "//*[@id='mainContent']/div[1]/ul/li[7]/a")
    collectibles_and_art = (By.XPATH, "//*[@id='mainContent']/div[1]/ul/li[8]/a")
    industrials_link = (By.XPATH, "//*[@id='mainContent']/div[1]/ul/li[9]/a")
