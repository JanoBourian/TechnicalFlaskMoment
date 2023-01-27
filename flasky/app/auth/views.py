from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .. import db
from .forms import LoginForm, RegistrationForms
import datetime

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember =  form.remember_me.data, duration = datetime.timedelta(hours=4))
            next_arg = request.args.get("next")
            if next_arg is None or not next_arg.startswith("/"):
                next_arg = url_for("main.index")
            return redirect(next_arg)
        flash("Invalid username or password")
    return render_template("/auth/login.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for("main.index"))

@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForms()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You can now login")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)