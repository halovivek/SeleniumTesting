from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.common.by import By

#s = Service("C:\Drivers\geckodriver.exe")
browser = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
#browser = webdriver.firefox(service = s)
browser.maximize_window()
browser.get("https://demo.guru99.com/test/newtours/")
print(browser.title)