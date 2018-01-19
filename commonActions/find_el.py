from selenium import common

from commonActions.screenshot_after_failure import GetFailureScreenshot as gs


class Find_el(object):
    def __init__(self, driver):
        self.d = driver

    def find_element(self, el_string, wait_time=15):
        el = None

        if el_string.startswith("//android.widget"):  # 通过xpath的方式寻找元素
            try:
                self.d.find_element_by_xpath(el_string).is_displayed()
                el = self.d.find_element_by_xpath(el_string)
            except common.exceptions.NoSuchElementException:
                gs(self.d).jietu()

        elif el_string.startswith("com."):  # 通过id的方式寻找元素
            try:
                self.d.find_element_by_id(el_string).is_displayed()
                el = self.d.find_element_by_id(el_string)
            except common.exceptions.NoSuchElementException:
                gs(self.d).jietu()

        self.d.implicitly_wait(wait_time)
        return el
