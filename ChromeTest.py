import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class ChromeTest:
    def test(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
      # driverlocation = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        # os.environ["webdriver.chrome.driver"] = driverlocation
        #driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",options=chrome_options)
        driver = webdriver.Chrome("/usr/bin/chromedriver",options=chrome_options)
        url = "http://www.saucedemo.com"
        driver.get(url)
        time.sleep(6)
        print(driver.title)
        #username_id = "user-name"
        # user_element = driver.find_element_by_id(username_id)
        # print("Username found")


t = ChromeTest()
t.test()
