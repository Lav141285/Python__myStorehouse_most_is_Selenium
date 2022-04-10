from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

PATH = "E:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
# Go to the correct domain
driver.get("https://www.messenger.com/")
time.sleep(1)
search = driver.find_element_by_xpath('//*[@id="email"]')
search.send_keys('tieple1782002@gmail.com')

search = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
search.send_keys('4h50pomny')
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(10)
