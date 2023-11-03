import os


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--env", default="UAT")

@pytest.fixture(autouse=True, scope="class")
def setUp(request):

    global driver
    browser = request.config.getoption("--browser")

    env = request.config.getoption("--env")

    # browser = request.param
    # print(browser)
    if browser == "chrome":
        print(browser + " is started")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "C:\\old data\\chrome-win64\\chrome.exe"

        # SeleniumManager.driver_location("chrome")
        driver = webdriver.Chrome(options=chrome_options,
                                  service=Service("\\XelpmocTest\\venv\\Scripts\\chromedriver.exe"))
        driver.maximize_window()
        driver.get("https://trytestingthis.netlify.app/")
        driver.delete_cookie(browser)
        driver.implicitly_wait(3.2)


    elif browser == "firefox":
        path = os.getcwd()
        list_path = list(path)

        fp = webdriver.FirefoxOptions()
        driver=webdriver.Firefox()
        driver.get("https://trytestingthis.netlify.app/")

    request.cls.driver = driver
    yield
    driver.quit()