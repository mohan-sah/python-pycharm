import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException

from dotenv import load_dotenv
load_dotenv()

FACEBOOK_USERNAME = os.environ["FACEBOOK_USERNAME"]
FACEBOOK_PASSWORD = os.environ["FACEBOOK_PASSWORD"]
I_WANT_THESE_SWIPES = 5

URL = "https://tinder.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--lang=en")
chrome_options.add_argument(f"--user-data-dir={os.getcwd()}/.data")
chrome_options.add_argument("--force-device-scale-factor=1.2")


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
def facebook_login():
    sleep(2)
    sign_in_btn  = driver.find_element(by=By.CSS_SELECTOR,value="a[class='c1p6lbu0 Miw(120px)'] .lxn9zzn")
    sign_in_btn.click()

    sleep(1)
    try:
        more_option_btn= driver.find_element(by=By.XPATH, value='//button[text()="More Options"]')
        # more_option_btn= driver.find_element(by=By.XPATH, value='//button[contains(@class, "Typs(button-2)")]')
        # more_option_btn= driver.find_element(by=By.LINK_TEXT, value='More Options')
        more_option_btn.click()
    except NoSuchElementException:
        print("this time [more option] not there")

    sleep(1)
    facebook_login_btn = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='Log in with Facebook']")
    facebook_login_btn.click()


    sleep(3)

    handles = driver.window_handles

    print(handles)
    base_window = handles[0]
    fb_login_window = handles[1]

    print(fb_login_window)
    driver.switch_to.window(fb_login_window)

    email_textfield = driver.find_element(by=By.ID,value='email')
    password_textfield = driver.find_element(by=By.ID,value="pass")
    login_btn = driver.find_element(by=By.CSS_SELECTOR,value='input[value="Log in"]')

    email_textfield.send_keys(FACEBOOK_USERNAME)
    password_textfield.send_keys(FACEBOOK_PASSWORD)
    sleep(0.5)
    login_btn.click()
    sleep(3.8)

    try:
        fb_confirm_element = driver.find_element(by=By.CSS_SELECTOR, value='div span[dir="auto"] span').click()
    except StaleElementReferenceException:
        sleep(4)
        fb_confirm_element = driver.find_element(by=By.CSS_SELECTOR, value='div span[dir="auto"] span').click()
    except NoSuchElementException:
        driver.close()
    handles = driver.window_handles
    base_window = handles[0]
    driver.switch_to.window(base_window)
    print(driver.title)

try :
    facebook_login()
    try:
        sleep(4.6)
        driver.find_element(by=By.CSS_SELECTOR,value='button[aria-label="Allow"]').click()
        sleep(1.3)
        driver.find_element(by=By.CSS_SELECTOR,value='button[aria-label="I’ll miss out"]').click()
        sleep(1.3)
        driver.find_element(by=By.XPATH,value='//div[text() = "I decline"]').click()
        sleep(5)
    except NoSuchElementException:
        print("login done")
except NoSuchElementException:
    print("login complete")

n= 0
total = I_WANT_THESE_SWIPES
while n<total:
    try:
        print("liking...")
        # like_button  = driver.find_element(by=By.XPATH, value='//span[text() = "Like"]')
        # like_button.click()
        # sleep(1.7)
        tinder_card = driver.find_element(
            By.CLASS_NAME,
            'recsCardboard__cards'
        )

        print(tinder_card.get_attribute('innerHTML'))
        # with open("t.html", "w") as f:
        #     f.write(tinder_card.get_attribute('innerHTML'))

        # Issue with data-keyboard-gamepad sometimes 2 div
        button = tinder_card.find_element(
            By.XPATH,
            'div[not(@data-keyboard-gamepad)]/div/div[4]/button'
        )

        button.click()
        sleep(2)
        n+=1
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            sleep(2)




sleep(5)
print("your welcome")
driver.quit()


