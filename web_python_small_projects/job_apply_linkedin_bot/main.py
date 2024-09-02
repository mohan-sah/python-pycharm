import os
import time

import selenium.common.exceptions
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

#for captcha
input("Press Enter when you have solved the Captcha")

time.sleep(1)
#job apply process
easy_apply_button = driver.find_element(by=By.CSS_SELECTOR, value='.jobs-apply-button')
easy_apply_button.click()

time.sleep(1)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(MOBILE_NUMBER)
next_button = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='Continue to next step']")
next_button.click()
next_button.click()
time.sleep(1)

#deal with additional question
# Define your question and corresponding answer

questions_and_answers = {
    "Are you willing to take a drug test, in accordance with local law/regulations?": "Yes",
    "How many years of work experience do you have with Python (Programming Language)?": "1",  # Example answer
    "How many years of work experience do you have with Automation?": "1" , # Example answer
    "How many years of work experience do you have with AUTOSAR?": "0",
    "How many years of work experience do you have with GitHub?": "1",
    "Python Full Stack Development (HTML5, CSS3, BootStrap, JavaScript, Python and Django)": "Yes"
}

# Iterate through questions and provide answers
for question, answer in questions_and_answers.items():
    try:
        # Find the question by its label
        question_element = driver.find_element(By.XPATH, f"//label[contains(text(), '{question}')]")

        # Locate the form element based on the question
        form_element = question_element.find_element(By.XPATH, "..")  # ".." Parent element usually contains the input field

        # Check if it's a radio button or text input
        if "radio" in form_element.get_attribute("innerHTML"):
            print("radio_element")
            # Find and select the radio button
            option_element = form_element.find_element(By.XPATH, f".//input[@value='{answer}']")
            if not option_element.is_selected():
                option_element.click()
        elif "text" in form_element.get_attribute("innerHTML"):
            print("text_element")
            # Find and fill the text input
            input_element = form_element.find_element(By.XPATH, ".//input[@type='text']")
            input_element.send_keys(answer)
        elif "select" in form_element.get_attribute("innerHTML"):
            print("select element")
            select_element = form_element.find_element(by=By.XPATH, value=f".//select" )
            select = Select(select_element)
            select.select_by_visible_text(answer)

        else:
            print(f"Unknown input type for question: '{question}'")
    except NoSuchElementException:
        print(f"Unable to find or interact with the question: '{question}'")

# Submit the form if necessary
submit_button = driver.find_element(By.XPATH, "//button[@aria-label='Review']")
submit_button.click()



time.sleep(1000)
driver.quit()



