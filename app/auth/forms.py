#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file name :'forms.py'
# created on:'2018/11/9'
from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo, ValidationError

from ..models import User

__author__ = 'turbobin'


class LoginForm(FlaskForm):
    email = wtforms.StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    remember_me = wtforms.BooleanField('记住我？')
    submit = wtforms.SubmitField('登录')


class RegisterForm(FlaskForm):
    email = wtforms.StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = wtforms.StringField('Username', validators=[DataRequired(), Length(1, 64),
                                                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                  '用户名必须是英文字符开头，且必须是字母、数字、. 或下划线的组合')])
    password = wtforms.PasswordField('Password', validators=[DataRequired(), EqualTo('password2',
                                                                                     message='两次密码输入必须一致！')])
    password2 = wtforms.PasswordField('Password Again', validators=[DataRequired()])
    submit = wtforms.SubmitField('注册')

    def validate_email(self, field):       # 固定写法 validate + 字段名
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册！')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名被使用！')
