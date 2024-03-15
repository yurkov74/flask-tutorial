"""
Simplest single-file flask app.
"""
from flask import Flask


"""
A Flask application is an instance of the Flask class. Everything about the \
  application, such as configuration and URLs, will be registered with this \
  class.

The most straightforward way to create a Flask application is to create a \
  global Flask instance directly at the top of your code.
"""
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
