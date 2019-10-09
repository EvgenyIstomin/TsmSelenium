# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_login(self):
        wd = self.wd
        # open home page
        self.openHomePage(wd)
        # login
        self.login(wd, username = "istomin.ev@gmail.com", password = "Istomin18")
        # log out
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Settings'])[1]/following::span[1]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("(button.btn.btn-primary.btn-lg.btn-block").click()
        # wd.find_element_by_xpath(
        #     "(.//*[normalize-space(text()) and normalize-space(.)='Remember me'])[1]/following::button[1]").click()

    def openHomePage(self, wd):
        wd.get("http://tsm-website-dev.s3-website-us-east-1.amazonaws.com/auth/sign-in")

    def tearDown(self):
        self.wd.quit()

# if __name__ == "__main__":
#     unittest.main()
