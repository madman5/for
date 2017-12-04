#coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,sys,os,csv
import xlrd
sys.path.append("..")
from model.dirpath import Dir_path

p = Dir_path()

# 截图
def getscreen(driver):
    filepath = p.dirName("screenshot")
    filename = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    filename = os.path.join(filepath, "%s.jpg" % filename)
    driver.get_screenshot_as_file(filename)
    print u"已保存运行错误界面截图：%s" % filename
    return filename

# 获取文件date.csv中邮箱配置
def getcsv():
	filename = p.existsfile('Date', 'date.csv')
	if filename == False:
		return False
	try:
		with open(filename,'rb') as f:
			csv_reader = csv.reader(f)
			for data in csv_reader:pass
			email_info = data[0:5]
			email_recivew = data[5:6]
			email_info.append(email_recivew)
			csv_keys = ['sender', 'psw', 'server', 'port', 'subject', 'receiver']
			csv_date = dict(zip(csv_keys,email_info)) 
			return csv_date
	except:
		print u"请填写邮件相关信息!"


def getexcel(table,sheet):
	filename = p.existsfile('Date', table)
	f = xlrd.open_workbook(filename)
	table = f.sheet_by_name(sheet)

	keys = table.row_values(0)	# 表格标题
	# nrows = table.nrows		# 总行数	
	# ncols = table.ncols		# 总列数

	if table.nrows <= 1:
		print (u"总行数小于1")
	else:
		date = []
		j = 1
		for i in range(table.nrows - 1):
			y = {}
			for x in range(table.ncols):
				value = table.row_values(j)
				if type(value[x]) == float:
					value = str(int(value[x]))
					y[keys[x]] = value
				else:
					value = value[x].strip()
					y[keys[x]] = value
			if y['loc'] == "" or y['method'] == "":
				print u"method和loc项不能为空！"
			print y['result']
			j += 1
			date.append(y)
		return date


if __name__ == '__main__':
	# getscreen(1)
	# getcsv()
	getexcel('jfy.xlsx','login_error')