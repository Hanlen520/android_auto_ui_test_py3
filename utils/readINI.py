import configparser
import os

from utils import location


class Readini:

    def __init__(self, inif):
        self.inif = inif

    def ini_data(self):
        if os.path.exists(self.inif):
            cf = configparser.ConfigParser()
            cf.read(location.CONF_INI_PATH)
            return cf
        else:
            raise FileNotFoundError("文件不存在")
