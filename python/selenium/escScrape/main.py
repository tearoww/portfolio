from selenium.webdriver.common.by import By
from selenium import webdriver
import openpyxl
import pandas

site = "https://eurovisionworld.com/eurovision/"
driver = webdriver.Firefox()
all_tables = {}
year = 2022

driver.implicitly_wait(0.5)
driver.maximize_window()

while year >= 1956:
    driver.get(site + str(year))

    table_html = driver.find_element(By.CSS_SELECTOR, 'table.v_table:nth-child(1)')
    table = pandas.read_html(table_html.get_attribute('outerHTML'))

    for df in table:
        df.to_csv("/mnt/media/documents/csv/esc/" + str(year) + ".csv")

    year -= 1
