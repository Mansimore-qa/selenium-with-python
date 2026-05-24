import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
print(f"Page Title --> {driver.title}")

# Switch Window

open_window = driver.find_element(By.XPATH, "//button[@id='openwindow']")
driver.execute_script("arguments[0].scrollIntoView();", open_window) # java_script # new
open_window.click()
time.sleep(2)
print(f"Page Title --> {driver.title}") # till it is in the old window

#  Switch to new window
driver.switch_to.window(driver.window_handles[1]) # driver will switch to new window # new
print(f"Page Title --> {driver.title}")

msg = driver.find_element(By.XPATH, "//span[@class='text-white b label']").text # new
print(f"Message -- > {msg}")




#  Switch to old window
driver.switch_to.window(driver.window_handles[0]) # driver will switch to new window # new
print(f"Page Title --> {driver.title}") # practice page


time.sleep(8)
driver.quit()
#open_window.click()