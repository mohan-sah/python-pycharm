import os
from dotenv import load_dotenv
from selenium import webdriver
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
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):

        pass

    def tweet_at_provider(self):
        pass

if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
