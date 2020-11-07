import unittest
from selenium import webdriver
from time import sleep
from PO_selenium_demo.basepase.homeBase import *
from PO_selenium_demo.page.loginpage import *
from PO_selenium_demo.common.ownUnit import MyunitTests
from PO_selenium_demo.common.helper import Helper
from PO_selenium_demo.common.getImage import SaveImage


class TestLogin(MyunitTests, Helper):
    def test_login(self):
        self.loginpage.openLoginPage()
        self.makelog('PO_selenium_demo-jsh:打开浏览器进入地址')
        self.loginpage.login_jsh(self.readusername(1), round(float(self.readpassword(1))))
        self.makelog('PO_selenium_demo-jsh: 登录')
        sleep(3)
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO_selenium_demo-jsh: 断言')
        SaveImage(self.dr, 'login_success.png')
        self.makelog('PO_selenium_demo-jsh: 截图')


if __name__ == '__main__':
    unittest.main(verbosity=2)
