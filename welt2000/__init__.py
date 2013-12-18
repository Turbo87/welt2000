from flask import Flask


app = Flask(__name__)
from welt2000 import views  # noqa
