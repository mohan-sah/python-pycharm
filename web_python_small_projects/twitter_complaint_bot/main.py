import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

PROMISED_UP = 100
PROMISED_DOWN = 100

TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
TWITTER_USER = os.environ['TWITTER_USER']


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = None
        self.down = None
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--lang=en")
        chrome_options.add_argument(f"--user-data-dir={os.getcwd()}/.data")
        chrome_options.add_argument("--force-device-scale-factor=0.7")
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self, max_retires=3, retry_delay=40):
        URL = "https://www.speedtest.net/"
        self.driver.get(URL)
        go_btn = self.driver.find_element(by=By.CSS_SELECTOR,
                                          value='a[aria-label="start speed test - connection type multi"]')
        go_btn.click()
        print(' go btn clicked')
        for attempt in range(max_retires):

            try:

                down_speed = self.driver.find_element(by=By.CSS_SELECTOR,
                                                      value='div[class="result-data u-align-left"] span.download-speed')
                self.down = down_speed.text
                print(f"downspeed :{self.down}")

                up_speed = self.driver.find_element(by=By.CSS_SELECTOR,
                                                    value='div[class="result-data u-align-left"] span.upload-speed')
                self.up = up_speed.text
                print(f"upspeed:{self.up}")

                if down_speed == "—" or up_speed == "—":
                    return self.up, self.down
            except NoSuchElementException as e:
                print(f" Attempt {attempt + 1} failed: {e}")
            time.sleep(retry_delay)

    def login_twitter(self):
        try:
            sing_in_btn = self.driver.find_element(by=By.XPATH, value="//span[text()='Sign in']")
            sing_in_btn.click()
            print("logging in...")
            time.sleep(5)

            email_box = self.driver.find_element(by=By.CSS_SELECTOR, value='input[name="text"]')
            email_box.send_keys(TWITTER_EMAIL, Keys.ENTER)
            time.sleep(3)

            try:
                if self.driver.find_element(by=By.XPATH,
                                            value="//span[text()='Enter your phone number or username']").text == "Enter your phone number or username":
                    user_box = self.driver.find_element(by=By.CSS_SELECTOR, value='input[name="text"]')
                    user_box.send_keys(TWITTER_USER, Keys.ENTER)
                    time.sleep(3)
                if self.driver.find_element(by=By.CSS_SELECTOR,
                                            value='h1[role="heading"]').text == "Enter your password":
                    password_box = self.driver.find_element(by=By.CSS_SELECTOR, value='input[name="password"]')
                    password_box.send_keys(TWITTER_PASSWORD, Keys.ENTER)
                    time.sleep(3)
            except NoSuchElementException:
                pass
        except NoSuchElementException:
            pass

    def tweet_at_provider(self):
        URL = "https://x.com/home?lang=en"
        Content = f"HEy internet provider , Why is my internet speed {self.down}down/{self.up}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
        self.driver.get(URL)
        self.login_twitter()
        print("login successfull")
        time.sleep(5)
        post_content = self.driver.find_element(by=By.CSS_SELECTOR, value="[data-testid='tweetTextarea_0']")
        post_content.click()
        print("writing post...")
        post_content.send_keys(Content)
        print(f"POST: {Content}")
        post_content.send_keys( Keys.CONTROL, Keys.ENTER)
        time.sleep(3)

        time.sleep(50)
        self.driver.close()


if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
