from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# 通过find_element_by_id()

# driver.find_element_by_id("kw").send_keys("python自动化测试")
# 通过find_element_by_name()

# driver.find_element_by_name("wd").send_keys("UI测试")

# 通过find_element_by_class_name()
# driver.find_element_by_class_name("s_ipt").send_keys("WEB测试")
# 通过find_element_by_xpath()
# driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys("xpath")
# 通过find_element_by_css_selector()    #表示id, . 表示class  > 表示层级关系（也可空格表示）
# driver.find_element_by_css_selector("input#kw").send_keys("selector")
driver.find_element_by_css_selector("input.s_ipt").send_keys("selector")



time.sleep(2)

driver.quit()


