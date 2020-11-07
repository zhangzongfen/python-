import xlrd
import ddt, unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def readData():
    book = xlrd.open_workbook('datainfo.xlsx', 'r')
    table = book.sheet_by_index(0)
    newRows= []
    for i in range(1, table.nrows):
        newRows.append(table.row_values(i, 0, table.ncols))

    return newRows


@ddt.ddt
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

    @ddt.data(*readData())
    @ddt.unpack
    def test_souHuLogin(self, user, passwd, text):
        self.driver.get(self.url)
        sleep(2)
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').clear()
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').clear()
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(passwd)
        self.by_css('.btn-login.fontFamily').click()
        self.assertEqual(self.getasserText(), text)


if __name__ == '__main__':
    unittest.main()