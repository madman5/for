# coding:utf-8
import sys, time, unittest,ddt
sys.path.append("..")
from PageObject.login_page import LoginPage
from model.driver import brower
from model import logger,func

log = logger.Log()
test_err = func.getexcel('jfy.xlsx','login_error')

@ddt.ddt
class LoginTest(unittest.TestCase):
	def setUp(self):
		self.driver = brower("chrome")
		self.driver.maximize_window()
		time.sleep(2)
		self.p = LoginPage(self.driver)



	@ddt.data(*test_err)
	def test_login(self,data):
		log.info(u"--------------------登录用例-------------------------------------------")
		self.p.login_action(data['username'], data['password'])
		try:
			self.assertEqual(self.p.login_asser(data['method'],data['loc']), data['result'])
			log.info(u"用例：test_login---NO.:%s ，断言通过" % (data['NO.']))
		except Exception as e:
			log.info(u"用例：test_login---NO.:%s ,断言失败的原因：%s" % (data['NO.'],e))
			func.getscreen(self.driver)

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()