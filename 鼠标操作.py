# 鼠标指针悬停
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
setting = driver.find_element_by_link_text("设置")
time.sleep(3)
ActionChains(driver).move_to_element(setting).perform()
time.sleep(5)
driver.find_element_by_link_text("搜索设置").click()
time.sleep(3)

# 模拟鼠标右键
context = driver.find_element_by_id("su")
ActionChains(driver).context_click(context).perform()

# 鼠标双击
double = driver.find_element_by_id("su")
ActionChains(driver).double_click(double).perform()
