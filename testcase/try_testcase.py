from commonActions.login_sys import LoginSystem
from driver.driver import Driver
from page import shouye
from page.hse import HSE, renyuan_Security

def ceshi(d):
    LoginSystem(d).login()
    d.find_element(*shouye.switch_btn).click()
    d.find_element(*shouye.HSE).click()
    d.find_element(*HSE.renyuan_security).click()
    d.find_element(*renyuan_Security.zidingyi_search).click()


if __name__ == "__main__":
    d = Driver().get_android_driver()
    ceshi(d)
