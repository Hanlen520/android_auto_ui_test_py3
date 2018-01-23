import selenium.common

from page import shouye
from page.login_page import login, choose_server, judge_homepage


class LoginSystem:
    def __init__(self, android_driver, username='18121225109', password='123456'):
        self.d = android_driver
        self.uname = username
        self.pwd = password

    def _login_steps(self):  # 登录的通用方法，输入用户名、密码后点击登录
        self.d.find_element(*login.username).clear()
        self.d.find_element(*login.username).send_keys(self.uname)
        self.d.find_element(*login.password).clear()
        self.d.find_element(*login.password).send_keys(self.pwd)
        self.d.find_element(*login.login_button).click()

    def _input_code(self):  # 输入用户代码，选择服务器(0004为自动化测试的服务器)
        self.d.find_element(*choose_server.zero).click()
        self.d.find_element(*choose_server.zero).click()
        self.d.find_element(*choose_server.zero).click()
        self.d.find_element(*choose_server.four).click()

    def login(self):
        try:
            if self.d.find_element(*judge_homepage.usercode_first) is not None:
                self._input_code()
                self._login_steps()
                return 1
        except selenium.common.exceptions.NoSuchElementException:
            print()
        try:
            if self.d.find_element(*login.username) is not None:
                self.d.find_element(*login.choose_server).click()
                self._input_code()
                self._login_steps()
                return 2
        except selenium.common.exceptions.NoSuchElementException:
            print()
        try:
            if self.d.find_element(*judge_homepage.usercode_after_long_time) is not None:
                self._input_code()
                return 3
        except selenium.common.exceptions.NoSuchElementException:
            print()
        try:
            if self.d.find_element(*shouye.switch_btn) is not None:
                print("已登录")
                return 4
        except selenium.common.exceptions.NoSuchElementException:
            print()
