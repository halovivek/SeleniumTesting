
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\Drivers\chromedriver.exe")

browser = webdriver.Chrome(service = s)
browser.maximize_window()
browser.get("https://demo.guru99.com/test/newtours/")
links = browser.find_elements(By.TAG_NAME,"a")
#print(links)
print("number of links presents = ", len(links))
for link in links:
    print(link.text)
browser.find_element(By.XPATH, "//*[@id='navbar-brand-centered']/ul/li[3]/a").click()


#browser.get("https://www.google.com")
print(browser.title)
#browser.quit()
