#coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 重写显示等待until
def webDriverWait_until(self, timeout = 10, poll = 0.5, *loc):
	return WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located(*loc))


# 重写显示等待until_not
def webDriverWait_until_not(self, timeout = 10, poll = 0.5, *loc):
	return WebDriverWait(self.driver, timeout, poll).until_not(EC.presence_of_element_located(*loc))