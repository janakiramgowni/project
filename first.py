from selenium import webdriver
import time
# initial
driver = webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver")
driver.get("https://www.facebook.com/")
time.sleep(3)
driver.close()
