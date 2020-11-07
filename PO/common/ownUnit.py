from PO.basepase.homeBase import *
from PO.page.loginpage import *
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait


class MyunitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://localhost:8080/login.html"
        self.dr = webdriver.Chrome()
        WebDriverWait(self.dr, 2)
        self.loginpage = LoginPage(self.url, self.dr)

    def tearDown(self) -> None:
        self.dr.quit()
