import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
print(f"Page Title --> {driver.title}") # Practice page


credence_site = driver.find_element(By.XPATH, "//a[@id='opentab1']")
credence_site.click()
print(f"Page Title --> {driver.title}") # Practice page


# switch to new tab -credence
driver.switch_to.window(driver.window_handles[1]) # driver will switch to credence_site tab
time.sleep(2)
print(f"Page Title --> {driver.title}") # Software Testing Training Institute - Credence

# switch to new tab - practice
driver.switch_to.window(driver.window_handles[0]) # driver will switch to practice tab

bank_site = driver.find_element(By.XPATH, "//a[@id='opentab2']")
bank_site.click()

# switch to new tab -Bank Application
driver.switch_to.window(driver.window_handles[1]) # driver will switch to bank app tab
time.sleep(2)
print(f"Page Title --> {driver.title}") # Bank Application

# switch to new tab -credence
driver.switch_to.window(driver.window_handles[2]) # driver will switch to credence_site tab
time.sleep(2)
print(f"Page Title --> {driver.title}") # Software Testing Training Institute - Credence




time.sleep(8)
driver.quit()
#open_window.click()