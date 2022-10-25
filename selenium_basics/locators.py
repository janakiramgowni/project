from selenium import webdriver
import time
driver=webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver")
driver.get("https://www.facebook.com/")
time.sleep(5)
driver.close()
