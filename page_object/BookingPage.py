from selenium.webdriver.common.by import By

from page_object.CheckOutPopupPage import CheckOutPopupPage


class BookingPage:
    def __init__(self, driver):
        self.driver = driver

    book_now = (By.CSS_SELECTOR, "#BtnBookNow")

    def take_screenshot(self):
        return self.driver.get_screenshot_as_file("booking_page.png")

    def book_now_option(self):
        book_now = self.driver.find_element(*BookingPage.book_now).click()
        check_out_popup = CheckOutPopupPage(self.driver)
        return check_out_popup
