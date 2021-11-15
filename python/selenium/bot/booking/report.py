# This file handles the reporting of search results to the user

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class Report:
    def __init__(self, results: WebElement):
        self.results = results
        self.result_elements = self.get_result_elements()

    def get_result_elements(self):
        return self.results.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]'
        )

    def get_hotel_info(self):
        info = []

        for result in self.result_elements:
            hotel_name = result.find_element(
                By.CLASS_NAME, 'fde444d7ef._c445487e2'
            ).get_attribute('innerHTML').strip()

            hotel_price = result.find_element(
                By.CLASS_NAME, 'fde444d7ef._e885fdc12'
            ).get_attribute('innerHTML').strip()

            try:
                hotel_score = result.find_element(
                    By.CSS_SELECTOR, 'div[aria-label*="Scored"]'
                ).text
            except NoSuchElementException:
                hotel_score = 'No score'

            info.append(
                [hotel_name.replace('&amp;', '&'), hotel_price.replace('&nbsp;', ' '), hotel_score]
            )

        return info
