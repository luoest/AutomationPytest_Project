import unittest
import pytest
from pages.home.baidusearch import BaiduSearch
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures('oneTimeSetUp')
class BaiduSearchTests(unittest.TestCase):
    '''
    terminal中执行，命令中加上： --browser chrome(或者Firefox，edge)
    生成HTML报告， 命令中加上： --html=report.html
    '''
    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.bs = BaiduSearch(self.driver)
        self.ts = TestStatus()

    def test_search(self):
        self.bs.performSearch('python')
        titleResult = self.bs.veryfyTitleHas('python', 1)
        self.ts.setCaseSteps(titleResult, 'test_search veryfyTitleHas: python')

        searchResult = self.bs.veryfySearchSuccessful('partial link text', 'python')
        self.ts.setCaseFinal('test_search', searchResult, 'test_search 全部执行结束。')

