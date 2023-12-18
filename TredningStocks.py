# Gather Trending Stocks
# Looking for consecutive green or red days
# Find percentage of green/red days
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Stock symbol list
file_path = 'my-watchlist.txt'
with open(file_path, 'r') as file:
    stock_list = [line.strip() for line in file.readlines()]

print('stockList', stock_list)

start = datetime.now() - timedelta(days = 31)
end = datetime.now()

for ticker in stock_list:
    try:
        stock_data = yf.download(ticker, start, end)
    except Exception as e:
        print(e)
        break

    # Identify consecutive days where open is higher than close
    consecutive_days = 0
    green_days = 0
    red_days = 0
    total_days = len(stock_data)

    for i in range(1, len(stock_data)):
        if stock_data['Open'].iloc[i] < stock_data['Close'].iloc[i]:
        # Green Day
            green_days += 1
        else:
        # Red Day
            red_days += 1
            consecutive_days = 0

    # Overall Gain
    initial_price = stock_data['Open'].iloc[0]
    final_price = stock_data['Close'].iloc[-1]
    weekold_price = stock_data['Open'].iloc[-5]
    overall_gain_percect = ((final_price - initial_price) / initial_price) * 100
    week_gain_percent = ((final_price - weekold_price)/ weekold_price) * 100

    green_precent = (green_days/total_days * 100)
    print(f'Ticker: {ticker}, Green: {green_precent: .2f}%, Month Gain/Loss:{overall_gain_percect: .2f}%, Week Gain: {week_gain_percent: .2f}%')
