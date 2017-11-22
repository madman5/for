# coding:utf-8
import os, sys, logging, time
sys.path.append('..')
from model.dirpath import Dir_path

p = Dir_path()
path = p.getpath()
log_path = os.path.join(path,'Report')

class Log():
	def __init__(self):
		self.log_name = os.path.join(log_path, ('%s.log') % time.strftime('%Y_%m_%d'))	 # 日志名称

		self.logger = logging.getLogger()    # 第一步，创建一个logger 记录器
		self.logger.setLevel(logging.DEBUG)  # Log等级总开关
		self.formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")  # 定义日志输出格式

	def __console(self, level, message):
		fh = logging.FileHandler(self.log_name, mode = 'a')	 	# 创建一个FileHandler，用于写入到本地文件
		fh.setLevel(logging.DEBUG) 		# 写入文件的日志级别
		fh.setFormatter(self.formatter)
		self.logger.addHandler(fh) 		# 第五步，将fh添加到logger记录器里面


		ch = logging.StreamHandler()	 # 创建一个StreamHandler,用于输出到控制台
		ch.setLevel(logging.DEBUG)
		ch.setFormatter(self.formatter)
		self.logger.addHandler(ch)

		# 日志输入级别判断
		if level == 'debug':
			self.logger.debug(message)
		elif level == 'info':
			self.logger.info(message)
		elif level == 'warning':
			self.logger.warning(message)
		else:
			self.logger.error(message)

		# 这两行代码是为了避免日志输出重复问题
		self.logger.removeHandler(fh)
		self.logger.removeHandler(ch)

		fh.close()


	def debug(self, message):
		self.__console('debug', message)

	def info(self, message):
		self.__console('info', message)

	def warning(self, message):
		self.__console('warning', message)

	def error(self, message):
		self.__console('error', message)


if __name__ == "__main__":
	log = Log()
	log.info('测试开始')
	log.debug('测试调试')
	log.warning('测试警告')
	log.error('测试错误')
	log.info('测试结束')