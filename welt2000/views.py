from flask import render_template
from welt2000 import app


@app.route('/')
def index():
    return render_template('index.jinja')


@app.route('/contribute')
def contribute():
    return render_template('contribute.jinja')


@app.route('/references')
def references():
    return render_template('references.jinja')
