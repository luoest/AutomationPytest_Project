from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from utilities.util import Util
from utilities.mylog import *
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDriver():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.locDict = {'id': By.ID,
                        'link text': By.LINK_TEXT,
                        'partial link text': By.PARTIAL_LINK_TEXT,
                        'css': By.CSS_SELECTOR}
        self.util = Util()

    def getHightLightElement(self, element):
        # 高亮显示正在操作的元素
        self.driver.execute_script('arguments[0].setAttribute("style", arguments[1]);', element,
                                   'background: yellow; border: 2px solid red;')

    def getFindElement(self, locType, loc):
        # 获取并返回目标元素。
        try:
            if locType.lower() in self.locDict:
                element = self.wait.until(lambda driver: driver.find_element(self.locDict[locType.lower()], loc))
                msg = '发现目标元素，定位方式：{}， 定位器：{}'.format(locType, loc)
                print(msg)
                logging.info(msg)
                self.getHightLightElement(element)
                return element
            else:
                msg = '没有发现定位方式“{}”和定位器“{}”指向的目标元素。'.format(locType, loc)
                print(msg)
                logging.info(msg)
        except:
            msg = "没有发现目标元素，请确认定位方式或者定位器是否正确。"
            print(msg)
            logging.debug(msg)

    def getClear(self, locType, loc):
        # 执行清空操作
        try:
            self.getFindElement(locType, loc).clear()
            msg = '执行清空操作。'
            print(msg)
            logging.info(msg)
        except Exception as e:
            print(e)

    def getSendKeys(self, locType, loc, value):
        # 发送信息到目标元素。
        try:
            self.getFindElement(locType, loc).send_keys(value)
            msg = '发送信息：{}。'.format(value)
            print(msg)
            logging.info(msg)
        except Exception as e:
            print(e)

    def getClick(self, locType, loc):
        # 执行点击操作
        try:
            self.getFindElement(locType, loc).click()
            msg = '执行点击操作。'
            print(msg)
            logging.info(msg)
        except Exception as e:
            print(e)

    def getSleep(self, sleepSeconds):
        # 设置等待时间， 输入整数或者浮点数
        msg = '等待时间：{}'.format(sleepSeconds)
        print(msg)
        logging.info(msg)
        sleep(sleepSeconds)

    def getTitle(self):
        # 获取当前页面的标题
        msg = '获取页面标题'
        print(msg)
        logging.info(msg)
        try:
            return self.driver.title
        except Exception as e:
            print(e)

    def getAssertElementInTitle(self, element, seconds = 0):
        # 查看页面标题中是否含有指定元素。
        self.getSleep(seconds)
        msg = '查看页面标题中是否有元素：' + str(element)
        logging.info(msg)
        print(msg)
        try:
            assert str(element) in self.getTitle(), '页面标题中没有元素：' + str(element)
            return True
        except Exception as e:
            print(e)
            return False

    def getAssertTitleEqual(self, expected, seconds = 0):
        self.getSleep(seconds)
        try:
            actual = self.getTitle()
            msg = '查看页面实际标题“{}”是否与预期“{}”相符:'.format(actual, expected)
            print(msg)
            logging.info(msg)
            return self.util.isTextMatch(actual, expected)
        except Exception as e:
            print(e)

    def getIsElementPresent(self, locType, loc):
        msg = '查看页面代码中是否出现目标元素。'
        print(msg)
        logging.info(msg)
        try:
            element = self.getFindElement(locType, loc)
            if element is not None:
                if element:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

    def getAlert(self):
        try:
            alertResult = self.wait.until(EC.alert_is_present())
            if alertResult:
                return alertResult
            else:
                return False
        except:
            print('未发现弹窗，或者弹窗未在设定的时间内弹出。')
            return False

    def getClose(self):
        msg = '关闭浏览器。'
        print(msg)
        logging.info(msg)
        try:
            self.driver.quit()
        except Exception as e:
            print(e)



















