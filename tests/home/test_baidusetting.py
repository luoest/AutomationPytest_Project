import unittest
import pytest
from pages.home.baidusetting import BaiduSetting
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp")
class BaiduSettingTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.bSet = BaiduSetting(self.driver)
        self.ts = TestStatus()

    def test_baiduSetting(self):
        self.bSet.performBaiduSetting()
        result = self.bSet.veryfyAlertTextMatchAndAccept('已经记录下您的使用偏好')
        self.ts.setCaseFinal('BaiduSettingTests', result, 'BaiduSettingTests测试完成。')
