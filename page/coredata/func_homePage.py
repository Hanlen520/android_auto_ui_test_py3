# 进入关键数据后的首页元素
from appium.webdriver.common.mobileby import By

data_report = (By.XPATH, "//android.widget.TextView[contains(@text,'数据报表')]")
enter_data = (By.XPATH, "//android.widget.TextView[contains(@text,'数据项录入')]")
query_data = (By.XPATH, "//android.widget.TextView[contains(@text,'数据查询')]")
report_setting = (By.XPATH, "//android.widget.TextView[contains(@text,'报表设置')]")
data_setting = (By.XPATH, "//android.widget.TextView[contains(@text,'数据项设置')]")
interface_setting = (By.XPATH, "//android.widget.TextView[contains(@text,'接口设置')]")
renter_reportData = (By.XPATH, "//android.widget.TextView[contains(@text,'报表数据录入')]")
