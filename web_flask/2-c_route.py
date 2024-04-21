#!/usr/bin/python3
""" Starts a web application and adds another route"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """returns Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """displays C followed by value of text"""
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
