import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By


load_dotenv()

SIGNIN_EMAIL = os.environ["SIGNIN_EMAIL"]
SIGNIN_PASSWORD = os.environ["SIGNIN_PASSWORD"]
MOBILE_NUMBER = os.environ["MOBILE_NUMBER"]


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
chrome_option.add_argument("--force-device-scale-factor=0.7")

driver =  webdriver.Chrome(options=chrome_option)

TEST_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3989642624&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=Bengaluru%2C%20Karnataka%2C%20India"
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3989438002&f_LF=f_AL&geoId=105214831&keywords=python%20developer&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"

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

# for captcha
input("Press Enter when you have solved the Captcha")

time.sleep(1)

#save jobpost
save_button = driver.find_element(by=By.CSS_SELECTOR, value='div[class="mt5"] button.jobs-save-button')
save_button_text = save_button.find_element(by=By.CSS_SELECTOR, value='span[aria-hidden="true"]')
if save_button_text.text == "Save":
    save_button.click()
else:print("Already Saved")
time.sleep(1)

#obstruction removal
svg_element = driver.find_element(By.CSS_SELECTOR, 'svg[data-test-icon="chevron-down-small"]')
parent_element = svg_element.find_element(By.XPATH, '..')
parent_element.click()
time.sleep(1)


#follow
follow_button = driver.find_element(by=By.CSS_SELECTOR, value='div.jobs-company__box button[type="button"]')
driver.execute_script("arguments[0].scrollIntoView(true);", follow_button)
time.sleep(1)
if follow_button.text  == "Follow":
    follow_button.click()
else:print("Already followed")










time.sleep(1000)
driver.quit()