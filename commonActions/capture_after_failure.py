import time

from driver import driver
from utils import location


class GetFailureScreenshot(object):
    def __init__(self, android_driver):
        self.d = android_driver

    def capture(self):
        tamp = time.strftime('%Y%m%d%H%M', time.localtime())
        filename = location.SCREENSHOT_PATH + '/ %s.png' % tamp
        self.d.get_screenshot_as_file(filename)


if __name__ == "__main__":
    d = driver.Driver().get_android_driver()
    GetFailureScreenshot(d).capture()
