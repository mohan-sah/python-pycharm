from bs4 import BeautifulSoup
import requests
from email_notification_manager import EmailNotificationManager

WEBSITE_URL = "https://appbrewery.github.io/instant_pot/"
TRIGGER_PRICE = 150


email_manager = EmailNotificationManager()

response = requests.get(url=WEBSITE_URL)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page,features="html.parser")
# print(soup.prettify())
# print(soup.title.text)
##price
price = float
price = soup.find(name= "span", class_ ="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").get_text().split("$")[1]
#price.replace(" $", "")
print(price)
price = float(price)
## product name and link
product_title = soup.find(name="span", id = "productTitle").text
print(product_title)
link_to_buy = WEBSITE_URL

## product image
product_image = soup.find(name="div", id ="imgTagWrapperId")
print(product_image)

#
# when price below a certain value, to send an email to yourself.
# In the email, include
# 1.the title of the product,
# 2. the current price ,
# 3. a link to buy the product.
if price < TRIGGER_PRICE:
    email_manager.send_email(product_title = product_title, current_price = price, link_to_buy = link_to_buy)


