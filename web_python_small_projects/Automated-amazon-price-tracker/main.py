from bs4 import BeautifulSoup

import requests
from email_notification_manager import EmailNotificationManager

# WEBSITE_URL = "https://appbrewery.github.io/instant_pot/"
# WEBSITE_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# WEBSITE_URL = "https://amzn.in/d/hQVoETU"
WEBSITE_URL = "https://www.amazon.in/dp/B0C6TWHN8Y/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pd_rd_plhdr=t&aref=QngiaJQCFa"
TRIGGER_PRICE = 150

email_manager = EmailNotificationManager()
cookies = {
        "csm-hit" :"tb:s-6DTBNSTV471EHHHQ2EQX|1724237766611&t:1724237770939&adb:adblk_no",
        "i18n-prefs":"INR",
        "session-id":"261-4700197-3858964",
        "session-id-time":"2082787201l",
        "session-token":"gSY9U+J1sJgzClnd6I/pKufLc4lGnLzsYmaYMkDBjTxiyuAH982OD4VlrLZahGNSI1JRmEcQWdkJflRFTVUyySu4V8x6S1Q34vpAq6qi0sK1BAGoVOREuDhUlQDAYG/JqxgpMwBfcGeeI24mHGmt+Jn+SovHZ64OrMgC78lsgbU1n3+MRucPe6j5lJ1T4UUT5j+N1B5SWnmOZFkjXUu5V+sMZdDlxp+A+Vm+skTdDB8F91SFnvyWLjOC8umybC4ED0vr5xVVFBobfcouHSZ4igD8T8oO+AXNgYQHVjR4aoLwgqAP/QUQUbJhK5wCXfFtaiSYDajFs8p2fiFx2T9TVUtashCxZllg",
        "ubid-acbin":"258-5435697-5123067"
}
response = requests.get(url=WEBSITE_URL,cookies=cookies, headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Dnt": "1",
        "Priority": "u=0, i",
        "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    })
html = response.text

soup = BeautifulSoup(html, "lxml")
print(soup.prettify())
print(soup.title.text)  # print(soup.title.text)
##price
# price = float
# price = "".join(soup.find(name="span", _class="a-price-whole").get_text().split(","))
price = soup.select_one(selector="span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay").get_text().replace("$", "").replace(" ₹","").replace(",","")

# price.replace(" $", "")
print(price)
price = float(price)
## product name and link
product_title = soup.find(name="span", id="productTitle").text
# img_tag = soup.select_one("div img #landingImage")

link_to_buy = WEBSITE_URL

## product image
#
# product_image_url = soup.find(name="div", id ="imgTagWrapperId").get('src')
# product_image = soup.find(name="div", id ="imgTagWrapperId")
# print(product_image)
# print(product_image_url)

#
# when price below a certain value, to send an email to yourself.
# In the email, include
# 1.the title of the product,
# 2. the current price ,
# 3. a link to buy the product.
# if price < TRIGGER_PRICE:
#     email_manager.send_html_email(product_title=product_title, current_price=price, link_to_buy=link_to_buy)
#     # email_manager.send_email(product_title = product_title, current_price = price, link_to_buy = link_to_buy)
