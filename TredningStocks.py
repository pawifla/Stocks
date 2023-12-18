# Gather Trending Stocks
# Looking for consecutive green or red days
# Find percentage of green/red days
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta 

# Stock symbol list
stock_list = 'amzn'

start = datetime.now() - timedelta(days = 31)
end = datetime.now()

stock_data = yf.download(stock_list, start, end)

# Identify consecutive days where open is higher than close
consecutive_days = 0
green_days = 0
red_days = 0
total_days = len(stock_data)
for i in range(1, len(stock_data)):
    if stock_data['Open'][i] < stock_data['Close'][i]:
    # Green Day
        green_days += 1
    else:
    # Red Day
        red_days += 1
        consecutive_days = 0

# Overall Gain
initial_price = stock_data['Open'].iloc[0]
final_price = stock_data['Close'].iloc[-1]
overall_gain_perfect = ((final_price - initial_price) / initial_price) * 100

green_precent = (green_days/total_days * 100)
print(f'Ticker: {stock_list}, Green: {green_precent: .2f}%, Gain/Loss:{overall_gain_perfect: .2f}%')
