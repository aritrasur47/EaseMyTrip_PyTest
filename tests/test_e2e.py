import pytest
from selenium import webdriver
import time

from page_object.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestSite(BaseClass):

    def test_e2e(self):
        time.sleep(5)
        homepage = HomePage(self.driver)

        # Clicking on round-trip
        homepage.round_trip_option()

        # Clicking on From
        homepage.from_location_option()

        # Selecting Mumbai in "From" field
        from_places = homepage.from_places_option()

        for place in from_places:
            if place.text == "Mumbai(BOM)":
                place.click()
                break

        # Clicking on To
        homepage.to_location_option()

        # Selecting Bangalore in "To" field
        to_places = homepage.to_places_option()
        for place in to_places:
            if place.text == "Kolkata(CCU)":
                place.click()
                break

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

        # Calendar (To) selection
        homepage.to_calendar_option()
        homepage.to_day_option()

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

        # Click on Done button
        homepage.done_button_option()

        # Click on search button
        booking_page = homepage.search_button_option()
        time.sleep(10)

        # Take screenshot
        booking_page.take_screenshot()

        # Click on Book Now
        check_out_popup = booking_page.book_now_option()

        # Click on Continue
        checkout_page = check_out_popup.checkout_option()
        time.sleep(2)

        # Scrolling page down
        page_down_scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # do not insure trip
        checkout_page.do_not_insure_option()
        checkout_page.insure_option()
        checkout_page.checkbox_deselect_option()

        checkbox_tick = checkout_page.checkbox_deselect_option()

        if checkbox_tick:
            checkbox_status = checkbox_tick.is_selected()
            assert checkbox_status == False
        else:
            pass

        # checkbox = checkout_page.checkbox_deselect_option()
        # checkbox_tick = checkbox.click()
        #
        # if not checkbox_tick:
        #     checkbox_status = checkbox.is_selected()
        #     assert checkbox_status == False
        # else:
        #     checkbox.click()

        # Enter email
        checkout_page.email_option()

        # Click on Continue Booking
        checkout_page.continue_booking
        time.sleep(2)
