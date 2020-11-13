from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
import time

url = 'D:\\PyCharm 2019.1.1\\workspace\\python-selenium\\test_html.html'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
# 获取第一，二，三能拖拽的元素
drag1 = driver.find_element_by_id('dragEle')

# 创建一个新的ActionChains，将webdriver实例对driver作为参数值传入，然后通过WenDriver实例执行用户动作
action_chains = ActionChains(driver)
# 将页面上的第一个能被拖拽的元素拖拽到第二个元素位置
# 将页面上的第三个能拖拽的元素，向右下拖动10个像素，共拖动5次
action_chains.drag_and_drop_by_offset(drag1, 208, 0).perform()
time.sleep(5)
driver.quit()
