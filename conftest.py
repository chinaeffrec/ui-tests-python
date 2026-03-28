import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


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