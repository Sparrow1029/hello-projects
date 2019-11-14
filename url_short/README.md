# Url shortener project built with flask and sqlite3
### Super simple URL shortener service with db mapping to full URLs
From PyBites code challenge #61: [Build a URL Shortener](https://pybit.es/codechallenge61.html)

* requires SQLite3 to be installed.
```
$ cd url_short
$ mkvirtualenv urls
(urls) $ pip install -r requirements.txt
(urls) $ export FLASK_APP=shortener.py
(urls) $ flask shell
>>> from shortener import init_db
>>> init_db()
>>> exit()
(urls) $ flask run
```
