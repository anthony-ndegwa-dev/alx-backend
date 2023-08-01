#!/usr/bin/env python3
"""Use _ or gettext function to parametrize your templates. Use message IDs
home_title and home_header.

Create a babel.cfg file containing
  [python: **.py]
  [jinja2: **/templates/**.html]
  extensions=jinja2.ext.autoescape,jinja2.ext.with_

Initialize your translations: $ pybabel extract -F babel.cfg -o messages.pot
and your two dictionaries with
  $ pybabel init -i messages.pot -d translations -l en
  $ pybabel init -i messages.pot -d translations -l fr

Edit files translations/[en|fr]/LC_MESSAGES/messages.po to provide correct
value for each message ID for each language. Use the following translations:
  msgid 	         English                French
  home_title 	  "Welcome to Holberton" 	"Bienvenue chez Holberton"
  home_header 	  "Hello world!"             "Bonjour monde!"

Then compile your dictionaries with

$ pybabel compile -d translations

Reload the page of your app and make sure that the correct messages show up.
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
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page."""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
