from selenium import webdriver

def brower(brow = "chrome"):
    try:
        if brow == "chrome":
            driver = webdriver.Chrome()
            return driver
        elif brow == "ie":
            driver = webdriver.Ie()
            return driver
        elif brow == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif brow == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        else:
            print "Not found this browser,You can enter 'firefox', 'chrome', 'ie' or 'phantomjs'"
    except Exception as msg:
        print "%s" % msg

if __name__ == "__main__":
	brower("phantomjs")