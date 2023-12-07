import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH,"//span[@aria-label='Country']//b[@role='presentation']").click()

countries=driver.find_element(By.XPATH,"")
print(len(countries))

for country in countries:
    if country.text=="India":
        country.click()
        break