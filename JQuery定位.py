from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.jianshu.com/sign_in")
js_class = 'document.getElementsByClassName("active")[0].click();'
driver.execute_script(js_class)
time.sleep(2)

js_input = 'document.getElementsyTagName("input")[2].value="username";'
driver.execute_script(js_input)
time.sleep(2)

js_passwd = 'documentElementsByTagName("input")[3].value="password";'
driver.execute_script(js_passwd)
time.sleep(2)

css_btn = 'document.querySelectorAll(".sign-in-button")[0].click();'
driver.execute_script(css_btn)

# JQuery 定位语法可以统一用 document.querySelectorAll()  方法返回的是list对象

