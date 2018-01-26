from commonActions.login import LoginSystem
from driver.driver import Driver
from page import shouye
from page.hse import HSE, renyuan_Security


def ceshi(d):
    LoginSystem(d).login()
    d.find_element(*shouye.switch_btn).click()
    d.find_element(*shouye.HSE).click()
    d.find_element(*HSE.renyuan_security).click()
    d.find_element(*renyuan_Security.zidingyi_search).click()
    d.find_element_by_id("com.gongzhidao.inroad:id/edit_begindate").send_keys("123456")


if __name__ == "__main__":
    d = Driver().get_android_driver()
    ceshi(d)
'''


if __name__ == "__main__":
    d = Driver().get_android_driver()
    mesg = '//*[@text=\'{}\']'.format("网络连接错误")
    el = WebDriverWait(d, 20, 0.5).until(ec.presence_of_all_elements_located((By.XPATH, mesg)))
    if el:
        print(1)
    else:
        print(2)
'''
