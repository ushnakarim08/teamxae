from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import Config
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Safer than By.ID (because your page didn't find id="email")
        self.email_field = (By.CSS_SELECTOR, "input[type='email']")
        self.password_field = (By.CSS_SELECTOR, "input[type='password']")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        self.driver.get(Config.base_url)

    def login_test(self, email, password):
        self.open()
        wait = WebDriverWait(self.driver, 15)

        email_el = wait.until(EC.visibility_of_element_located(self.email_field))
        email_el.clear()
        email_el.send_keys(email)
        time.sleep(2)

        pass_el = wait.until(EC.visibility_of_element_located(self.password_field))
        pass_el.clear()
        pass_el.send_keys(password)
        time.sleep(2)

        wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def is_dashboard_displayed(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(Config.dashboard)
            )
            return True
        except Exception:
            return False
