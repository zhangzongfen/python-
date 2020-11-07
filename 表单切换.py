from selenium import webdriver

driver = webdriver.Chrome()
driver.get("")

# 单表单切换
# 切换iframe标签
driver.switch_to.frame("")
# 退出iframe标签
driver.switch_to.default_content()


# 嵌套表单切换
# 先切换到最外层iframe标签
driver.switch_to.frame("")
# 在切换到第二个iframe标签
driver.switch_to.frame("")
# 定位需要的标签元素
driver.find_element_by_id("").send_keys("")


# 平行切换表单
# 在第一个iframe
driver.switch_to.frame("")
# 退出第一个iframe
driver.switch_to.default_content()
# 切换到第二个iframe
driver.switch_to.frame("")
# 操作第二个iframe下的元素
driver.find_element_by_id("").send_keys("")
#  iframe 无论几层，执行一次退出，就是最外层

