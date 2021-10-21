import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class ChromeTest:
    def test(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
      # driverlocation = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        # os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",options=chrome_options)

        url = "http://www.saucedemo.com"
        driver.get(url)
        print(driver.title)
        #username_id = "user-name"
        # user_element = driver.find_element_by_id(username_id)
        # print("Username found")


t = ChromeTest()
t.test()
