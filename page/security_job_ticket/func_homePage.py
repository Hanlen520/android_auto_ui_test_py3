# 进入安全作业单后的首页元素
from appium.webdriver.common.mobileby import By

jobticket_to_evaluate = (By.XPATH, "//android.widget.TextView[contains(@text,'待评估作业单')]")
jobticket_to_apporve = (By.XPATH, "//android.widget.TextView[contains(@text,'待审批作业单')]")
jobticket_doing = (By.XPATH, "//android.widget.TextView[contains(@text,'进行中作业单')]")
completed_jobticket = (By.XPATH, "//android.widget.TextView[contains(@text,'已完成作业单')]")
query_jobticket = (By.XPATH, "//android.widget.TextView[contains(@text,'作业单查询')]")
count_jobticket = (By.XPATH, "//android.widget.TextView[contains(@text,'作业单统计')]")
