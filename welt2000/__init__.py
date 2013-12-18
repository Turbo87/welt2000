from flask import Flask, request
from flask.ext.babel import Babel

from welt2000.__about__ import (
    __title__, __summary__, __uri__, __version__, __author__, __email__,
    __license__,
)  # noqa


app = Flask(__name__)
babel = Babel(app)

translations = ['en']
translations.extend(map(str, babel.list_translations()))


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(translations)


from welt2000 import views  # noqa
