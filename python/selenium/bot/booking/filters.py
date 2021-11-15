# This file handles the filtering and sorting of hotel search results

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


class Filters:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def by_rating(self, *desired_ratings):
        rating_box = self.driver.find_element(
            By.CSS_SELECTOR, 'div[data-filters-group="class"]'
        )

        for rating in desired_ratings:
            try:
                rating_box.find_element(
                    By.CSS_SELECTOR, f'div[data-filters-item="class:class={rating}"]'
                ).click()
            except NoSuchElementException:
                print(f'No results with {rating} star rating were found.')

    def sort_by_lowest_price(self):
        time.sleep(2)

        self.driver.find_element(
            By.CSS_SELECTOR, 'li[data-id="price"]'
        ).click()
