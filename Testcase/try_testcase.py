from common.find_el import Find_el
from common.login_sys import LoginSystem
from driver.driver import Driver
from page import shouye


def ceshi():
    d = Driver().get_android_driver()
    LoginSystem(d).login()
    Find_el(d).find_element(shouye.switch_btn).click()
    Find_el(d).find_element(shouye.process).click()


if __name__ == "__main__":
    ceshi()
