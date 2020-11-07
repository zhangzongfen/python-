from PO_selenium_demo.basepase.homeBase import HomePage
from time import sleep
from selenium.webdriver.common.by import By


class LoginPage(HomePage):
    # 定位器
    username_loc = (By.ID, 'loginName')
    password_loc = (By.ID, 'password')
    loginBtn_loc = (By.ID, 'btnSubmit')
    assertText_loc = (By.XPATH, '/html/body/div[1]/header/nav/div[2]/ul/li[5]/a/span')

    def openLoginPage(self):
        self.dr.get(self.url)
        self.dr.refresh()
        self.dr.maximize_window()
        sleep(1)

    def input_username(self, username):
        self.dr.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.dr.find_element(*self.password_loc).send_keys(password)

    def click_loginbtn(self):
        self.dr.find_element(*self.loginBtn_loc).click()

    def get_assertText(self):
        return self.dr.find_element(*self.assertText_loc).text

    def login_jsh(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_loginbtn()




