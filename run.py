#coding:utf-8
import time, os, unittest, HTMLTestRunner, smtplib
from model import dirpath,logger, func
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


log = logger.Log()


class Resport():
	def __init__(self, start_dir="TestCase", pattern = "*_case.py"):
		self.start_dir = start_dir
		self.pattern = pattern
		self.p = dirpath.Dir_path()

	def __sendEmail(self,reportname):
		csv_date = func.getcsv()
		if csv_date == False:
			return False
		mail_receiver = csv_date['receiver']
		mail_receiver = "".join(mail_receiver)

		receiver = mail_receiver.split(";")
		port = int(csv_date['port'])
		sender = csv_date['sender']
		psw = csv_date['psw'].strip()
		server = csv_date['server'].strip()

		# 编写邮件内容
		with open(reportname, mode = 'rb') as fh:
			mail_body = fh.read()

		msg = MIMEMultipart()
		msg['from'] = sender
		msg['to'] = ";".join(receiver)
		msg['subject'] = csv_date['subject'].decode('gbk')
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
			smtp.connect(server)
			smtp.login(sender, psw)
		except:
			smtp = smtplib.SMTP_SSL(server, 465)
			smtp.login(sender, psw)
		smtp.sendmail(sender, receiver, msg.as_string())
		smtp.quit()

	# 测试用例批量加载
	def __suites(self):
		log.info (u"--------------------------- START ---------------------------")
		casedir = os.path.join(self.p.get_path(), "TestCase")
		discover = unittest.defaultTestLoader.discover(start_dir = casedir, pattern = self.pattern, top_level_dir = None)
		return discover

	# 执行用例并发送测试报告
	def report(self):
		now_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
		reportdir = self.p.dirName("Report")
		reportname = "%s\\%s.html" % (reportdir, now_time)
		f = open(reportname, "wb")
		runner = HTMLTestRunner.HTMLTestRunner(stream = f, title = u"自动化测试报告", description = u"用例执行情况:", verbosity = 2)
		runner.run(self.__suites())
		log.info(u"--------------------------- END ---------------------------") 
		f.close()
		self.__sendEmail(reportname)


if __name__ == "__main__":
	r = Resport()
	r.report()
	# r.suites()