
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

# Invoke the firefox
driver = webdriver.Firefox()
# To go below url
driver.get("https://apps.credence.in/practice")

time.sleep(2)

#  Select Multi select Drop down box
drop_down_list = driver.find_element(By.ID, "multiSelect")
select_drop_down  = Select(drop_down_list)
time.sleep(2)

# To Select Item 1 by visible text
select_drop_down.select_by_visible_text("Item 1")
time.sleep(2)

# To Select Item 2 by index
select_drop_down.select_by_index(1)

# To Select Item 5 by index
select_drop_down.select_by_index(4)


print(select_drop_down.all_selected_options[0].text == "Item 1") # True
print(select_drop_down.all_selected_options[1].text == "Item 2") # True
print(select_drop_down.all_selected_options[2].text == "Item 5") # True


#assert select_drop_down.first_selected_option.text == "Option1", "Dropdown Option1 is not selected."


"""
1. For Select Hub extension go to below link to add it in your brower
    Firefox :
    https://addons.mozilla.org/en-US/firefox/addon/selectorshub/
    
    Chrome:
    https://chromewebstore.google.com/detail/selectorshub/ndgimibanhlabgdgjcpbbndiehljcpfh


2. Click on add to firefox/chrome, to add selector hub extension in browser


3. Also add test case studio.

    firefox :
    https://addons.mozilla.org/en-US/firefox/addon/testcase-studio/
    
    chrome:
    https://chromewebstore.google.com/detail/testcase-studio-selenium/loopjjegnlccnhgfehekecpanpmielcj


4. Click on add to firefox/chrome, to add testcase studio in browser


"""

