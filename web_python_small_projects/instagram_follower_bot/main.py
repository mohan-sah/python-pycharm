
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

INSTAGRAM_USERNAME  = os.environ["INSTAGRAM_USERNAME"]
INSTAGRAM_PASSWORD = os.environ["INSTAGRAM_PASSWORD"]
SIMILAR_ACCOUNT = os.environ["SIMILAR_ACCOUNT"]


class InstaFollower:

    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--lang=en")
        chrome_options.add_argument(f"--user-data-dir={os.getcwd()}/.data")
        chrome_options.add_argument("--force-device-scale-factor=0.9")
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        '''Login to insta gram , if already logged in , skip'''

        try:
            URL =  "https://www.instagram.com/"
            URL2 = "https://www.instagram.com/accounts/login/"
            self.driver.get(URL)

            sleep(5)

            user_name_field = self.driver.find_element(by=By.CSS_SELECTOR, value='input[aria-label="Phone number, username, or email"]')
            user_name_field.send_keys(INSTAGRAM_USERNAME)

            password_field = self.driver.find_element(by=By.CSS_SELECTOR, value = 'input[aria-label="Password"]')
            password_field.send_keys(INSTAGRAM_PASSWORD,Keys.ENTER)
            sleep(4)

            try :
                save_info_btn = self.driver.find_element(by=By.XPATH, value='//button[text()="Save info"]')
                #save_info_btn = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Save info')]")
                save_info_btn.click()
            except NoSuchElementException:
                print("no save info button found")
            else:
                print("no save info, continue")
            sleep(3)
            try:
                notification_dialog = self.driver.find_element(by=By.CSS_SELECTOR, value='div[role="dialog"]')
                notification_span_elements = notification_dialog.find_elements(by=By.TAG_NAME, value="span")
                notification_found = any(span.text == "Turn on Notifications" for span in notification_span_elements)

                if notification_found:
                    print("Text 'Turn on Notifications' found.")
                    not_now_button = self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')
                    not_now_button.click()
                    print("Clicked 'Not Now' button.")
                else:
                    print("Text 'Turn on Notifications' not found.")

            except Exception as e:
                print(f"error occured while handling notification dialog : {e}")
            sleep(3)
        except NoSuchElementException:
            print("login page not found")
    def find_followers(self):
        URL = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
        self.driver.get(URL)


        sleep(3)
        follower_btn = self.driver.find_element(by=By.XPATH, value='//a[contains(text(), " followers")]')
        follower_btn.click()
        print("follower btn clicked")
        i = 0

        pop_up_window = WebDriverWait(
            self.driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")))

        while i<5:
            sleep(2)
            # follower_dialog = self.driver.find_element(by=By.CSS_SELECTOR , value= 'div[role="dialog"]')
            # scroll_script = """
            #     var element = arguments[0];
            #     element.scrollTop = element.scrollHeight;
            # """
            # self.driver.execute_script(scroll_script,follower_dialog)


            # Scroll till Followers list is there

            self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                    pop_up_window)

            i += 1
            print(i)
    def follow(self):
        sleep(800)
        pass


if __name__ == "__main__":
    bot  = InstaFollower()
    # bot.login()
    bot.find_followers()
    bot.follow()