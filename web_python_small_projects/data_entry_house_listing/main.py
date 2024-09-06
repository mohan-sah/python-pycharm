import time,os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from http_header import HttpHeader

load_dotenv()
http_header = HttpHeader()
FORM_URL = os.environ['FORM_URL']
SITE_URL = os.environ['SITE_URL']

response = requests.get(SITE_URL,headers=http_header.header_data)
content = response.text
soup = BeautifulSoup(content,"html.parser")
webpage_title = soup.title.text
print(webpage_title)

cards = soup.find(name='div', id = 'grid-search-results')

listing_links = [listing.get('href') for listing in cards.select('a[data-test="property-card-link"]')]
prices = [price.text.split('+')[0].split('/')[0] for price in cards.select('span[data-test="property-card-price"]')]
addresses = [address.text.strip().replace('|','') for address in cards.select('address[data-test="property-card-addr"]')] #
housing_list = [[link,price,address] for link,price,address in zip(listing_links,prices,addresses)]
print(housing_list)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--lang=en")
chrome_options.add_argument(f"--user-data-dir={os.getcwd()}/.data")
chrome_options.add_argument("--force-device-scale-factor=0.9")
driver = webdriver.Chrome(options=chrome_options)

for housedata in housing_list:
    driver.get(FORM_URL)

    answer1 = driver.find_element(by=By.CSS_SELECTOR, value='input[aria-labelledby="i1"]')
    answer1.send_keys(f'{housedata[0]}')
    answer2 = driver.find_element(by=By.CSS_SELECTOR, value='input[aria-labelledby="i5"]')
    answer2.send_keys(f'{housedata[1]}')
    answer3 = driver.find_element(by=By.CSS_SELECTOR, value='input[aria-labelledby="i9"]')
    answer3.send_keys(f'{housedata[2]}')
    submit_btm = driver.find_element(by=By.CSS_SELECTOR, value='div[aria-label="Submit"]')
    time.sleep(1)
    submit_btm.click()

time.sleep(300)


