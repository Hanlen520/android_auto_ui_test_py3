import os

import yaml
from selenium import webdriver


class Driver:
    def __init__(self):
        #  最好使用相对地址
        config_file = os.path.dirname(os.getcwd()) + '/driver/des_caps.yaml'
        des_caps = yaml.load(open(config_file))
        # print(des_caps)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", des_caps)

    def get_android_driver(self):
        return self.driver


if __name__ == "__main__":
    Driver().get_android_driver()
