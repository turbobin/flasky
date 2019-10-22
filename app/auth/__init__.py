#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file name :'__init__.py.py'
# created on:'2018/11/9'
__author__ = 'turbobin'

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views