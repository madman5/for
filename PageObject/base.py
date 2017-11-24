# coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# import time,sys,os
# sys.path.append("..")
# from model.dirpath import Dir_path
import unittest


class Base(object):

    def __init__(self, drive, url="http://qudao.jiaofuyun.com/Home/login"):
        self.driver = drive
        self.url = url
        self.timeout = 10

    def	_open(self):
        self.driver.get(self.url)
        assert self.driver.current_url == self.url, 'Did ont land on %s' % self.url

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open()

	# 重定义获取cookies
	# def getCookie(self, cookiename):
	# 	return self.driver.get_cookie(cookiename)
	#
	#
	# def addCookies(self, cookies):
	# 	self.driver.add_cookie(cookies)
	# 	self.driver.refresh()

	# 重定义find_element方法
    def find_element(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print u"元素定位出错原因：%s" %e

	# 重定义find_element方法
    def find_elements(self, *loc):
        # 逻辑判断没写
        return self.driver.find_elements(*loc)

	# 重写获取元素文本方法
    def element_text(self, *loc):
        return self.driver.find_element(*loc).text


	# 去除一组元素的readonly属性的方法
    def removAttributes(self, num, *loc):
        try:
            js = "document.getElementsBy%s('%s')[%d].removeAttribute('readonly')" % (loc[0], loc[1], num)
            self.driver.execute_script(js)
        except Exception as msg:
            print "元素位置或JS方法错误"

	# 去除readonly属性方法
    def removAttribute(self, *loc):
        try:
            js = "document.getElementBy%d('%d').removeAttribute('readonly')" % (loc[0], loc[1])
            self.driver.execute_script(js)
        except Exception as msg:
            print "元素位置或JS方法错误"


	# 重定义click
    def click(self, *loc):
		# 逻辑判断没写
        return self.find_element(*loc).click()


	# 重定义senk_key
    def send_key(self, value, *loc):
		# 逻辑判断没写
        self.find_element(*loc).send_keys(value)

	# 重定义clear
    def clear(self,*loc):
		# 逻辑判断没写
        return self.find_element(*loc)

	# 重写显示等待until
    def webDriverWait_until(self, loc):
        return WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(*loc))

	# 重写显示等待until_not
    def webDriverWait_until_not(self, loc):
        return WebDriverWait(self.driver, 10, 0.5).until_not(EC.presence_of_element_located(*loc))

	# 重定义switch_iframe
    def switch_iframe(self, *loc):
		# 逻辑判断没写
        iframe = self.find_element(*loc)
        return self.driver.switch_to.frame(iframe)


	# 重定义switch_to.default_content方法
    def iframe_out(self):
        return self.driver.switch_to.default_content()


	# 重定义鼠标悬停方法
    def move_to_element(self, *loc):
        # 逻辑判断没写
        return ActionChains(self.driver).move_to_element(self.find_element(*loc)).perform()

 

if __name__ == "__main__":
    driver = webdriver.Chrome()
    B = Base(driver)
