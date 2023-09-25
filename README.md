# YFinance > 0.2.28 support in Community Cloud

yfinance changed the default behavior in version 0.2.29 to cache timezone info to
improve performance. However, the default place it tries to save the cache is not
writeable on Streamlit Community Cloud.

You can get around this issue and still use the latest versions of yfinance by setting
a different cache directory than the default one, like this:

```python
import yfinance as yf

yf.set_tz_cache_location(".cache")
```

This puts the timezone cache in a new folder inside the current folder, called .cache

```
streamlit_app.py
.cache/
   tkr-tz.db
```

`.cache` isn't really special, but it's a writable location -- you can name the folder
whatever you want.
