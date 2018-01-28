# 进入HSE后的首页元素
from appium.webdriver.common.mobileby import By

renyuan_security = (By.XPATH, "//android.widget.TextView[contains(@text,'人员行为安全')")
yinhuan_guanli = (By.XPATH, "//android.widget.TextView[contains(@text,'隐患管理')")
