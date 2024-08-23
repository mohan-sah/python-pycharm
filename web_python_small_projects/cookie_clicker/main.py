import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://orteil.dashnet.org/cookieclicker/'

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url=URL)
action = ActionChains(driver)

# deals with selecting lang and allow cookies
time.sleep(3)
got_it = driver.find_element(by=By.CLASS_NAME, value="cc_btn_accept_all")
got_it.click()
english = driver.find_element(by=By.XPATH, value='//*[@id="langSelect-EN"]')
english.click()
time.sleep(2)

# main program
cookie = driver.find_element(by=By.ID, value="bigCookie")
start_time = time_to_check = time.time()
timeout = 10
check_upgrade_time = 5
store = driver.find_element(by=By.ID, value="products")
upgrade_box  = driver.find_element(by=By.CSS_SELECTOR, value="div#upgrades.storeSection.upgradeBox")

while True:

    # cookie auto upgrade achieved.will stop after 5 mins and show final result
    cookie.click()
    #yet to do
    # if upgrade_box.find_element(by=By.CSS_SELECTOR, value="div") in upgrade_box:
    #     for box_item in upgrade_box.find_elements(by=By.CSS_SELECTOR, value="div"):
    #         box_item.click()


    if time.time() - start_time > check_upgrade_time:
        start_time = time.time()
        products = store.find_elements(by=By.CSS_SELECTOR, value=".enabled")
        product_list = []
        for product in products:
            product_list.append(product)
        print(product_list)
        try:
            buy_this = product_list[-1]
            buy_this.click()
            print(f"bought {buy_this.text}")
        except IndexError:
            print("saving money this time...")

    if time.time() - time_to_check > 300:
        print(driver.find_element(by=By.XPATH, value='//*[@id="cookies"]').text)
        break

time.sleep(50)
driver.quit()
