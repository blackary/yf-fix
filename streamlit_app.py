import streamlit as st
import yfinance as yf

yf.set_tz_cache_location(".cache")
msft = yf.Ticker("MSFT")

# get historical market data
hist = msft.history(period="1mo")

st.write(hist)
