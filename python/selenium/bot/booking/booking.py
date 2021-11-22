# This file handles hotel searching

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from booking.input_handling import *
from prettytable import PrettyTable
from booking.filters import Filters
import booking.constants as const
from booking.report import Report
from selenium import webdriver
import time


class Booking(webdriver.Firefox):
    def __init__(self, close=False):
        self.close = close
        super(Booking, self).__init__()
        self.implicitly_wait(0.5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.close:
            self.quit()

    def main_page(self):
        self.get(const.MAIN_PAGE_URL)

    def deny_cookies(self):
        time.sleep(1)

        self.find_element(
            By.ID, 'onetrust-pc-btn-handler'
        ).click()

        self.find_element(
            By.CLASS_NAME, 'save-preference-btn-handler.onetrust-close-btn-handler'
        ).click()

    def change_currency(self, desired_currency):
        currency_found = False

        time.sleep(1)

        self.find_element(
            By.CLASS_NAME, 'bui-button.bui-button--light.bui-button--large'
        ).click()

        while not currency_found:
            try:
                self.find_element(
                    By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={desired_currency}"]'
                ).click()

                currency_found = True
            except NoSuchElementException:
                desired_currency = handle_currency(currency_not_found=True)

    def select_destination(self, destination):
        destination_found = False

        search_field = self.find_element(
            By.ID, 'ss'
        )

        while not destination_found:
            try:
                search_field.clear()
                search_field.send_keys(destination)

                time.sleep(1)

                self.find_element(
                    By.CSS_SELECTOR, 'li[data-i="0"]'
                ).click()  # Select the first search result

                destination_found = True
            except NoSuchElementException:
                destination = handle_destination(destination_not_found=True)

        if self.find_element(
            By.CLASS_NAME, 'bui-checkbox.xp__results-on-map.sb-searchbox__map_trigger'
        ).is_displayed():
            self.find_element(
                By.CLASS_NAME, 'bui-checkbox.xp__results-on-map.sb-searchbox__map_trigger'
            ).click()  # Uncheck show on map if that's an option

    def set_dates(self, dates):
        check_in = dates[0]
        check_out = dates[1]
        check_in_not_set = True
        check_out_not_set = True

        if not self.find_element(
            By.CLASS_NAME, 'bui-calendar__control.bui-calendar__control--next'
        ).is_displayed():
            self.find_element(
                By.CLASS_NAME, 'xp__dates-inner'
            ).click()  # Click the calendar into view if not in view

        while check_in_not_set or check_out_not_set:
            try:
                if check_in_not_set:
                    self.find_element(
                        By.CSS_SELECTOR, f'td[data-date="{check_in}"]'
                    ).click()  # Select the check-in date if visible

                    check_in_not_set = False
                elif check_out_not_set:
                    self.find_element(
                        By.CSS_SELECTOR, f'td[data-date="{check_out}"]'
                    ).click()  # Select the check-out date if visible

                    check_out_not_set = False
            except NoSuchElementException:
                self.find_element(
                    By.CLASS_NAME, 'bui-calendar__control.bui-calendar__control--next'
                ).click()  # Click the next arrow if either date is not visible

    def set_guests(self, adults, rooms):
        adults_not_set = True
        rooms_not_set = True

        self.find_element(
            By.ID, 'xp__guests__toggle'
        ).click()  # Click to show amounts and controls of guests

        while adults_not_set:
            amount_of_adults = int(self.find_element(
                By.ID, 'group_adults'
            ).get_attribute('value'))

            if int(adults) < int(amount_of_adults):
                self.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]'
                ).click()

            elif int(adults) > int(amount_of_adults):
                self.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]'
                ).click()
            else:
                adults_not_set = False

        while rooms_not_set:
            amount_of_rooms = int(self.find_element(
                By.ID, 'no_rooms'
            ).get_attribute('value'))

            if int(rooms) < int(amount_of_rooms):
                self.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Decrease number of Rooms"]'
                ).click()
            elif int(rooms) > int(amount_of_rooms):
                self.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]'
                ).click()
            else:
                rooms_not_set = False

    def search_for_hotels(self):
        self.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        ).click()

    def filter_results(self):
        apply_filter = Filters(driver=self)

        apply_filter.by_rating(4, 5)
        apply_filter.sort_by_lowest_price()

    def report_results(self):
        try:
            results = self.find_element(
                By.CLASS_NAME, '_814193827'
            )

            report = Report(results)
            report.get_result_elements()

            table = PrettyTable(
                field_names=["Name", "Price", "Score"]
            )
            table.add_rows(report.get_hotel_info())

            print('\nHere are the results:\n')
            print(table)
        except NoSuchElementException:
            print('\nNo results to show. Exiting..')
