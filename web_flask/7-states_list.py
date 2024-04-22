#!/usr/bin/python3
""" Starts a web application"""


from models.state import State
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with state objects present in DBStorage"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown(self):
    """removes currrent sqlachemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
