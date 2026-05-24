# 1. Install Selenium Library
# Command: pip install selenium (terminal(in cmd not in powershell))


# 2. Download Chrome driver from below url:
# https://googlechromelabs.github.io/chrome-for-testing/#stable

# For 143 version driver url:
# https://storage.googleapis.com/chrome-for-testing-public/143.0.7499.169/win64/chromedriver-win64.zip

import time
from selenium import webdriver
driver = webdriver.Chrome() # invoke the Chrome browser
driver.maximize_window()
driver.get("https://credence.in/")
time.sleep(10)
driver.quit() # quit the browser session




# search the same for firefox and edge