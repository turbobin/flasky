#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file name :'forms.py'
# created on:'2018/11/8'
__author__ = 'turbobin'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('提交')
