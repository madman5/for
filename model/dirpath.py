# -*- coding: utf-8 -*-
import os

class Dir_path():

	##把根路径写入到path文件中并返回
	def get_path (self):
		path = os.path.dirname(os.path.realpath(__file__))
		path = os.path.dirname(path)
		filename = "%s\path.txt" % path
		try:
			f = open(filename, "wb")
			path = path.replace("\\", r"\\")
			f.write(path)
			return path
		except Exception as msg:
			print ("打开文件或写内文件内容发生错误：%s"%msg)
		finally:
			f.close()
 

	# 创建并返回目录
	def dirName(self,Folder):
		path = os.path.join(self.get_path(),Folder)
		if os.path.exists (path) == False:
			os.makedirs(path)
			print "未发现%s目录，自动创建%s目录成功" %(Folder,Folder)
		return path



	def existsfile(self,folder, filename):
		path = self.dirName(folder)
		file = os.path.join(path,filename)
		if os.path.exists(file) == False:
			print u"%s目录下无配置文件，请创建%s文件!" %(folder,filename)
			return False
		return file





if __name__ == "__main__":
	D = Dir_path()
	D.get_path()
	# print(D.dirName("Report"))
