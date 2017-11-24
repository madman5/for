# coding:utf-8
import sys, time, unittest
sys.path.append("..")
from PageObject.login_page import LoginPage
from model.driver import brower
from model import logger,func

log = logger.Log()



class LoginTest(unittest.TestCase):
	def setUp(self):
		self.driver = brower("chrome")
		self.driver.maximize_window()
		time.sleep(2)
		self.p = LoginPage(self.driver)

	# def test_login_user_pwd_null(self):
	# 	log.info(u"----- 用例 (test_login_user_pwd_null)：密码为空，登录失败")
	# 	self.p.login_action("98556", "")
	# 	try:
	# 		self.assertEqual(self.p.login_error_info(), u"登录")
	# 	except Exception as e:
	# 		print u"断言失败的原因：%s" % e
	# 		func.getscreen(self.driver)
	
	def test_login_user_pwd(self):
		print "0"
		log.info(u"----- 用例 (test_login_user_pwd)：用户名密码正确，成功登录")
		self.p.login_action('98557', 'qijing')
		time.sleep(2)
		print "1"
		try:
			print "2"
			self.assertEqual(self.p.login_success_info(), "98556")
		except Exception as e:
			print u"断言失败的原因：%s" % e
			func.getscreen(self.driver)




	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()