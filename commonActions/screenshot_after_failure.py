import time
from driver import driver


class GetFailureScreenshot(object):
    def __init__(self, d):
        self.d = d

    def jietu(self):
        tamp = time.strftime('%Y%m%d%H%M', time.localtime())
        filename = '../failure_screenshot/ %s.png' % tamp
        self.d.get_screenshot_as_file(filename)


if __name__ == "__main__":
    print(time.strftime('%Y%m%d%H%M', time.localtime()))
    d = driver.Driver().get_android_driver()
    GetFailureScreenshot(d).jietu()

