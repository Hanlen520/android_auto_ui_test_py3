import unittest

from commonActions.login import LoginSystem
from driver.driver import Driver
from page import shouye
from page.hse import HSE


class TestSF(unittest.TestCase):
    def setUp(self):
        self.d = Driver().get_android_driver()

    def test_suc_1(self):
        LoginSystem(self.d).login()
        self.d.find_element(*shouye.switch_btn).click()
        self.d.find_element(*shouye.HSE).click()
        self.d.find_element(*HSE.renyuan_security).click()
        self.assertEqual(self.d.find_element(*HSE.yinhuan_guanli), None)

    def tearDown(self):
        self.d.quit()


if __name__ == "__main__":
    unittest.main()
