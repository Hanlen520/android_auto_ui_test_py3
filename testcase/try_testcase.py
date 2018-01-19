from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from commonActions.find_el import Find_el
from commonActions.login_sys import LoginSystem
from driver.driver import Driver
from page import shouye
from page.hse import HSE,renyuan_Security


def ceshi(d):
    LoginSystem(d).login()
    Find_el(d).find_element(shouye.switch_btn).click()
    Find_el(d).find_element(shouye.HSE).click()
    Find_el(d).find_element(HSE.renyuan_security).click()
    Find_el(d).find_element(renyuan_Security.zidingyi_search).click()
    Find_el(d).find_element('com.gongzhidao.inroad:id/edit_name').click()
    Find_el(d).find_element('com.gongzhidao.inroad:id/edit_name').send_keys("2019-08-21")
    ActionChains(d).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    ActionChains(d).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    ActionChains(d).key_down(Keys.CONTROL,Find_el(d).find_element('com.gongzhidao.inroad:id/edit_begindate')).send_keys('v').key_up(Keys.CONTROL).perform()


if __name__ == "__main__":
    d = Driver().get_android_driver()
    ceshi(d)
