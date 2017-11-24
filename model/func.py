#coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,sys,os,csv
sys.path.append("..")
from model.dirpath import Dir_path

p = Dir_path()

# 截图
def getscreen(driver):
    filepath = p.dirName("screenshot")
    filename = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    filename = os.path.join(filepath, "%s.jpg" % filename)
    return driver.get_screenshot_as_file(filename)

# 获取文件date.csv中邮箱配置
def getcsv():
    path = p.dirName("Date")
    filename = os.path.join(path,"date.csv")

    with open(filename, mode = 'rb') as f:
        csv_reader = csv.reader(f)
        for i in csv_reader:
            pass
    if len(i) == 3 :
        a = ','.join(i).split(',')
        # print tuple(a)
        return tuple(a)

if __name__ == '__main__':
    # getscreen(1)
    print getcsv()