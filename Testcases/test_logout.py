from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import Config
from Locators.login_page_locators import LoginPage
from Locators.logout_page_locators import LogoutPage
import time

def test_logout(driver):
    login_page = LoginPage(driver)

    # 1) Login
    login_page.login_test(Config.valid_email, Config.valid_password)

    # 2) Confirm dashboard is visible
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Config.dashboard))
    assert login_page.is_dashboard_displayed(), "Login failed: Dashboard not displayed"
    time.sleep(2)

    # 3) Logout
    logout_page = LogoutPage(driver)
    logout_page.logout()
    time.sleep(2)

    # 4) Confirm returned to login page
    assert logout_page.is_login_displayed(), "Logout failed: Login page not displayed"