import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.yield_fixture(scope='class')
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getBrowserInstance('https://www.baidu.com')
    if request.cls is not None:
        request.cls.driver = driver

    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('browser')
