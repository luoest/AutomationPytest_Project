from base.seleniumdriver import SeleniumDriver

class BaiduSearch(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchBoxLoc = ('id', 'kw')
    _submitBtnLoc = ('id', 'su')

    def clearSearchBox(self):
        self.getClear(*self._searchBoxLoc)

    def enterSearchBox(self, keyword):
        self.getSendKeys(*self._searchBoxLoc, keyword)

    def submit(self):
        self.getClick(*self._submitBtnLoc)

    def performSearch(self, keyword):
        self.clearSearchBox()
        self.enterSearchBox(keyword)
        self.submit()

    def veryfyTitleHas(self, element, seconds = 0):
        return self.getAssertElementInTitle(element, seconds)

    def veryfyTitleEqual(self, expected, seconds = 0):
        return self.getAssertTitleEqual(expected, seconds)

    def veryfySearchSuccessful(self, locType, loc):
        return self.getIsElementPresent(locType, loc)
