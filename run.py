#coding:utf-8
import time, os, unittest, HTMLTestRunner, smtplib
from model import dirpath,logger 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

log = logger.Log()

class Resport():

	def __init__(self, start_dir="TestCase", pattern = "*_case.py"):
		self.start_dir = start_dir
		self.pattern = pattern
		self.p = dirpath.Dir_path()

	def sendEmail(self, filename, mail_sender, mail_psw, mail_receiver, mail_subject, mail_server, mail_port):
		# 编写邮件内容
		with open(filename, mode = 'rb') as fh:
			mail_body = fh.read()
		msg = MIMEMultipart()
		msg['from'] = mail_sender
		msg['to'] = ";".join(mail_receiver)
		msg['subject'] = mail_subject
		body = MIMEText(mail_body, "html", "utf-8")
		msg.attach(body)
		#附件
		att = MIMEText(mail_body, "base64", "utf-8")
		att["Content-Type"] = "application/octet-stream"
		att["Content-Disposition"] = 'attachment;filename = "test_report.html"'
		msg.attach(att)
		# 发送邮件
		try:
			smtp = smtplib.SMTP()
			smtp.connect(mail_server)
			smtp.login(mail_sender, mail_psw)
		except:
			smtp = smtplib.SMTP_SSL(mail_server, mail_port)
			smtp.login(mail_sender, mail_psw)
		smtp.sendmail(mail_sender, mail_receiver, msg.as_string())
		smtp.quit()


	# 测试用例批量加载到suites中
	def testSuites(self):
		log.info (u"--------------------------- START ---------------------------")
		casedir = os.path.join(self.p.getpath(), "TestCase")
		discover = unittest.defaultTestLoader.discover(start_dir = casedir, pattern = self.pattern, top_level_dir = None)
		return discover
		# runner = unittest.TextTestRunner()
		# runner.run(discover)



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
	# r.testSuites()