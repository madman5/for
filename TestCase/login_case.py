# coding:utf-8
import sys, time, unittest
sys.path.append("..")
from PageObject.login_page import LoginPage
from model.driver import brower
from model import logger




class LoginTest(unittest.TestCase):
	def setUp(self):
		self.driver = brower("chrome")
		self.driver.maximize_window()
		time.sleep(2)
		self.p = LoginPage(self.driver)

	def test_login_user_pwd_null(self):
		log = logger.Log()
		log.debug(u"-------密码为空，登录失败-------")
		self.p.login_action("", "qijing")
		time.sleep(2)

	
	def test_login_user_pwd(self):
		self.p.login_action('98556', 'qijing')
		time.sleep(2)
		# self.assertIn("22", u"齐晶")


	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()