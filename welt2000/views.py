from welt2000 import app


@app.route('/')
def hello_world():
    return 'Hello World!'
