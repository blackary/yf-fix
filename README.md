# YFinance > 0.2.28 support in Community Cloud

yfinance changed the default behavior in version 0.2.29 to cache timezone info to
improve performance. However, the default place it tries to save the cache
(`'/home/appuser/.cache/`) doesn't exist on Streamlit Community Cloud.

You can get around this issue and still use the latest versions of yfinance by setting
a different cache directory than the default one, like this:

```python
from pathlib import Path

import appdirs as ad

CACHE_DIR = ".cache"

# Force appdirs to say that the cache dir is .cache
ad.user_cache_dir = lambda *args: CACHE_DIR

# Create the cache dir if it doesn't exist
Path(CACHE_DIR).mkdir(exist_ok=True)
```

This puts the timezone cache in a new folder inside the current folder, called .cache

```
streamlit_app.py
.cache/
  py-yfinance/
    tkr-tz.db
```

`.cache` isn't really special, but it's a writable location -- you can name the folder
whatever you want.

This bug has been reported here https://github.com/ranaroussi/yfinance/issues/1700

Alternatively, you can set `yfinance==0.2.28` in your requirements.txt to avoid this
issue.
