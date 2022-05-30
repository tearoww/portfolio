from selenium.webdriver.common.by import By
from collections import Counter
from selenium import webdriver
from datetime import datetime

site = "https://eurovisionworld.com/eurovision/"
probability = open("probability.txt", "w")
nobody = open("nobody.txt", "w")
driver = webdriver.Firefox()
year = datetime.now().year
indexes = []
running = []
places = []
occur = []
i = 1

driver.implicitly_wait(0.5)
driver.maximize_window()

while year >= 1956:
    if year != 2020:
        driver.get(site + str(year))

        table = driver.find_element(
        By.CSS_SELECTOR, 'table.v_table:nth-child(1)')
        participants = table.find_element(
        By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        for row in participants:
            columns = row.find_elements(By.TAG_NAME, 'td')

            places.append(int(columns[0].text))

            if year > 2015:
                running.append(int(columns[6].text))
            else:
                running.append(int(columns[4].text))

    year -= 1

while i <= max(places):
    index = [x for x in range(len(places)) if places[x] == i]

    for item in index:
        occur.append(running[item])

    participant = Counter(occur).most_common(1)[0][0]
    occurrences = Counter(occur).most_common(1)[0][1]

    probability.write(
    "Running number " +
    str(participant) +
    " was the most likely to rank number " + str(i) +
    " (" + str(occurrences) + " out of " + str(len(running)) +
    "!). It has had a rate of " +
    str(round(occurrences / len(running) * 100, 2)) + "%.\n")

    nobody.write(
    "Nobody has ranked " +
    str(i) +
    " from these running places: " + str(set(running).difference(occur)) + "\n")

    indexes.clear()
    occur.clear()
    i += 1

probability.close()
nobody.close()
driver.quit()
