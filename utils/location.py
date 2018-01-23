import os

# BasePath = os.path.abspath(__file__)  # 当前文件的绝对路径
# CurrentDir = os.path.dirname(os.path.abspath(__file__))  # 当前文件的父目录，即当前文件所在的目录
ROOT_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # project的绝对路径

'''
定位project目录下的文件夹
'''

COMMONACTIONS_PATH = os.path.join(ROOT_DIR, 'commonActions')
CONFIG_PATH = os.path.join(ROOT_DIR, 'config')
DRIVER_PATH = os.path.join(ROOT_DIR, 'driver')
PAGE_PATH = os.path.join(ROOT_DIR, 'page')
REPORT_PATH = os.path.join(ROOT_DIR, 'report')
TESTCASE_PATH = os.path.join(ROOT_DIR, 'testcase')
UTILS_PATH = os.path.join(ROOT_DIR, 'utils')
SCREENSHOT_PATH = os.path.join(ROOT_DIR, 'screenshot')

DES_CAPS_FILE_PATH = os.path.join(ROOT_DIR, 'config', 'des_caps.yaml')
