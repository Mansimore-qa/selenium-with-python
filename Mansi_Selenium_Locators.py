import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.gucci.com/")
driver.maximize_window()
print(f"Page title --> {driver.title}")
time.sleep(3)



# Locator --> ID
username_field = driver.find_element(By.ID , "username")
username_field.send_keys("Testuser011")

# Locator --> NAME
password_field = driver.find_element(By.NAME , "password")
password_field.send_keys("Shital@1234")
time.sleep(2)

# Locator --> Class_Name
login_button = driver.find_element(By.CLASS_NAME, "submitButton")
login_button.click()

time.sleep(2)
driver.quit()
