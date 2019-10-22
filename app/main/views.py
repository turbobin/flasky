#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file name :'views.py'
# created on:'2018/11/8'
from datetime import datetime
from flask import session, redirect, url_for, render_template
from flask_login import login_required

from . import main
from .forms import NameForm
from ..models import User
from .. import db


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data)
        if user is None:
            # user = User(username=form.name.data)
            # db.session.add(user)
            # db.session.commit()
            session['known'] = False
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))     # 省略了蓝本名, main.index
    return render_template('index.html', form=form,
                           name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())


__author__ = 'turbobin'
