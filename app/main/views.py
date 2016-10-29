from . import main
from flask import render_template

@main.route('/')
def hello_world():
    return "<h1>Hello world</h1>"
