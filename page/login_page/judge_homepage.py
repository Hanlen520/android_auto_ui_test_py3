# app打开后分成4种情况
# ①安装完成后的第一次打开，弹出输入选择服务器输入code页面
# ②打开app后，在输入用户名和密码页面
# ③打开app后，已经登录进去的页面(首页)
# ④长时间不使用app，会弹出类似选择服务器输入code的页面

usercode_first = "com.gongzhidao.inroad:id/input_code_numbers_layout"  # 情形①
usercode_after_long_time = "//android.widget.TextView[contains(@text,'请输入客户代码')]"  # 情形④
