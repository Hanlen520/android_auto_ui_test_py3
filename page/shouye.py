from appium.webdriver.common.mobileby import By

# 2017-12-290版本的首页菜单选项(部分摘录，用于UI自动化)

switch_btn = (By.ID, "com.gongzhidao.inroad:id/switch_btn")  # 个人/菜单 切换按钮
personal = (By.ID, "com.gongzhidao.inroad:id/personal")  # 个人信息按钮
process = (By.ID, "com.gongzhidao.inroad:id/scan")  # 扫一扫
notification = (By.ID, "com.gongzhidao.inroad:id/rota")  # 值班
task = (By.ID, "com.gongzhidao.inroad:id/task")  # 任务

process_management = (By.XPATH, "//android.widget.TextView[contains(@text,'工艺管理')]")
taizhang_liulan = (By.XPATH, "//android.widget.TextView[contains(@text,'台账浏览')]")
jidian_management = (By.XPATH, "//android.widget.TextView[contains(@text,'机电管理')]")
HSE = (By.XPATH, "//android.widget.TextView[contains(@text,'HSE')]")
info_lib = (By.XPATH, "//android.widget.TextView[contains(@text,'信息库')]")
training_management = (By.XPATH, "//android.widget.TextView[contains(@text,'培训管理')]")
equip_instrument_ticket = (By.XPATH, "//android.widget.TextView[contains(@text,'设备仪表工单')]")
coredata = (By.XPATH, "//android.widget.TextView[contains(@text,'关键数据')]")
security_job_ticket = (By.XPATH, "//android.widget.TextView[contains(@text,'安全作业单')]")
