#!/usr/bin/env python

from flask.ext.script import Manager

from welt2000 import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
