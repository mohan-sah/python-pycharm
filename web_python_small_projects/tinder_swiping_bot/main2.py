from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import *


class TinderAutoSwipe:
    driver: webdriver
    main_frame = ""
    login_frame = ""

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--lang=en")
        chrome_options.add_argument(f"--user-data-dir={os.getcwd()}/.data")
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(
            "https://tinder.com/"
        )
        sleep(5)

        # Get main page handle so we can compare handle vs sign in window
        self.main_frame = self.driver.current_window_handle

        try:
            # cookies accept
            cookies_button = self.driver.find_element(By.XPATH, value='//*[text()="I accept"]')
        except NoSuchElementException:
            pass
        else:
            cookies_button.click()
            sleep(1)

        try:
            login_button = self.driver.find_element(By.XPATH, value='//*[text()="Log in"]')
        except NoSuchElementException:
            pass
        else:
            login_button.click()
            sleep(5)

        try:
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,
                                                                 '//*[@title="Sign in with Google Button"]'))
            google_sign_in_button = self.driver.find_element(By.XPATH, '//*[@role="button"]')
        except NoSuchElementException:
            pass
        else:
            google_sign_in_button.click()
            sleep(5)

        # changing the handles to access login page
        for handle in self.driver.window_handles:
            if handle != self.main_frame:
                self.login_frame = handle
                # change the control to signin page
                self.driver.switch_to.window(self.login_frame)

        try:
            google_mail = self.driver.find_element(By.ID, 'identifierId')
        except NoSuchElementException:
            pass
        else:
            google_mail.send_keys(GOOGLE_ACCOUNT_EMAIL)
            google_mail.send_keys(Keys.ENTER)
            sleep(20)

        # You have to input the captcha as we can't do that for now

        try:
            google_password = self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        except NoSuchElementException:
            pass
        else:
            google_password.send_keys(GOOGLE_ACCOUNT_PASSWORD)
            google_password.send_keys(Keys.ENTER)
            sleep(10)

    def swipe(self):
        self.driver.switch_to.window(self.main_frame)

        for i in range(100):
            try:
                self.driver.find_element(
                    By.XPATH, "//*[contains(text(), 'Add Tinder to your Home Screen')]"
                )
                add_tinder_to_home_screen = self.driver.find_element(
                    By.XPATH,
                    '//*[@role="dialog"]'
                )
            except NoSuchElementException:
                pass
            else:
                # to do Create click "NO"
                with open("add_tinder_to_home_screen.html", "w") as f:
                    f.write(add_tinder_to_home_screen.get_attribute('innerHTML'))

            tinder_card = self.driver.find_element(
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



if __name__ == '__main__':
    app = TinderAutoSwipe()
    app.login()
    app.swipe()