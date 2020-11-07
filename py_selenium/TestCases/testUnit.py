from TestCases.Myunit import TestWebUI
import ddt, unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def readData():
    return [
        ['', '', '请输入账号密码'],
        ['admin123@sohu.com', '', '请输入账号密码'],
        ['admin111@sohu.com', '', '请输入账号密码'],
        ['', 'a123456789', '请输入账号密码']
    ]


@ddt.ddt
class TestModle(TestWebUI):
    # def test_QQLogin(self):
    #     self.driver.get("https://mail.qq.com/cgi-bin/loginpape")
    #     self.assertEqual(self.driver.title, '登录QQ邮箱')
    #
    # def test_MaoyanMovie(self):
    #     self.driver.get("https://maoyan.com/")
    #     self.assertEqual(self.driver.title, '猫眼电影 - 一网打尽好电影')

    def by_css(self, usernameloc):
        '''
        重写css定位
        :return:
        '''
        return self.driver.find_element_by_css_selector(usernameloc)

    def getasserText(self):
        '''
        获取验证信息
        :return:
        '''
        try:
            sleep(3)
            loctor = (By.CSS_SELECTOR, '.tipHolder.ng-binding')
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((loctor)))
            return self.by_css('.tipHolder.ng-binding').text
        except Exception as message:
            print("元素定位报错，报错原因：{}".format(message))

    @ddt.data(*readData())
    @ddt.unpack
    def test_sohuLogin(self, user, passwd, text):
        self.driver.get("https://mail.sohu.com/fe/#/login")
        sleep(3)
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').clear()
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').clear()
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(passwd)
        self.by_css('.btn-login.fontFamily').click()
        self.assertEqual(self.getasserText(), text)


if __name__ == '__main__':
    unittest.main()
