import pytest
from selenium import webdriver
import time

from TestData.e2ePageData import e2ePageData
from page_object.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestSite(BaseClass):

    def test_e2e(self, get_data):
        log = self.get_logger()
        time.sleep(5)
        homepage = HomePage(self.driver)

        # Clicking on round-trip
        homepage.round_trip_option()
        log.info("Round Trip button is clicked.")

        # Clicking on From
        homepage.from_location_option()

        # Selecting Mumbai in "From" field
        from_places = homepage.from_places_option()

        for place in from_places:
            if place.text == "Mumbai(BOM)":
                place.click()
                break
        log.info("Mumbai location is selected in 'From' field.")

        # Clicking on To
        homepage.to_location_option()

        # Selecting Bangalore in "To" field
        to_places = homepage.to_places_option()
        for place in to_places:
            if place.text == "Kolkata(CCU)":
                place.click()
                break
        log.info("Kolkata location is selected in 'To' field.")

        # Calendar (From) selection
        homepage.from_calendar_option()

        from_months = homepage.from_months_option()
        for month in from_months:
            if month.text == "JUL 2021":
                days = month.find_elements_by_xpath("./parent::div/parent::div //div[@class='days']/ul/li")
                for day in days:
                    if day.text == "12":
                        day.click()
                        break
        log.info("Round trip date is from : " + day.text + month.text)

        # Calendar (To) selection
        homepage.to_calendar_option()
        homepage.to_day_option()
        log.info("Round trip date is to : 24 AUG 2021")

        # Click on dropdown menu to select passenger
        homepage.passenger_option()
        time.sleep(2)

        # Selecting one more adult
        homepage.adult_option()

        # selecting 2 children
        for i in range(1, 3):
            homepage.children_option()

        # Selecting business class radio button
        homepage.ticket_class_option()
        time.sleep(2)
        log.info("2 adults, 2 children & Business class is selected.")

        # Click on Done button
        homepage.done_button_option()
        log.info("Done button clicked")

        # Click on search button
        booking_page = homepage.search_button_option()
        time.sleep(10)
        log.info("Search button is clicked and the page is navigated to flight details page.")

        # Take screenshot
        # booking_page.take_screenshot()
        # log.info("Screenshot is taken.")

        # Click on Book Now
        check_out_popup = booking_page.book_now_option()
        log.info("Book now button is clicked.")

        # Click on Continue
        checkout_page = check_out_popup.checkout_option()
        log.info("Continue button is clicked in the checkout_popup screen.")
        time.sleep(2)

        # Scrolling page down
        page_down_scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        log.info("Page scrolled down using JSExecutor.")

        # do not insure trip
        checkout_page.do_not_insure_option()
        log.info("Do not insure option is selected.")

        checkout_page.insure_option()
        checkout_page.checkbox_deselect_option()

        checkbox_tick = checkout_page.checkbox_deselect_option()

        if checkbox_tick:
            checkbox_status = checkbox_tick.is_selected()
            assert checkbox_status == False
        else:
            pass
        log.info("No donations provided.")

        # checkbox = checkout_page.checkbox_deselect_option()
        # checkbox_tick = checkbox.click()
        #
        # if not checkbox_tick:
        #     checkbox_status = checkbox.is_selected()
        #     assert checkbox_status == False
        # else:
        #     checkbox.click()

        # Enter email
        checkout_page.email_option().send_keys(get_data["email"])
        log.info("Email : " + get_data["email"] + " is entered.")

        # Click on Continue Booking
        checkout_page.continue_booking_option()
        log.info("Continue booking is clicked.")
        log.info("-------------------------------------------------")
        time.sleep(2)
        # self.driver.refresh()

    @pytest.fixture(params=e2ePageData.test_e2e_page_data)
    def get_data(self, request):
        return request.param
