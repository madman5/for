# coding:utf-8
from appium import webdriver
import time

desired_cap = {
	'platformName': 'Android',	# android或ios
	'deviceName': '127.0.0.1:62001',	# 设备名称，通过adb devices查看  A1UACN7NFMB9 
	'platformVersion': '4.4.2',	# 安卓的系统版本号
	'appPackage': 'com.taobao.taobao',	# apk的包名称
	'appActivity': 'com.taobao.tao.welcome.Welcome',	# apk的launcherActivity名
	'unicodeKeyboard': True,	# 使用unicode编码方式发送字符串
	'restKeyboard': True 	# 将键盘隐藏起来
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
time.sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
time.sleep(3)
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys(u'测试部落')
time.sleep(3)
driver.quit()