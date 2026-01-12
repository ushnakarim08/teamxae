import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Config.config import Config
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self):
        self.driver.get(Config.base_url)

    def login_test(self, email, password):
        # self.driver.find_element(*self.email_field).send_keys("abc")
        # time.sleep(2)
        # self.driver.find_element(*self.email_field).clear()
        # time.sleep(2)
        self.driver.find_element(*self.email_field).send_keys(email)

        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.login_button).click()


    def is_dashboard_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Config.dashboard)
            )
            return True
        except Exception:
            return False