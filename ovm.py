from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service("C:\Drivers\chromedriver.exe")

driver = webdriver.Chrome(service = s)
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)

