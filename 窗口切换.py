from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# driver.find_element_by_id("kw").send_keys("渗透吧")
# driver.find_element_by_id("su").click()
# sleep(3)
# # 第一个窗口下点击渗透吧链接
# driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
# sleep(3)
# # 使用get方法获取跳转后的URL
# driver.get("https://tieba.baidu.com/f?kw=%C9%F8%CD%B8&fr=ala0&tpl=5")
# sleep(3)
# driver.find_element_by_link_text("进入贴吧").click()

driver.get("https://www.so.com")
sleep(2)
driver.find_element_by_link_text("360导航").click()
sleep(2)
# 获取所有窗口的句柄
windows = driver.window_handles
# 通过索引切换到第二个窗口
driver.switch_to.window(windows[1])
sleep(2)
driver.find_element_by_id("search-kw").send_keys("第二个窗口")
sleep(2)
# 切换到第一个窗口
driver.switch_to.window(windows[0])
driver.find_element_by_id("input").send_keys("第一个窗口")





