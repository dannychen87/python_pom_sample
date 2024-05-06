import allure
import pytest
from jproperties import Properties

from common.config_factory import ConfigFactory
from common.driver_factory import DriverFactory
from page_object.login_sample_page import LoginSamplePage


@pytest.fixture(scope='module')
def driver(request):
    def quit_driver():
        driver.quit()

    request.addfinalizer(quit_driver)
    driver = DriverFactory().get_driver()
    config = ConfigFactory()
    return driver, config


@pytest.fixture(scope='module')
def login(request, driver):
    sp = LoginSamplePage(driver)
    username, password = request.param['username'], request.param['password']
    sp.login(username, password)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Add screenshot of failed cases to allure report
    :param item:
    :param call:
    :return:
    """
    out = yield
    report = out.get_result()

    if report.when == "call":
        # Get all test cases with failure result
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            if 'driver' in item.fixturenames:
                web_driver = item.funcargs['driver']
                with allure.step("Add Failed Screenshot"):
                    allure.attach(web_driver.get_screenshot_as_png(), "Failure Screenshot", allure.attachment_type.PNG)


def pytest_metadata(metadata):
    """
    Access metadata by hook method: pytest_metadata and fixture: metadata
    then modify environment.properties by jproperties library for info to Allure report
    :param metadata: a fixture collected all metadata from pytest
    :return:
    """
    with open("./environment.properties", "r+b") as f:
        env = Properties()
        env.load(f, "utf-8")
        env['Platform'] = metadata['Platform']
        env['Python'] = metadata['Python']
        env['Pytest'] = metadata['Packages']['pytest']
        env['Allure'] = metadata['Plugins']['allure-pytest']

        f.seek(0)
        f.truncate(0)
        env.store(f, encoding='utf-8', timestamp=False)
