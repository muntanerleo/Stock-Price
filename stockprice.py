# simple data driven web app with a few lines of code

# i will be using the python library called streamlit to make this simple web app

# Streamlit is an open-source app framework built specifically for Machine Learning and Data Science projects.

import yfinance as yf
import streamlit as st
import pandas as pd

# this will be the header for the web application 
# the "#" indicates that the contents are a heading. the '**' make the words bold.
st.write("""
# Simple Stock Price App

Here is the stock **closing price** and **volume** of **Apple!**

""")

# i extracted some lines from the below article
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

# the line below defines the ticker symbol for google
tickerSymbol = 'AAPL'

# now this lines retrieves the data on the ticker
tickerData = yf.Ticker(tickerSymbol)

# this line will get the historical stock prices for the ticker and save it into the dataframe
# Note: currently there is an issue between yfinance and pandas 1.4, resulting in a traceback error:
# 'Index' object has no attribute 'tz_localize'. 

# there are two solutions: 1. downgrade to pandas 1.35 or 2. use period='max' then filter the data using pandas.

# i went with solution 2 as you can see in the code below:
tickerdataf = tickerData.history(period='max')
tickerdataf = tickerdataf.loc['2018-01-01':'2018-01-31']

st.write("""
## Closing Price
""")
# in the web app i will show two line charts. the first will be the closing price 
st.line_chart(tickerdataf.Close)

st.write("""
## Volume Price
""")
# the second one will be the volume
st.line_chart(tickerdataf.Volume)