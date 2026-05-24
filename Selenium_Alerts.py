import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
print(f"Page Title --> {driver.title}") # Practice page



# Simple Alert
simple_alert = driver.find_element(By.XPATH, "//button[@id='simpleAlert']")
driver.execute_script("arguments[0].scrollIntoView();", simple_alert) # java_script
simple_alert.click()

time.sleep(2)
# import alert
alert = Alert(driver)

# get the text of alert
print(f"alert text --> {alert.text}")

# To accept the alert
alert.accept()


# Confirmation alter
# prompt alter

time.sleep(8)
driver.quit()