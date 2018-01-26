from appium import webdriver

from utils import location
from utils.readYaml import ReadYaml


class Driver:
    def __init__(self):
        des_caps = ReadYaml(location.DES_CAPS_FILE_PATH).yaml_data()
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def get_android_driver(self):
        return self.driver
