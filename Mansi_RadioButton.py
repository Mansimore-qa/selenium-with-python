import time

from selenium.webdriver.common.by import By
from selenium import webdriver
# Invoke the firefox
driver = webdriver.Firefox()
# To go below url
driver.get("https://apps.credence.in/practice")
time.sleep(2)

radio1 = driver.find_element(By.XPATH, "//input[@value='radio1']")
radio1.click()

time.sleep(2)

radio2 = driver.find_element(By.XPATH, "//input[@value='radio2']")
radio2.click()

time.sleep(2)

radio3 = driver.find_element(By.XPATH, "//input[@value='radio3']")

time.sleep(2)
driver.quit()