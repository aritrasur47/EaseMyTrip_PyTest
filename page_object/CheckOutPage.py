from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    do_not_insure = (By.XPATH, "//div[@class='insur-no']/label/input[@name='rdoInsuNew']")
    insure = (By.XPATH, "//div[@class='insur-no']/label/input[@name='rdoInsuNew']")
    checkbox_deselect = (By.XPATH, "//label[@for='chkPubReliefFund']")
    email = (By.ID, "txtEmailId")
    continue_booking = (By.XPATH, "//span[text()='Continue Booking']")

    def do_not_insure_option(self):
        do_not_insure = self.driver.find_element(*CheckOutPage.do_not_insure).click()
        return do_not_insure

    def insure_option(self):
        insure_option = self.driver.find_element(*CheckOutPage.insure).click()
        return insure_option

    def checkbox_deselect_option(self):
        checkbox_deselect = self.driver.find_element(*CheckOutPage.checkbox_deselect).click()
        return checkbox_deselect

    def email_option(self):
        email = self.driver.find_element(*CheckOutPage.email).send_keys("aritrasur47@example.com")
        return email

    def continue_booking_option(self):
        continue_booking = self.driver.find_element(*CheckOutPage.continue_booking).click()
        return continue_booking
