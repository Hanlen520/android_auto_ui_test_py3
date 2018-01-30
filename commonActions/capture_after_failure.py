import functools
import os
import time

from utils import location


def capture(func):
    tamp = time.strftime('%Y%m%d%H%M', time.localtime())

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            os.popen("adb wait-for-device")
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png %s/%s_%s.png" % (location.SCREENSHOT_PATH, func.__name__, tamp))
            os.popen("adb shell rm /data/local/tmp/tmp.png")

    return wrapper
