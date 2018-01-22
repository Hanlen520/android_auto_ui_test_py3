from appium.webdriver.common.mobileby import By

# 罗列登录页面上的元素

username = (By.ID, "com.gongzhidao.inroad:id/shouji_edit")  # 用户名输入框
password = (By.ID, "com.gongzhidao.inroad:id/passwd_edit")  # 密码输入框
login_button = (By.ID, "com.gongzhidao.inroad:id/login_login")  # 登录按钮
register = (By.ID, "com.gongzhidao.inroad:id/register")  # 立即注册按钮
forget_password = (By.ID, "com.gongzhidao.inroad:id/forget_passwd")  # 忘记密码按钮
choose_server = (By.ID, "com.gongzhidao.inroad:id/setting")  # 设置（选择服务器按钮）
