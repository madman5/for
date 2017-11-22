#coding:utf-8

'''
	登录页面
'''
import sys
sys.path.append('..')
from PageObject import base
from model import driver   #用来与__name__配合调试测
import time


class LoginPage(base.Base):
	login_name_loc = ("name", "userName")
	login_pwd_loc = ("name", "userPass")
	login_submit_loc = ("css selector", "button[type='submit']")
	login_homepage_loc = ("link text", "公司首页")
	login_market_loc = ("link text", "批发市场")
	login_error_loc = ("class name", "#form > ul > li.l-keep > span:nth-child(2)")
	login_succeed_loc = ("class name", "banner")

	# 输入用户名
	def login_username(self,username):
		self.clear(*self.login_name_loc)
		self.send_key(username,*self.login_name_loc)


	# 输入密码
	def login_password(self,pwd):
		self.clear(*self.login_pwd_loc)
		self.send_key(pwd,*self.login_pwd_loc)

	# 点击登录
	def login_submit(self):
		self.click(*self.login_submit_loc)

	# 登录错误提示
	def login_error_info(self):
		return self.element_text(*self.login_error_loc)

	# 点击公司首页
	def login_homepage(self):
		self.click(*self.login_homepage_loc)

	# 点击批发市场
	def login_mark(self):
		self.click(*self.login_market_loc)

	#登录方法
	def login_action(self,username,userpwd):
		self.open()
		self.login_username(username)
		self.login_password(userpwd)
		self.login_submit()

if __name__ == "__main__":
	driver = driver.brower()
	Login = LoginPage(driver)
	Login.open()
	Login.login_action("98556","qijing")
	driver.quit()




