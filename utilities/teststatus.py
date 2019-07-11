from utilities.mylog import *

class TestStatus():
    result_list = []
    def setResult(self, result, resultMessage):
        if result:
            self.result_list.append('成功')
            msg = '本次步骤执行结果：{}， {}。'.format(result, resultMessage)
            print(msg)
            logging.info(msg)
        else:
            self.result_list.append('失败')
            msg = '本次步骤执行结果：{}， {}。'.format(result, resultMessage)
            print(msg)
            logging.info(msg)

    def setCaseSteps(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def setCaseFinal(self, testCase, result, resultMessage):
        self.setResult(result, resultMessage)
        if '失败' in self.result_list:
            msg = '》》》》》用例：“{}”执行失败。步骤信息：“{}”，{}'.format(testCase, self.result_list, resultMessage)
            print(msg)
            logging.info(msg)
            self.result_list.clear()
            assert True == False
        else:
            msg = '>>>>>>>>>> 用例：“{}”执行成功。步骤信息：“{}”，{}'.format(testCase, self.result_list, resultMessage)
            print(msg)
            logging.info(msg)
            self.result_list.clear()
            assert True == True
