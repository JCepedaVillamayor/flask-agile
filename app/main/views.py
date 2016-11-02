from . import main
from flask import render_template, flash

@main.route('/')
def hello_world():
    flash("oops, there are no forms here!")
    return render_template('index.html')
