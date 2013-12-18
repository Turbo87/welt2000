from flask import render_template
from welt2000 import app


@app.route('/')
def hello_world():
    return render_template('index.jinja')
