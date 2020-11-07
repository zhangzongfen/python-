from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
sleep(3)
setting = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(setting).perform()
sleep(5)

driver.find_element_by_link_text("搜索设置").click()
sleep(5)

driver.find_element_by_id("SL_1").click()
sleep(3)

select = driver.find_element_by_xpath("//select[@id='nr']")
Select(select).select_by_value(20)
sleep(3)

driver.find_element_by_class_name("prefpanelgo").click()
# 获取弹框文本
alter_text = driver.switch_to.alert.text

print(alter_text)
# 确认弹框
driver.switch_to.alert.accept()
# 取消弹框
driver.switch_to.alert.dismiss()

