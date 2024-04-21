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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
