from Config.config import Config
from Locators.login_page_locators import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login_test(Config.valid_email, Config.valid_password)
    assert login_page.is_dashboard_displayed(), "Valid login FAILED: Dashboard not displayed"

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login_test(Config.invalid_email, Config.invalid_password)
    assert not login_page.is_dashboard_displayed(), "Invalid login FAILED: Dashboard displayed"