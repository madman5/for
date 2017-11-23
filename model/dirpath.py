# -*- coding: utf-8 -*-
import os

class Dir_path():

	##把根路径写入到path文件中
	def get_path (self):
		path = os.path.dirname(os.path.realpath(__file__))
		path = os.path.dirname(path)
		filename = "%s\path.txt" % path

		f = open(filename, "wb")
		try:
			path = path.replace("\\", r"\\")
			f.write(path)
			return path
		except Exception as msg:
			print ("打开文件或写内文件内容发生错误：%s"%msg)
		f.close()
 
	def getpath(self):
		# 获取path.txt的绝对路径
		path = os.path.dirname(os.path.dirname (os.path.realpath (__file__)))
		patht = os.path.join(path, "path.txt")

		if os.path.exists(patht) == False:
			self.get_path()
		f = open(patht)
		p = str(f.readlines()[0])

		if p not in os.getcwd():
			p = self.get_path()

		f.close()
		return p

	# 创建并返回目录
	def dirName(self,Folder):
		f = os.path.join(self.getpath(),Folder)
		if os.path.exists (f) == False:
			os.makedirs(f)
			print "未发现%s目录，自动创建%s目录成功" %(Folder,Folder)
		return f



if __name__ == "__main__":
	D = Dir_path()
	D.getpath()
	# print(D.dirName("Resport"))
