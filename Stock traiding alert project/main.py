import requests
import datetime

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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
# -------------------------------------------------------------------------------------------------------------------------


STOCK = "ITC.BSE"
COMPANY_NAME = "ITC"
Stocks_apiKey = "WAYQ1RPQJRZ5TJHN"
url = "https://www.alphavantage.co/query"
parameters = {"function": "TIME_SERIES_DAILY", "symbol": STOCK, "outputsize": "compact", "apikey": Stocks_apiKey}
stock_response = requests.get(url, params=parameters)

stock_data = stock_response.json()["Time Series (Daily)"]
yesterday = list(stock_data.keys())[0]
day_before = list(stock_data.keys())[1]
stock_price_yesterday = float(stock_data[yesterday]["1. open"])
stock_price_day_before = float(stock_data[day_before]["1. open"])
price_difference = ((stock_price_yesterday - stock_price_day_before) / stock_price_day_before) * 100


def get_news():
    news_apikey = "9f96a6b32cb6495290a87c8111eff693"
    url = "https://newsapi.org//v2/top-headlines"
    parameters = {"q": COMPANY_NAME, "apiKey": news_apikey}
    news_response = requests.get(url, params=parameters)
    top_news = news_response.json()["articles"]
    print(top_news[1]["title"], "\n", top_news[2]["title"], "\n", top_news[3]["title"])


if price_difference >= 5 or price_difference <= -5:
    get_news()
else:
    print("pass")
