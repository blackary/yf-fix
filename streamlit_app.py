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

st.write("This has been fixed in the latest pre-release of yfinance.")
st.code("pip install yfinance>=0.2.31b2")

msft = yf.Ticker("MSFT")

hist = msft.history(period="1mo")

st.write(hist)

with st.expander("Old fix"):
    st.markdown(Path("README.md").read_text())
