#coding:utf-8
import time, os, unittest, HTMLTestRunner
from model import dirpath,logger

log = logger.Log()

class Resport():

	def __init__(self, start_dir="TestCase", pattern = "*_case.py"):
		self.start_dir = start_dir
		self.pattern = pattern
		self.p = dirpath.Dir_path()



	# 测试用例批量加载到suites中
	def testSuites(self):
		log.info (u"-------开始---------")
		casedir = os.path.join(self.p.getpath(), "TestCase")
		discover = unittest.defaultTestLoader.discover(start_dir = casedir, pattern = self.pattern, top_level_dir = None)

		return discover

	# 测试报告
	def report(self, title = u"自动化测试报告", description = u"用例执行情况:", rname = "Report"):

		now_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())

		# 创建并获取Report的目录地址
		reportdir = self.p.dirName(rname)

		# 拼接report文件名称
		reportname = "%s\\%s.html" % (reportdir, now_time)

		f = open(reportname, "wb")

		runner = HTMLTestRunner.HTMLTestRunner(stream = f, title = title, description = description, verbosity = 2, retry = 1)
		if runner.run(self.testSuites()):
			log.info(u"-------登录用例执行完成-------") 
		f.close()




if __name__ == "__main__":
	r = Resport()
	r.report()