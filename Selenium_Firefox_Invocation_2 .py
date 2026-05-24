'''
install webdriver manager
# Command:
pip install webdriver-manager

It will automatically download and manager the chrome driver
but it is bit slower.
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service # new
from webdriver_manager.chrome import ChromeDriverManager # new
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
url = "https://credence.in/"
driver.get(url)
print(f" You are landed on '{url}' and page title is '{driver.title}'") # Software Testing Training Institute - Credence
time.sleep(10)
driver.quit() # quit the browser session



