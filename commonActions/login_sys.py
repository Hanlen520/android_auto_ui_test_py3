from commonActions.find_el import Find_el
from page.login_page import login,choose_server,judge_homepage
from page import shouye


class LoginSystem:
    def __init__(self, android_driver, username='18121225109', password='123456'):
        self.d = android_driver
        self.uname = username
        self.pwd = password

    def _login_steps(self):  # 登录的通用方法，输入用户名、密码后点击登录
        Find_el(self.d).find_element(login.username).clear()
        Find_el(self.d).find_element(login.username).send_keys(self.uname)
        Find_el(self.d).find_element(login.password).clear()
        Find_el(self.d).find_element(login.password).send_keys(self.pwd)
        Find_el(self.d).find_element(login.login_button).click()

    def _input_code(self):  # 输入用户代码，选择服务器(0004为自动化测试的服务器)
        Find_el(self.d).find_element(choose_server.zero).click()
        Find_el(self.d).find_element(choose_server.zero).click()
        Find_el(self.d).find_element(choose_server.zero).click()
        Find_el(self.d).find_element(choose_server.four).click()

    def login(self):
        if Find_el(self.d).find_element(judge_homepage.usercode_first) is not None:
            self._input_code()
            self._login_steps()
        elif Find_el(self.d).find_element(login.username) is not None:
            Find_el(self.d).find_element(login.choose_server).click()
            self._input_code()
            self._login_steps()
        elif Find_el(self.d).find_element(judge_homepage.usercode_after_long_time) is not None:
            self._input_code()
        elif Find_el(self.d).find_element(shouye.switch_btn) is not None:
            print("已登录")
