from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import re
from twilio_text import send_message
from local_time import get_time

camping_url = "https://reservemn.usedirect.com/MinnesotaWeb/"

driver = webdriver.Firefox()
driver.get(camping_url)
assert "Minnesota" in driver.title
camp_loc = driver.find_element(By.NAME, "ctl00$ctl00$mainContent$txtSearchparkautocomplete")
camp_loc.clear()
camp_loc.send_keys("Temperance River State Park")
sleep(2)
camp_loc.send_keys(Keys.RETURN)

arv_date = driver.find_element(By.NAME, "ctl00$ctl00$mainContent$txtArrivalDate")
arv_date.clear()
sleep(.5)
arv_date.click()
sleep(.5)
arv_date = driver.find_element(By.ID, "FurthestDate")
# arv_date.send_keys("06/07/2023")
sleep(.5)
arv_date.click()

# stay_len = driver.find_element(By.NAME, "ctl00$ctl00$mainContent$ddlHomeNights")
# stay_len.send_keys("1")
# stay_len.send_keys(Keys.RETURN)

sleep(2)

search = driver.find_element(By.LINK_TEXT, "Search")
search.click()

sleep(2)

assert "Search" in driver.title
# Find the link in the 3rd row of the table
check_avail = driver.find_element(By.XPATH, '//table//tr[4]//td[2]//a')
sleep(.5)
check_avail.click()

sleep(2)

availabilities = []

pattern = r'Drive-In #\d+ is not available on \d{2}/\d{2}/\d{4}'
compiled_pattern = re.compile(pattern)

for index, status in enumerate(range(7)):
    res_status = driver.find_element(By.ID, f"td_6_{index}")
    title = res_status.get_attribute("title")
    match = compiled_pattern.search(title)
    if not match:
        availabilities.append(title)

recipients = ["+17636914403"]  # "+17635682973"

for recipient in recipients:
    time = get_time()
    if availabilities:
        message = f"We checked camping availability at {time} and found:\n" +\
                  "\n".join(availabilities) +\
                  "\n" + camping_url
        send_message(recipient, "+15403860915", message)
    else:
        message = f"We checked camping availability at {time} and found no availabilities! =("
        send_message(recipient, "+15403860915", message)

sleep(5)

driver.close()
