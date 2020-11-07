from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

tag = driver.find_elements_by_tag_name("input")

for i in tag:
    if i.get_attribute('autocomplete') == "off":
        i.send_keys('fighter007')
driver.find_element_by_id("su").click()
time.sleep(2)
driver.quit()
