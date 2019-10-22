#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file name :'flasky.py'
# created on:'2018/11/8'
import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

__author__ = 'turbobin'

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
def test():
    """run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
