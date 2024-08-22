import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
URL2 = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , value=True)

driver =  webdriver.Chrome(options=chrome_options)

driver.get(url=URL2)

# link by css selector
# article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# article_count.click()


# # click by link selector
# article_count = driver.find_element(by=By.LINK_TEXT, value="English")
# article_count.click()

# driver.find_element(by=By.CSS_SELECTOR,value=".mw-ui-icon-search").click()
# ## search by Name
# search = driver.find_element(by=By.NAME, value="search")
# ## send input to selenium and send form request by copying keyboard Keys
# search.send_keys("Python",Keys.ENTER)

## auto singin by selenium
fname = driver.find_element(by=By.NAME, value="fName")
lname = driver.find_element(by=By.NAME, value="lName")
email = driver.find_element(by=By.NAME, value="email")

# fname.click()
fname.send_keys("Mohan")
# lname.click()
lname.send_keys("Sah")
# email.click()
email.send_keys("mohansah944@gmail.com")
driver.find_element(by = By.CSS_SELECTOR, value=".btn").click()




time.sleep(3)

driver.quit()

