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
"""
click(on_element=None) ——单击鼠标左键

click_and_hold(on_element=None) ——点击鼠标左键，不松开

context_click(on_element=None) ——点击鼠标右键

double_click(on_element=None) ——双击鼠标左键

drag_and_drop(source, target) ——拖拽到某个元素然后松开

drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开

key_down(value, element=None) ——按下某个键盘上的键

key_up(value, element=None) ——松开某个键

move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标

move_to_element(to_element) ——鼠标移动到某个元素

move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置

perform() ——执行链中的所有动作

release(on_element=None) ——在某个元素位置松开鼠标左键

send_keys(*keys_to_send) ——发送某个键到当前焦点的元素

send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素
"""