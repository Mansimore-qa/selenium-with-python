
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

# Invoke the firefox
driver = webdriver.Firefox()
# To go below url
driver.get("https://apps.credence.in/practice")

time.sleep(2)

#  Select Drop down box
drop_down = driver.find_element(By.ID, "dropdown-class-example")
select_drop_down  = Select(drop_down)
time.sleep(2)
# To Select Option3 by visible text
select_drop_down.select_by_visible_text("Option3")
time.sleep(2)
# To Select Option2 by index
select_drop_down.select_by_index(2)


assert select_drop_down.first_selected_option.text == "Option2", "Dropdown Option2 is not selected."

#assert select_drop_down.first_selected_option.text == "Option1", "Dropdown Option1 is not selected."
