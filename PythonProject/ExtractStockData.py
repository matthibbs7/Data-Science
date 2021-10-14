# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:36:45 2021

yfinance demo

@Matthew Hibbs
"""

import yfinance as yf
import pandas as pd

# Create ticker object to access functions for extracting data
apple = yf.Ticker("AAPL")

# Extract Stock Information
apple_info = apple.info

# Extract Share Price
apple_share_price = apple.history(period="max")
# apple_share_price.head()
apple_share_price.reset_index(inplace=True)
apple_share_price.plot(x="Date", y="Open")

# Extract Dividends
apple.dividends.plot()

# Exercise: Create AMD ticker

amd = yf.Ticker("AMD").info
amd_obj = yf.Ticker("AMD")
amd_country = amd['country']
amd_sector = amd['sector']

amd_stock_data = amd_obj.history(period="max")
# amd_stock_data['Volume]


