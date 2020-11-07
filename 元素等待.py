from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# 强制等待
sleep(5)
driver.find_element_by_id("kw").send_keys("强制等待")

# 隐侍等待
driver.implicitly_wait(20)

# 显示等待

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'freename')))
element.send_keys('hello')
driver.quit()
