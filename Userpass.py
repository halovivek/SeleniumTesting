
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
s = Service("C:\Drivers\chromedriver.exe")

browser = webdriver.Chrome(service = s)
browser.get("https://trade.fyers.in/")
browser.maximize_window()
#browser.get("https://www.amazon.in")
time.sleep(5)
cookies = browser.get_cookies()
print(len(cookies))
print(cookies)
time.sleep(5)

browser.quit()
