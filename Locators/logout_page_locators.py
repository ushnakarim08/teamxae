from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.profile = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/header/div/div/div[2]/div[2]/button/h5")
        self.logout_btn = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/header/div/div/div[2]/div[2]/div/ul/li[2]/div")

        # Login page element (proves we are logged out)
        self.email = (By.ID, "email")

    def logout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.profile)).click()
        time.sleep(2)
        wait.until(EC.element_to_be_clickable(self.logout_btn)).click()

    def is_login_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.email)
            )
            return True
        except Exception:
            return False

