from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

# value 属性定位
driver = webdriver.Chrome()
driver.get("")
element = driver.find_element(By.ID, "")
Select(element).select_by_value("")
# index 属性定位
Select(element).deselect_by_index("")
# visible_text 属性定位
Select(element).deselect_by_visible_text("")
