#!/usr/bin/env python3
"""Implement a way to force particular locale by passing locale=fr parameter
to your app’s URLs.

In get_locale function, detect if incoming request contains locale argument
and if value is a supported locale, return it. If not or the parameter is not
present, resort to the previous default behavior.

Test different translations by visiting http://127.0.0.1:5000?locale=[fr|en]

Visiting http://127.0.0.1:5000/?locale=fr should display this level 1 heading
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page."""
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
