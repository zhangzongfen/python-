import unittest
from selenium import webdriver
from time import sleep
from PO.basepase.homeBase import *
from PO.page.loginpage import *
from PO.common.ownUnit import MyunitTests
from PO.common.helper import Helper
from PO.common.getImage import SaveImage


class TestLogin(MyunitTests, Helper):
    def test_login(self):
        self.loginpage.openLoginPage()
        self.makelog('PO-jsh:打开浏览器进入地址')
        self.loginpage.login_jsh(self.readusername(1), round(float(self.readpassword(1))))
        self.makelog('PO-jsh: 登录')
        sleep(3)
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-jsh: 断言')
        SaveImage(self.dr, 'login_success.png')
        self.makelog('PO-jsh: 截图')


if __name__ == '__main__':
    unittest.main(verbosity=2)
