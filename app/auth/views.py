# -*- coding: utf-8 -*-
# file name :'views.py'
# created on:'2018/11/9'
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .forms import LoginForm, RegisterForm
from ..models import User
from .. import db
from ..email import send_mail

__author__ = 'turbobin'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('该账户未注册！')

        if user and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next_url = request.args.get('next')
            if next_url is None or not next_url.startswith('/'):
                next_url = url_for('main.index')

            return redirect(next_url)

        flash('账户名或密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.username = form.username.data
        user.password = form.password.data

        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail(user.email, '确认账户', 'auth/email/confirm',
                  user=user, token=token)
        # flash('注册成功，请登录！')
        flash('注册确认邮件已发送，请注意查收！')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.indenx'))
    if current_user.confirm(token):
        db.session.commit()
        flash("账户认证成功！")
    else:
        flash("确认链接无效或已过期！")
    return redirect(url_for('main.index'))


@auth.before_app_request
def before_request():
    if (current_user.is_authenticated and not current_user.confirmed
        and request.blueprint != 'auth'
        and request.endpoint != 'static'
    ):
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/confirmed')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_mail(current_user.email, '账户确认',
              'auth/email/confirm', user=current_user, token=token)
    flash('已发送一封新的确认邮件到您的邮箱！')
    return redirect(url_for('main.index'))