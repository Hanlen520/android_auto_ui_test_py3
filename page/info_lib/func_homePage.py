# 进入信息库后的首页元素
from appium.webdriver.common.mobileby import By

browse = (By.XPATH, "//android.widget.TextView[@text='浏览']")
myCollection = (By.XPATH, "//android.widget.TextView[@text='我的收藏']")
retrieve = (By.XPATH, "//android.widget.TextView[@text='检索']")
attachment_retrieve = (By.XPATH, "//android.widget.TextView[@text='附件检索']")
