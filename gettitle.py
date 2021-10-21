from selenium import webdriver
#changes made


from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
import time
#changes made
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager


#driver=webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#s=Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=s)
#changes made
driver.get("https://www.saucedemo.com")
time.sleep(2)
driver.maximize_window()
uname=driver.find_element_by_id("user-name")
uname.send_keys("problem_user")

password=driver.find_element_by_id("password")
password.send_keys("secret_sauce")

driver.find_element_by_id("login-button").click()

time.sleep(5)
inventory_name_element = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[2]/div[1]")
inventory_name = inventory_name_element.text
print(inventory_name)
time.sleep(5)

#driver.find_element_by_xpath("//[@class='search-icon']").click()

#time.sleep(5)


