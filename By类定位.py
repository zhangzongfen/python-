from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# By.ID  By.NAME By.XPATH By.CLASS_NAME By.LINK_TEXT By.CSS_SELECTOR
driver.find_element(By.ID, "kw").send_keys("By类定位")

time.sleep(2)
driver.quit()