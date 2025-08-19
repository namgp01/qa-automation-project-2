import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="class")
def setup(request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "16.0"
    options.device_name = "TestPhone"
    options.automation_name = "UiAutomator2"
    options.app_package = ""
    options.app_activity = ""
    options.no_reset = True

    driver = webdriver.Remote("http://localhost:4723", options=options)

    driver.implicitly_wait(10)

    request.cls.driver = driver

    yield driver

    driver.quit()