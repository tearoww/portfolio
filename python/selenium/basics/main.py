from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(5)

download_button = driver.find_element_by_id('downloadButton')

download_button.click()

progress_label = driver.find_element_by_class_name('progress-label')

close_button = driver.find_element_by_class_name('ui-dialog-buttonset')

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Complete!'
    )
)

close_button.click()

driver.close()
