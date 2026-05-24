# Headless browser invocation

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options # new
chrome_options = Options()# new
chrome_options.add_argument("--headless")# new
driver = webdriver.Chrome(options=chrome_options) # new
driver.maximize_window()
url = "https://credence.in/"
driver.get(url)
print(f" You are landed on '{url}' and page title is '{driver.title}'") # Software Testing Training Institute - Credence
driver.quit() # quit the browser session
