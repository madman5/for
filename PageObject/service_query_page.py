#coding:utf-8
'''
	服务管理页面---习网管理员
'''

from PageObject.base import Base
from model import driver   #用来与__name__配合调试测
import time
from PageObject.navigation_loc import Nav

class QueryPage(Base):

	iframe_loc=("css selector","[name='/Home/Desktop']")
	query_service_loc=("css selector","[placeholder='请输入服务名称']")
	query_sp_loc=("css selector","[placeholder='请输入商品名称']")
	query_school_loc=("css selector","[placeholder='请选择学段']")
	query_dj_loc=("css selector","[placeholder='请选择定价类型']")
	query_sj_loc=("css selector","[placeholder='请输入商家名称']")
	query_qd_loc=("css selector","[placeholder='请输入渠道商名称']")
	query_server_state_loc=("css selector","[placeholder='请输入服务状态']")
	query_book_loc=("name","IsExam")    #只看含有考试用书的服务

	readonly_loc=("class name","validatebox-readonly")	#去除下拉列表的readonly属性
	query_loc=("id","lbtnSearch")  #查询按钮
	clean_query_loc=("id","lbtnDelClearSelect")
	derive_loc=("id","lbtnToExcel")


	# 输入服务名称
	def serviceName(self,sname):
		self.send_key(sname,*self.query_service_loc)

	# 输入商品名称
	def shopName(self,shName):
		self.send_key(shName,*self.query_sp_loc)

	#输入学段
	def xueDuan(self,xd):
		self.send_key(xd,*self.query_school_loc)

	#定价类型
	def priceType(self,priceT):
		self.send_key(priceT,*self.query_dj_loc)

	# 商家名称
	def sjName(self,sjname):
		self.send_key(sjname,*self.query_sj_loc)

	#渠道名称
	def qdName(self,qdname):
		self.send_key(qdname,*self.query_qd_loc)

	# 服务状态
	def serverT(self,servert):
		self.send_key(servert,*self.query_qd_loc)

	# 只查看含有考试用书的服务
	def ksBook(self):
		self.click(*self.query_book_loc)

	#点击查询
	def query(self):
		self.click(*self.query_loc)

	#清除查询条件
	def cleanQuery(self):
		self.click(*self.clean_query_loc)

	#导出
	def derive(self):
		self.click(*self.derive_loc)

if __name__=="__main__":

	c={u'domain': u'.jiaofuyun.com',
	   u'secure': False,
	   u'value': u'565FC6AC56192E8833943CEA31A7DE3F990FE3B1D0D50AACCA81F45628B265FD7B822D1A787246A42CB58338A0A9C29B65C6CD13B291DDD5A2ED86EFB5C8FBCAA366195A8AC5A0F41270EC6497148B4C4FB491603A2655ECB1B49842BDDFFFD63DDCD9614E5185F234DC879952777084251244F4D98084D4AE870FFBC2BC649380BB853954D8EB2DB21B10257CAFEC1A698EF5333F60FD86E68022D8F5FDCE415FFA3ED03202A56FEBFE56A152A5BC6CF7ED79DEF430EC8A20E95DD592E138ECDB81C616E6A2CA91443382DA4E8FB90E86075A8225A5C4C4154B8F5CEA9DD59796BB07D3E2AB2BAB387577D3513B1E5D',
	   u'expiry':1500289643.429064,
	   u'path': u'/',
	   u'httpOnly': False,
	   u'name': u'jfy'}

	driver = driver.brower()
	query=QueryPage(driver)
	query.open()
	query.addCookies(c)
	time.sleep(3)
	query.click(*Nav.nav_service_loc)
	time.sleep(2)
	query.click(*Nav.nav_service_level_loc)
	time.sleep(3)

	driver.quit()






















