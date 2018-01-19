from selenium import webdriver

from utils import location
from utils.readYaml import ReadYaml


class Driver:
    def __init__(self):
        des_caps = ReadYaml(location.DES_CAPS_FILE_PATH).yaml_data()
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", des_caps)

    def get_android_driver(self):
        return self.driver


if __name__ == "__main__":
    Driver().get_android_driver()
