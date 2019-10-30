from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        wd.get("http://tsm-website-dev.s3-website-us-east-1.amazonaws.com")
        wd.find_element(By.NAME, "login").clear()
        wd.find_element(By.NAME, "login").send_keys(username)
        wd.find_element(By.NAME, "login").clear()
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, ".btn").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "li:nth-child(10) .nav-label").click()
