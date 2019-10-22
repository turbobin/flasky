#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file name :'__init__.py.py'
# created on:'2018/11/8'
__author__ = 'turbobin'

from flask import Blueprint

main = Blueprint('main', __name__)      # 第一个参数是蓝本名，也是一个蓝本命名空间; 第二个参数是蓝本所在的包或模块

from . import views, errors