import unittest

from commonActions.find_el import Find_el
from commonActions.login_sys import LoginSystem
from driver.driver import Driver
from page import shouye
from page.hse import HSE


class TestSF(unittest.TestCase):
    def setUp(self):
        self.d = Driver().get_android_driver()

    def test_suc_1(self):
        LoginSystem(self.d).login()
        Find_el(self.d).find_element(shouye.switch_btn).click()
        Find_el(self.d).find_element(shouye.HSE).click()
        Find_el(self.d).find_element(HSE.renyuan_security).click()
        self.assertEqual(Find_el(self.d).find_element(HSE.yinhuan_guanli), None)

    def tearDown(self):
        self.d.quit()


if __name__ == "__main__":
    unittest.main()