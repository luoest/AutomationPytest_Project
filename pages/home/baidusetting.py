from base.seleniumdriver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains

class BaiduSetting(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _settingLoc = ('link text', '设置')
    _searchLoc = ('css', '.setpref')
    _saveSetLoc = ('css', '.prefpanelgo')
    def actionOnElement(self):
        element = self.getFindElement(*self._settingLoc)
        ActionChains(self.driver).move_to_element(element).perform()

    def searchSetting(self):
        self.getClick(*self._searchLoc)

    def saveSetting(self):
        self.getClick(*self._saveSetLoc)

    def performBaiduSetting(self):
        self.actionOnElement()
        self.searchSetting()
        self.getSleep(1)
        self.saveSetting()

    def veryfyAlertTextMatchAndAccept(self, expected):
        alert = self.getAlert()
        if alert:
            actualAlertText = alert.text
            result = self.util.isTextMatch(actualAlertText, expected)
            if result:
                alert.accept()
                msg = '点选弹窗“确认”选项'
                print(msg)
            return result
        return alert

if __name__ == '__main__':
    try:
        from base.webdriverfactory import WebDriverFactory
        wdf = WebDriverFactory('chrome')
        driver = wdf.getBrowserInstance('https://www.baidu.com')
        bs = BaiduSetting(driver)
        bs.performBaiduSetting()
        result = bs.veryfyAlertTextMatchAndAccept('已经记录下您的使用偏好')
        msg = ('实际弹窗信息与提供的弹窗信息是否相符：{}'.format(result))
        print(msg)
    finally:
        bs.getClose()
