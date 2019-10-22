#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file name :'email.py'
# created on:'2018/11/8'
__author__ = 'turbobin'

from threading import Thread
from . import mail
from flask_mail import Message
from flask import current_app, render_template


def send_email_async(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_email_async, args=[current_app, msg])
    thr.start()
    return thr
