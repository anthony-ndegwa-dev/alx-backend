#!/usr/bin/env python3
"""A basic Flask app, single / route and an index.html template that outputs
“Welcome to Holberton” page title (<title>) and “Hello world” as header (<h1>)
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def get_index() -> str:
    """The home/index page."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
