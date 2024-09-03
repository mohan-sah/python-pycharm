import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
load_dotenv()

PROMISED_UP = 40
PROMISED_DOWN = 40

TWITTER_EMAIL =  os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD =  os .environ["TWITTER_PASSWORD"]

class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = None
        self.down = None
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--lang=en")
        chrome_options.add_argument("--force-device-scale-factor=0.7")
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self, max_retires = 3, retry_delay = 20):
        URL = "https://www.speedtest.net/"
        self.driver.get(URL)
        go_btn = self.driver.find_element(by=By.CSS_SELECTOR,
                                          value='a[aria-label="start speed test - connection type multi"]')
        go_btn.click()
        print(' go btn clicked')
        for attempt in range(max_retires):

            try:

                down_speed = self.driver.find_element(by=By.CSS_SELECTOR, value='div[class="result-data u-align-left"] span.download-speed')
                print("downspeed :")
                self.down = down_speed.text
                print(self.down)

                up_speed = self.driver.find_element(by=By.CSS_SELECTOR, value='div[class="result-data u-align-left"] span.upload-speed')
                print("upspeed:")
                self.up = up_speed.text
                print(self.up)

                if down_speed == "—" or up_speed == "—":
                    return self.up, self.down
            except NoSuchElementException as e:
                print(f" Attempt {attempt + 1} failed: {e}")
            time.sleep(retry_delay)
        self.driver.quit()






    def tweet_at_provider(self):
        pass

if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
