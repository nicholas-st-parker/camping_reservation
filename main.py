from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://reservemn.usedirect.com/MinnesotaWeb/")
assert "Minnesota" in driver.title
camp_loc = driver.find_element(By.NAME, "ctl00$ctl00$mainContent$txtSearchparkautocomplete")
camp_loc.clear()
camp_loc.send_keys("Temperance River State Park")
sleep(2)
camp_loc.send_keys(Keys.RETURN)

arv_date = driver.find_element(By.NAME, "ctl00$ctl00$mainContent$txtArrivalDate")
arv_date.clear()
arv_date.send_keys("07/01/2023")
# arv_date.send_keys(Keys.RETURN)

stay_len = driver.find_element(By.NAME, "ctl00$ctl00$mainContent$ddlHomeNights")
stay_len.send_keys("1")
stay_len.send_keys(Keys.RETURN)

sleep(1)

search = driver.find_element(By.LINK_TEXT, "Search")
search.click()

sleep(1)

assert "Search" in driver.title
check_avail = driver.find_elements(By.LINK_TEXT, "Check Availability")[2]
check_avail.click()



# assert "No results found." not in driver.page_source
# driver.close()