from pathlib import Path

_ = """
import appdirs as ad

CACHE_DIR = ".cache"

# Force appdirs to say that the cache dir is .cache
ad.user_cache_dir = lambda *args: CACHE_DIR

# Create the cache dir if it doesn't exist
Path(CACHE_DIR).mkdir(exist_ok=True)
"""

import yfinance as yf
import streamlit as st

msft = yf.Ticker("MSFT")

hist = msft.history(period="1mo")

st.write(hist)

st.markdown(Path("README.md").read_text())
