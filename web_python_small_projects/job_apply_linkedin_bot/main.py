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

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3989642624&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
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

time.sleep(100)
driver.quit()



