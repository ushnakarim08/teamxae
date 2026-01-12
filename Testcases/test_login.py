import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
from Config.config import Config
from Locators.login_page_locators import LoginPage

@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(3)
    login_page.login_test(Config.valid_email, Config.valid_password)
    time.sleep(3)
    assert login_page.is_dashboard_displayed(), "Valid login passed: Dashboard was displayed"


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(5)
    login_page.login_test(Config.invalid_email, Config.invalid_password)
    time.sleep(5)
    assert not login_page.is_dashboard_displayed(), "Invalid login passed: Dashboard not displayed"