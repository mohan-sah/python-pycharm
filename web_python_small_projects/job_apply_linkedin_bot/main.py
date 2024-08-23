import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv


load_dotenv()

SIGNIN_EMAIL = os.environ["SIGNIN_EMAIL"]
SIGNIN_PASSWORD = os.environ["SIGNIN_PASSWORD"]

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver =  webdriver.Chrome(options=chrome_option)

TEST_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3989642624&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=Bengaluru%2C%20Karnataka%2C%20India"
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3985604898&f_LF=f_AL&geoId=105214831&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_HISTORY&refresh=true"

driver.set_window_size(640, 480)
driver.get(URL)
#signin process
sign_in_btn = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')

sign_in_btn.click()

username_field = driver.find_element(by=By.CSS_SELECTOR, value="input#username")
password_field = driver.find_element(by=By.CSS_SELECTOR, value="input#password")
sign_in_btn2 = driver.find_element(by=By.XPATH , value='//*[@id="organic-div"]/form/div[3]/button')



username_field.send_keys(SIGNIN_EMAIL)
password_field.send_keys(SIGNIN_PASSWORD)
sign_in_btn2.click()

#for captcha
# input("Press Enter when you have solved the Captcha")

time.sleep(1)
#job apply process
easy_apply_button = driver.find_element(by=By.XPATH, value='//*[@id="ember52"]')
easy_apply_button.click()

# mobile_number_field = driver.find_element(by=By.CSS_SELECTOR, value="#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3985604898-7981708388-phoneNumber-nationalNumber")

time.sleep(100)
driver.quit()



