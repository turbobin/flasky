#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file name :'errors.py'
# created on:'2018/11/8'
__author__ = 'turbobin'

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def page_error(e):
    return render_template('500.html'), 500
