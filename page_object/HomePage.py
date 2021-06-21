from selenium.webdriver.common.by import By

from page_object.BookingPage import BookingPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    round_trip = (By.XPATH, "//li[text()='Round-Trip']")
    from_location = (By.ID, "FromSector_show")
    from_places = (By.XPATH, "//ul/li/div/span[@class='ct']")
    to_location = (By.ID, "Editbox13_show")
    to_places = (By.XPATH, "//ul/li/div/span[@class='ct']")
    from_calendar = (By.ID, "ddate")
    from_months = (By.XPATH, "//div[@class='month2']")
    to_calendar = (By.ID, "rdate")

    month_dict = {"1": "Jan",
                  "2": "Feb",
                  "3": "Mar",
                  "4": "Apr",
                  "5": "May",
                  "6": "Jun",
                  "7": "Jul",
                  "8": "Aug",
                  "9": "Sep",
                  "10": "Oct",
                  "11": "Nov",
                  "12": "Dec"}
    year = "2021"
    day = "24"
    to_day = (By.XPATH,
              f"//div[text()='{month_dict['8']} {year}']/parent::div/parent::div //div[@class='days']/ul/li[text()='{day}']")

    select_passenger = (By.CSS_SELECTOR, ".dropbtn_n")
    adult_check = (By.XPATH, "//input[@class='plus_box1']")
    children_check = (By.XPATH, "//input[@class='plus_boxChd']")

    business_class_value = "3"
    level_check = (By.XPATH, f"//div[@id='myDropdown_n']/div/label[{business_class_value}]")

    done_button = (By.CSS_SELECTOR, ".dn_btn")
    search_button = (By.CSS_SELECTOR, ".src_btn")

    def round_trip_option(self):
        round_trip = self.driver.find_element(*HomePage.round_trip).click()
        return round_trip

    def from_location_option(self):
        from_location = self.driver.find_element(*HomePage.from_location).click()
        return from_location

    def from_places_option(self):
        return self.driver.find_elements(*HomePage.from_places)

    def to_location_option(self):
        to_location = self.driver.find_element(*HomePage.to_location).click()
        return to_location

    def to_places_option(self):
        return self.driver.find_elements(*HomePage.to_places)

    def from_calendar_option(self):
        from_calendar = self.driver.find_element(*HomePage.from_calendar).click()
        return from_calendar

    def from_months_option(self):
        return self.driver.find_elements(*HomePage.from_months)

    def to_calendar_option(self):
        to_calendar = self.driver.find_element(*HomePage.to_calendar).click()
        return to_calendar

    def to_day_option(self):
        to_day = self.driver.find_element(*HomePage.to_day).click()
        return to_day

    def passenger_option(self):
        passenger = self.driver.find_element(*HomePage.select_passenger).click()
        return passenger

    def adult_option(self):
        adults = self.driver.find_element(*HomePage.adult_check).click()
        return adults

    def children_option(self):
        child = self.driver.find_element(*HomePage.children_check).click()
        return child

    def ticket_class_option(self):
        ticket_class = self.driver.find_element(*HomePage.level_check).click()
        return ticket_class

    def done_button_option(self):
        done_button = self.driver.find_element(*HomePage.done_button).click()
        return done_button

    def search_button_option(self):
        # self.driver.find_element(*HomePage.search_button)
        search_button = self.driver.find_element(*HomePage.search_button).click()
        booking_page = BookingPage(self.driver)
        return booking_page
