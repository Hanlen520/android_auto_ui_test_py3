import os
import time
import unittest

import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from commonActions.login import LoginSystem
from driver.driver import Driver
from page import shouye
from page.hse import HSE, renyuan_Security
from utils import location
from utils.readINI import Readini


class TestContinue(unittest.TestCase):
    """不退出driver测试"""
    user_info = Readini(location.CONF_INI_PATH).ini_data()
    usr = user_info.get('info', 'username')
    pwd = user_info.get('info', 'password')

    @classmethod
    def setUpClass(cls):
        cls.d = Driver().get_android_driver()

    @classmethod
    def tearDownClass(cls):
        cls.d.quit()

    def testLogin(self):
        """登录测试"""
        LoginSystem(self.d, self.usr, self.pwd).login()
        WebDriverWait(self.d, 20, 0.5).until(ec.visibility_of_element_located(shouye.switch_btn))
        self.assertEqual(self.d.find_element(*shouye.switch_btn).is_displayed(), True)

    def testZiDingYi(self):
        """搜索查询自定义测试"""
        self.d.find_element(*shouye.switch_btn).click()
        self.d.find_element(*shouye.HSE).click()
        self.d.find_element(*HSE.renyuan_security).click()
        self.assertEqual(self.d.find_element(*renyuan_Security.zidingyi_search).is_displayed(), True)


if __name__ == "__main__":
    now = time.strftime('%Y%m%d%H%M', time.localtime())
    test_unit = unittest.TestSuite()
    f = open(os.path.join(location.REPORT_PATH, 'report_' + now + '.html'), 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='appium自动化UI测试报告', description='')
    test_unit.addTest(unittest.makeSuite(TestContinue))
    runner.run(test_unit)
    f.close()
    # unittest.main()
