#!/usr/bin/python3
""" Starts a web application"""


from models.state import State
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities():
    """display a HTML page with city objects linked to state"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(self):
    """removes currrent sqlachemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
