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

    #Profile picture click
    profile = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/header/div/div/div[2]/div[2]/button/h5")

    #logout
    logout = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/header/div/div/div[2]/div[2]/div/ul/li[2]/div")