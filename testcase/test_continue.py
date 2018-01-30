import os
import time
import unittest

import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from commonActions import capture_after_failure
from commonActions.login import LoginSystem
from driver.driver import Driver
from page import shouye
from page.hse import func_homePage as hse_homePage
from page.hse import renyuan_Security
from page.info_lib import func_homePage as info_homePage
from utils import location
from utils.readINI import Readini


class TestContinue(unittest.TestCase):
    """不退出，连续测试"""
    user_info = Readini(location.CONF_INI_PATH).ini_data()
    usr = user_info.get('info', 'username')
    pwd = user_info.get('info', 'password')

    @classmethod
    def setUpClass(cls):
        cls.d = Driver().get_android_driver()

    @classmethod
    def tearDownClass(cls):
        cls.d.quit()

    @capture_after_failure.capture
    def testLogin(self):
        """--登录--测试"""
        LoginSystem(self.d, self.usr, self.pwd).login()
        WebDriverWait(self.d, 20, 0.5).until(ec.visibility_of_element_located(shouye.switch_btn))
        self.assertEqual(self.d.find_element(*shouye.switch_btn).is_displayed(), True, '登录成功')

    @capture_after_failure.capture
    def testZiDingYi_f(self):
        """搜索--自定义--测试，故意失败的case"""
        self.d.find_element(*shouye.switch_btn).click()
        self.d.find_element(*shouye.HSE).click()
        self.d.find_element(*hse_homePage.renyuan_security).click()
        self.assertEqual(self.d.find_element(*info_homePage.attachment_retrieve).is_displayed(), True)

    @capture_after_failure.capture
    def testZiDingYi_s(self):
        """搜索--自定义查询--测试"""
        self.assertEqual(self.d.find_element(*renyuan_Security.zidingyi_search).is_displayed(), True, '找到自定义查询')

    @capture_after_failure.capture
    @unittest.skip('强制跳过测试')
    def testBlacklist(self):
        """搜索--黑名单--测试"""
        self.assertEqual(self.d.find_element(*renyuan_Security.blacklist).is_displayed(), True, '找到黑名单')


if __name__ == "__main__":
    now = time.strftime('%Y%m%d%H%M', time.localtime())
    test_unit = unittest.TestSuite()
    f = open(os.path.join(location.REPORT_PATH, 'report_' + now + '.html'), 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='appium自动化UI测试报告', description='', verbosity=2)
    # test_unit.addTest(unittest.makeSuite(TestContinue))
    test_unit.addTest(TestContinue('testLogin'))
    test_unit.addTest(TestContinue('testZiDingYi_f'))
    test_unit.addTest(TestContinue('testBlacklist'))
    test_unit.addTest(TestContinue('testZiDingYi_s'))
    runner.run(test_unit)
    f.close()
