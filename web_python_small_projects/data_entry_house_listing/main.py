from bs4 import BeautifulSoup
import requests


FORM_URL = "https://forms.gle/QcLfUMXTFd4xUW787"
SITE_URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(SITE_URL)
content = response.text

soup = BeautifulSoup(content,"html.parser")
webpage_title = soup.title.text
print(webpage_title)






