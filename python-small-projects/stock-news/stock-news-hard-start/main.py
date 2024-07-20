import math
from support import Support
import requests
from datetime import datetime as dt
from datetime import timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
COMPANY_NEWS_KEYWORD = "Tesla"
TICKER = ""
NEWS = ""

environ = Support()
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_API_key = environ.stock_API_key
news_API_key = environ.news_API_key

AuthToken = environ.AuthToken
account_sid = environ.account_sid
auth_token = AuthToken
BODY = f"{TICKER}\n"

now = dt.now()
today_day = now.day
today_month = now.month
today_year = now.year

today = dt.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

date_yesterday = f"{dt.date(yesterday).isoformat()}"
date_day_before_yesterday = f"{dt.date(day_before_yesterday).isoformat()}"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.
def stock_price():
    global BODY
    global TICKER
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "full",
        "apikey": stock_API_key
    }
    # https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo
    response = requests.get(STOCK_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    print(data)
    #what if yesterday data is not available because stock market is closed
    # need error handling for that case
    # yesterday_close = float(data["Time Series (Daily)"][date_yesterday]["4. close"])
    # day_before_yesterday_close = float(data["Time Series (Daily)"][date_day_before_yesterday]["4. close"])

    data_list = [value for (key,value) in data.items()]
    yesterday_close = data_list[0]["4. close"]
    day_before_yesterday_close = float(data_list[1]["4. close"])

    stock_diff = yesterday_close - day_before_yesterday_close

    percent_change_yesterday = round(((stock_diff / yesterday_close) * 100), 2)
    print(percent_change_yesterday)

    if abs(percent_change_yesterday) > 4.00:
        print("diff")
        if percent_change_yesterday < 0:
            TICKER = f"{STOCK}: 🔻{abs(percent_change_yesterday)}\n"
        else:
            TICKER = f"{STOCK}: 🔺{abs(percent_change_yesterday)}\n"
        TICKER += get_news()
        BODY += TICKER
        send_message()

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator

def get_news() -> str:
    global NEWS
    parameters = {
        "qinTitle": COMPANY_NEWS_KEYWORD,
        "from": "2024-07-19",
        "sortBy": "popularity",
        "language": "en",
        "apiKey": news_API_key

    }

    response = requests.get(NEWS_ENDPOINT,
                            params=parameters)
    response.raise_for_status()
    data = response.json()
    articles = data['articles'][:3]

    # for article in articles:
    #     title = article["title"]
    #     description = article["description"]
    #     NEWS += f"Headline: {title}\nBrief: {description}\n"
    # return NEWS
    formatted_article = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in articles]
    NEWS = '\n'.join(formatted_article)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.
def send_message():
    global BODY
    # sms
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+19252737310',
        to='+919141143670',
        body=BODY
    )
    print(message.status)

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=BODY,
        to='whatsapp:+919141143670'
    )
    print(message.status)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
stock_price()
# get_news()


