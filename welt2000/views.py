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


@app.route('/contribute/data')
def contribute_data():
    return render_template('contribute-data.jinja')


@app.route('/downloads')
def downloads():
    return render_template('downloads.jinja')


@app.route('/references')
def references():
    return render_template('references.jinja')


@app.route('/faq')
def faq():
    return render_template('faq.jinja')


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


@app.route('/legal-terms/contribution')
def legal_contribution():
    return render_template('legal-terms-contribution.jinja')


@app.route('/legal-terms/contributor-terms')
def legal_contributor_terms():
    return render_template('legal-terms-contributor-terms.jinja')


@app.route('/legal-terms/terms-of-use')
def legal_terms_of_use():
    return render_template('legal-terms-terms-of-use.jinja')


@app.route('/legal-terms/privacy-policy')
def legal_privacy_policy():
    return render_template('legal-terms-privacy-policy.jinja')


@app.route('/legal-terms/website')
def legal_website():
    return render_template('legal-terms-website.jinja')


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
