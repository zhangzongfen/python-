from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(object):
    def __init__(self, url, dr):
        self.url = url
        self.dr = dr

    def find_element(self, *loc):
        try:
            WebDriverWait(self.dr, 20).until(EC.visibility_of_element_located(loc))
            return self.dr.find_element(*loc)

        except:
            print(*loc + "没有找到元素")

