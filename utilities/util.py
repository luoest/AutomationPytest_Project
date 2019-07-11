

class Util():
    '''
    用于判断实际字符与预期的字符是否完全相符
    '''
    def isTextMatch(self, actual, expected):
        if actual.lower() == expected.lower():
            return True
        else:
            return False
