from flask import render_template, request, session, redirect, url_for
from welt2000 import app


@app.route('/')
def index():
    return render_template('index.jinja')


@app.route('/news/updates.xml')
def news_updates_xml():
    return not_available()


@app.route('/contribute')
def contribute():
    return render_template('contribute.jinja')


@app.route('/references')
def references():
    return render_template('references.jinja')


@app.route('/history')
def history():
    return render_template('history.jinja')


@app.route('/obituary')
def obituary():
    return render_template('obituary.jinja')


@app.route('/contact')
def contact():
    return render_template('contact.jinja')


@app.route('/legal-terms')
def legal_terms():
    return render_template('legal-terms.jinja')


@app.route('/rss')
def rss():
    return render_template('rss.jinja')


@app.route('/about')
def about():
    return render_template('about.jinja')


@app.route('/404')
def not_available():
    return render_template('not-available.jinja')


@app.route('/lang/<lang>')
def lang(lang):
    session['lang'] = lang
    return redirect(request.referrer or url_for('index'))
