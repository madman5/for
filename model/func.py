#coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,sys,os
sys.path.append("..")
from model.dirpath import Dir_path

# 重写显示等待until
def webDriverWait_until(timeout = 10, poll = 0.5, *loc):
    return WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located(*loc))


# 重写显示等待until_not
def webDriverWait_until_not(self, timeout = 10, poll = 0.5, *loc):
    return WebDriverWait(self.driver, timeout, poll).until_not(EC.presence_of_element_located(*loc))

def getscreen(driver):
    filename = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    p = Dir_path()
    filepath = p.dirName("screenshot")
    filename = os.path.join(filepath, "%s.jpg" % filename)
    return driver.get_screenshot_as_file(filename)

if __name__ == '__main__':
    getscreen(1)