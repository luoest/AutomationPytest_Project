from selenium import webdriver
from utilities.mylog import *

class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getBrowserInstance(self, url):
        if self.browser.lower() == 'Edge':
            driver = webdriver.Edge()
        elif self.browser.lower() == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        msg = '本次操作使用的浏览器是：{}, 获取网址：{}'.format(self.browser, url)
        print(msg)
        logging.info(msg)

        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(url)

        return driver
