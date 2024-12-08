import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

driver=None

@pytest.fixture(scope='class')
def setup(request):

    options=Options()
    options.add_argument("--headless")

    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome(executable_path= r'C:\shetty\chromedriver-win32\chromedriver.exe')
    elif browser_name=="EDGE":
        driver = webdriver.Edge(executable_path=r'C:\fire\msedgedriver.exe')

    driver.get('https://qa.unifytwin.com')
    request.cls.driver=driver
    driver.maximize_window()
    yield
    driver.close()

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)

