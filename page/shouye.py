from appium.webdriver.common.mobileby import By

# 2017-12-290版本的首页菜单选项(部分摘录，用于UI自动化)

switch_btn = (By.ID, "com.gongzhidao.inroad:id/switch_btn")  # 个人/菜单 切换按钮
personal = (By.ID, "com.gongzhidao.inroad:id/personal")  # 个人信息按钮
process = (By.ID, "com.gongzhidao.inroad:id/process")  # 流程
notification = (By.ID, "com.gongzhidao.inroad:id/bell")  # 提醒
task = (By.ID, "com.gongzhidao.inroad:id/task")  # 任务

gongyi_guanli = (By.XPATH, "//android.widget.TextView[contains(@text,'工艺管理')]")
taizhang_liulan = (By.XPATH, "//android.widget.TextView[contains(@text,'台账浏览')]")
jidian_guanli = (By.XPATH, "//android.widget.TextView[contains(@text,'机电管理')]")
HSE = (By.XPATH, "//android.widget.TextView[contains(@text,'HSE')]")
library = (By.XPATH, "//android.widget.TextView[contains(@text,'信息库')]")
peixun_guanli = (By.XPATH, "//android.widget.TextView[contains(@text,'培训管理')]")
