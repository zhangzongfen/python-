import unittest, yaml
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def readYaml():
    """获取数据"""
    f = open("data.yaml", 'r', encoding="utf-8")
    data = yaml.load(f)
    f.close()

    return data


class TestSouHuLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = "https://mail.sohu.com/fe/#/login"

    def tearDown(self) -> None:
        self.driver.quit()

    def by_css(self, usernameloc):
        """重写css定位"""
        return self.driver.find_element_by_css_selector(usernameloc)

    def getasserText(self):
        """获取验证信息"""
        try:
            sleep(2)
            loctor = (By.CSS_SELECTOR, '.tipHolder.ng-binding')
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((loctor)))
            return self.by_css('.tipHolder.ng-binding').text
        except Exception as message:
            print("元素定位报错，报错原因：{}".format(message))

    def souhuLogin(self, user, passwd):
        """登录功能封装"""
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').clear()
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').clear()
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(passwd)
        self.by_css('.btn-login.fontFamily').click()

    def test_souHuLogin_001(self):
        """账号密码为空：登录失败"""
        self.driver.get(self.url)
        sleep(2)
        self.souhuLogin(readYaml()['userNull']['username'], readYaml()['userNull']['password'])
        self.assertEqual(self.getasserText(), readYaml()['userNull']['asserText'])

    def test_souHuLogin_002(self):
        """账号正确密码为空：登录失败"""
        self.driver.get(self.url)
        sleep(2)
        self.souhuLogin(readYaml()['passNull']['username'], readYaml()['passNull']['password'])
        self.assertEqual(self.getasserText(), readYaml()['passNull']['asserText'])


if __name__ == '__main__':
    unittest.main()
