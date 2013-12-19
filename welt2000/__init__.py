from flask import Flask, request, session, current_app
from flask.ext.babel import Babel
from babel.core import negotiate_locale

from welt2000.__about__ import (
    __title__, __summary__, __uri__, __version__, __author__, __email__,
    __license__,
)  # noqa


app = Flask(__name__)
app.secret_key = '1234567890'

babel = Babel(app)


@app.template_global()
@babel.localeselector
def get_locale():
    available = ['en']
    available.extend(map(str, current_app.babel_instance.list_translations()))

    lang = session.get('lang')
    if lang and lang in available:
        return lang

    preferred = map(lambda l: l[0], request.accept_languages)
    return negotiate_locale(preferred, available)


from welt2000 import views  # noqa
