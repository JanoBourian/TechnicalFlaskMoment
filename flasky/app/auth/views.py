from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from . import auth
from ..models import User
from .forms import LoginForm
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
