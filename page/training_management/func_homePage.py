# 进入培训管理后的首页元素
from appium.webdriver.common.mobileby import By

my_course = (By.XPATH, "//android.widget.TextView[@text='我的课程']")
my_subject = (By.XPATH, "//android.widget.TextView[@text='我的课题']")
my_examination = (By.XPATH, "//android.widget.TextView[@text='我的测验']")
self_study = (By.XPATH, "//android.widget.TextView[@text='自主学习']")
my_qualification = (By.XPATH, "//android.widget.TextView[@text='我的资质']")
my_collection = (By.XPATH, "//android.widget.TextView[@text='我的收藏']")
course_setting = (By.XPATH, "//android.widget.TextView[@text='课程设置']")
subject_setting = (By.XPATH, "//android.widget.TextView[@text='课题设置']")
examination_setting = (By.XPATH, "//android.widget.TextView[@text='测验设置']")
