import sqlite3
import short_url
from flask import Flask, render_template, request, g

app = Flask(__name__)
DATABASE = './urls.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('urls.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            first_url = 'pybit.es/' + short_url.encode_url(1)
            db.cursor().execute(f"""INSERT INTO urls(short, full)
                                    VALUES('{first_url}', 'http://example.com');""")
        db.commit()


def get_last_record_id():
    most_recent_record = query_db('SELECT * FROM urls ORDER BY id DESC;', one=True)
    return most_recent_record['id']


@app.route('/')
def index(url=None, link=None, all_links=None):
    # if request.method == 'GET':
    return render_template('index.html',
                           all_links=[link for link in query_db('select * from urls')])


@app.route('/shorten', methods=['POST'])
def shorten():
    raw_url = request.form.get("raw_url")
    cur_id = get_last_record_id()
    short = 'pybit.es/' + short_url.encode_url(cur_id + 1)
    db = get_db()
    db.cursor().execute(f"INSERT INTO urls(short, full) VALUES('{short}', '{raw_url}');")
    db.commit()
    return render_template('index.html', url=short, link=raw_url,
                           all_links=[link for link in query_db('select * from urls')])


if __name__ == '__main__':
    app.run(debug=True)
