from selenium.webdriver.common.by import By

from page_object.CheckOutPage import CheckOutPage


class CheckOutPopupPage:
    def __init__(self, driver):
        self.driver = driver

    checkout_button = (By.XPATH, "//a[text()='Continue']")

    def checkout_option(self):
        checkout_button = self.driver.find_element(*CheckOutPopupPage.checkout_button).click()
        checkout_page = CheckOutPage(self.driver)
        return checkout_page
