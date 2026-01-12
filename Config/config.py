from selenium.webdriver.common.by import By

class Config:

    #baseurl
    base_url = "https://pm.teamx.global/auth/sign-in"


    #valid login credentials
    valid_email = "samran@teamx.ae"
    valid_password = "Demo@123"

    #invalid login credentials
    invalid_email = "notvalid@teamx.global"
    invalid_password = "123456"

    # Locator for dashboard, which indicates a successful login
    dashboard = (By.XPATH, "//h2")