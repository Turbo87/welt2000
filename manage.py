#!/usr/bin/env python

from flask.ext.script import Manager

from welt2000 import app
from welt2000.commands import babel_manager

manager = Manager(app)
manager.add_command("babel", babel_manager)

if __name__ == "__main__":
    manager.run()
