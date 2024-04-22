#!/usr/bin/python3
""" Starts a web application and adds another route and renders template"""


from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """displays Python followed by text, replaces _ with space"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def display_int(n):
    """displays n is a number only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n=None):
    """ display a HTML page only if n is an integer"""
    if isinstance(n, int)
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n=None):
    """displays HTML page if n is even or odd"""
    if isinstance(n, int):
        if n % 2:
            even_odd = "odd"
        else:
            even_odd = "even"
        return render_template("6-number_odd_or_even.html", n=n, even_odd=even_odd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
