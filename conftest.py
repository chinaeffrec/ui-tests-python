import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    driver = item.funcargs.get("driver", None)

    if rep.when == "call" and rep.failed and driver:
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
