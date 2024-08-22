import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://orteil.dashnet.org/cookieclicker/"


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url=URL)
action = ActionChains(driver)

time.sleep(4)
got_it = driver.find_element(by=By.CLASS_NAME,value="cc_btn_accept_all")
got_it.click()
time.sleep(3)
# english = driver.find_element(by=By.CSS_SELECTOR, value="div .framed #langSelect-EN")
# time.sleep(2)
cookie = driver.find_element(by=By.ID, value="bigCookie")

start_time = time.time()
timeout = 10
check_upgrade_time = 5
store = driver.find_element(by=By.ID, value="products")

while True:#not action.move_by_offset(0,0)

    cookie.click()
    if  time.time() - start_time >check_upgrade_time:
        start_time = time.time()
        print("pass 5")



time.sleep(20)
driver.quit()