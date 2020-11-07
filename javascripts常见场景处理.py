from selenium import webdriver


driver = webdriver.Chrome()
# driver.get("")
# # 向富文本输入内容A
# js = "document.getElementById('content_ifr').contentwindow.document.body.innerHTML = '%s'" % ("A")
# driver.execute_script(js)
#
# # 元素被隐藏时,将元素设置可见
# js_display = "document.querySelectorAll('select')[0].style.display='block';"
# driver.execute_script(js_display)
#
# # 处理readonly
# js_readonly = "document.getElementById('id').removeAttribute('readonly');"
# driver.execute_script(js_readonly)

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
import time
time.sleep(3)
driver.execute_script('window.scrollTo(0,10000)')  # 将页面滚动条拖到底部
time.sleep(5)
driver.execute_script('window.scrollTo(10000,0)')  # 将滚动条拖到顶部
time.sleep(5)
driver.quit()