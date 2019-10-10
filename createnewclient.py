# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestCreatenewclient():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(30)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createnewclient(self):
    driver = self.driver
    driver.get("http://tsm-website-dev.s3-website-us-east-1.amazonaws.com/auth/sign-in")
    driver.set_window_size(1302, 952)
    driver.find_element(By.NAME, "login").click()
    driver.find_element(By.NAME, "login").send_keys("istomin.ev@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Istomin18")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(6) .nav-label").click()
    element = driver.find_element(By.LINK_TEXT, "Settings")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".page-controls-center > .btn").click()
    driver.find_element(By.ID, "input-preferredLanguage").click()
    dropdown = driver.find_element(By.ID, "input-preferredLanguage")
    dropdown.find_element(By.XPATH, "//option[. = 'English']").click()
    driver.find_element(By.ID, "input-preferredLanguage").click()
    driver.find_element(By.ID, "input-name").click()
    driver.find_element(By.ID, "input-name").send_keys("name_field")
    driver.find_element(By.ID, "input-legalName").click()
    driver.find_element(By.ID, "input-legalName").send_keys("Legal_name_field")
    driver.find_element(By.ID, "input-email").click()
    driver.find_element(By.ID, "input-email").send_keys("primary_email_field")
    driver.find_element(By.ID, "input-email2").click()
    driver.find_element(By.ID, "input-email2").send_keys("Secondary_email_field")
    driver.find_element(By.ID, "input-phone").click()
    driver.find_element(By.ID, "input-phone").send_keys("Primary_phone_field")
    driver.find_element(By.ID, "input-phone2").click()
    driver.find_element(By.ID, "input-phone2").send_keys("secondary_phone_field")
    driver.find_element(By.ID, "input-fax").click()
    driver.find_element(By.ID, "input-fax").send_keys("fax_field")
    driver.find_element(By.ID, "input-zip").click()
    driver.find_element(By.ID, "input-zip").send_keys("78748")
    driver.find_element(By.ID, "input-country").click()
    driver.find_element(By.ID, "input-country").send_keys("country_field")
    driver.find_element(By.ID, "input-state").click()
    driver.find_element(By.ID, "input-state").send_keys("TX")
    driver.find_element(By.ID, "input-city").click()
    driver.find_element(By.ID, "input-city").send_keys("city_field")
    driver.find_element(By.ID, "input-addressLine").click()
    driver.find_element(By.ID, "input-addressLine").send_keys("Address1_field")
    driver.find_element(By.ID, "input-addressLine2").click()
    driver.find_element(By.ID, "input-addressLine2").send_keys("Address2_field")
    driver.find_element(By.ID, "input-note").click()
    driver.find_element(By.ID, "input-note").send_keys("note_field")
    driver.find_element(By.LINK_TEXT, "Billing").click()
    driver.find_element(By.ID, "client-tin").click()
    driver.find_element(By.ID, "client-tin").send_keys("12345")
    driver.find_element(By.ID, "client-tax").click()
    driver.find_element(By.ID, "client-tax").send_keys("8")
    driver.find_element(By.ID, "client-paymentType").click()
    dropdown = driver.find_element(By.ID, "client-paymentType")
    dropdown.find_element(By.XPATH, "//option[. = 'CASH']").click()
    driver.find_element(By.ID, "client-paymentType").click()
    driver.find_element(By.ID, "client-currency").click()
    dropdown = driver.find_element(By.ID, "client-currency")
    dropdown.find_element(By.XPATH, "//option[. = 'USD - United States dollar']").click()
    driver.find_element(By.ID, "client-currency").click()
    driver.find_element(By.ID, "client-bankName").click()
    driver.find_element(By.ID, "client-bankName").send_keys("bank_field")
    driver.find_element(By.ID, "client-bankAccount").click()
    driver.find_element(By.ID, "client-bankAccount").send_keys("123456789")
    driver.find_element(By.CSS_SELECTOR, "fieldset > .btn-primary").click()
    driver.find_element(By.CSS_SELECTOR, ".routerLinkActive > .nav-label").click()
    driver.find_element(By.CSS_SELECTOR, "li:nth-child(10) .nav-label").click()