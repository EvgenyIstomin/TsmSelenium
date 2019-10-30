from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def create_new_client(self, Client):
        self.open_all_clients_page()
        self.open_new_client_general_page()
        self.fillout_client_general_page(Client)
        self.open_client_billing_page()
        self.fillout_client_billing_page()
        self.press_create_client_button()
        self.mark_client_as_deleted()
        self.open_all_clients_page()

    def mark_client_as_deleted(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Advanced").click()
        wd.find_element(By.CSS_SELECTOR, ".btn-danger").click()

    def press_create_client_button(self):
        wd = self.wd
        wd.find_element(By.CSS_SELECTOR, "fieldset > .btn-prim"
                                         "ary").click()

    def fillout_client_billing_page(self):
        wd = self.wd
        wd.find_element(By.ID, "client-tin").click()
        wd.find_element(By.ID, "client-tin").send_keys("12345")
        wd.find_element(By.ID, "client-tax").click()
        wd.find_element(By.ID, "client-tax").send_keys("8")
        wd.find_element(By.ID, "client-paymentType").click()
        dropdown = wd.find_element(By.ID, "client-paymentType")
        dropdown.find_element(By.XPATH, "//option[. = 'CASH']").click()
        wd.find_element(By.ID, "client-paymentType").click()
        wd.find_element(By.ID, "client-currency").click()
        dropdown = wd.find_element(By.ID, "client-currency")
        dropdown.find_element(By.XPATH, "//option[. = 'USD - United States dollar']").click()
        wd.find_element(By.ID, "client-currency").click()
        wd.find_element(By.ID, "client-bankName").click()
        wd.find_element(By.ID, "client-bankName").send_keys("bank_field")
        wd.find_element(By.ID, "client-bankAccount").click()
        wd.find_element(By.ID, "client-bankAccount").send_keys("123456789")

    def open_client_billing_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Billing").click()

    def fillout_client_general_page(self, client):
        wd = self.wd
        # element = driver.find_element(By.LINK_TEXT, "Settings")
        # actions = ActionChains(driver)
        # actions.move_to_element(element).perform()
        wd.find_element(By.ID, "input-preferredLanguage").click()
        dropdown = wd.find_element(By.ID, "input-preferredLanguage")
        dropdown.find_element(By.XPATH, "//option[. = %s]" % client.preferred_language).click()
        wd.find_element(By.ID, "input-preferredLanguage").click()
        wd.find_element(By.ID, "input-name").click()
        wd.find_element(By.ID, "input-name").send_keys(client.name)
        wd.find_element(By.ID, "input-legalName").click()
        wd.find_element(By.ID, "input-legalName").send_keys(client.legal_name)
        wd.find_element(By.ID, "input-email").click()
        wd.find_element(By.ID, "input-email").send_keys(client.primary_email)
        wd.find_element(By.ID, "input-email2").click()
        wd.find_element(By.ID, "input-email2").send_keys(client.secondary_email)
        wd.find_element(By.ID, "input-phone").click()
        wd.find_element(By.ID, "input-phone").send_keys(client.primary_phone)
        wd.find_element(By.ID, "input-phone2").click()
        wd.find_element(By.ID, "input-phone2").send_keys(client.secondary_phone)
        wd.find_element(By.ID, "input-fax").click()
        wd.find_element(By.ID, "input-fax").send_keys(client.fax)
        wd.find_element(By.ID, "input-zip").click()
        wd.find_element(By.ID, "input-zip").send_keys(client.postal_code)
        wd.find_element(By.ID, "input-country").click()
        wd.find_element(By.ID, "input-country").send_keys(client.country)
        wd.find_element(By.ID, "input-state").click()
        wd.find_element(By.ID, "input-state").send_keys(client.state)
        wd.find_element(By.ID, "input-city").click()
        wd.find_element(By.ID, "input-city").send_keys(client.city)
        wd.find_element(By.ID, "input-addressLine").click()
        wd.find_element(By.ID, "input-addressLine").send_keys(client.address_line_1)
        wd.find_element(By.ID, "input-addressLine2").click()
        wd.find_element(By.ID, "input-addressLine2").send_keys(client.address_line_2)
        wd.find_element(By.ID, "input-note").click()
        wd.find_element(By.ID, "input-note").send_keys(client.note)

    def open_new_client_general_page(self):
        wd = self.wd
        # driver.find_element(By.CSS_SELECTOR, ".page-controls-center > .btn").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='>>'])[1]/following::button[1]").click()

    def open_all_clients_page(self):
        wd = self.wd
        wd.find_element(By.CSS_SELECTOR, "li:nth-child(6) .nav-label").click()

    def destroy(self):
        self.wd.quit()
