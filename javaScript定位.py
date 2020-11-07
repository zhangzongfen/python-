# 定位方式： getElementsByClassName()  getElementByID()   getElementsByName()
# getElementsByTagName()  document.querySelectorAll()
# 除getElementByID()返回单个elements元素定位外，其他方式都返回list
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.jianshu.com/sign_in")
time.sleep(2)
# js_register = 'document.getElementById("js-sign-up-btn").click();'
# driver.execute_script(js_register)
# time.sleep(2)
# js_class = 'document.getElementsByClassName("active")[0].click();'
# driver.execute_script(js_class)
# time.sleep(2)

js_input = 'document.getElementsByTagName("inout")[2].value="username";'
driver.execute_script(js_input)
time.sleep(2)

driver.quit()
