from datetime import datetime
from flask import render_template, session, redirect, url_for, request, make_response
from . import main
from .forms import NameForm
from .. import db
from ..models import User 

# @main.route("/", methods=['GET'])
@main.get("/")
def index() -> str:
    user_agent = request.headers.get("User-Agent")
    response = make_response(
        "<h1> Hello, Flask! Your User-Agent is: {}</h1>".format(user_agent)
    )
    response.set_cookie("answer", "42")
    response.status_code = 200
    data = [{"name": "janobourian"}, {"name": "peter"}, {"name": "sysadmin"}]
    return render_template("index.html", data=data, datetime=datetime.utcnow())


@main.route("/user/<name>", methods=["GET"])
def user(name: str) -> str:
    user_agent = request.headers.get("User-Agent")
    response = make_response(
        "<h1> Hello, {}! Your User-Agent is: {}</h1>".format(name, user_agent)
    )
    response.set_cookie(name, "42")
    response.status_code = 200
    data = {"name": name}
    return render_template("user.html", data=data)


@main.route("/form", methods=["GET", "POST"])
def user_form():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
            # if app.config["FLASKY_ADMIN"]:
            #     send_email(app.config["FLASKY_ADMIN"],
            #                "New User",
            #                "mail/new_user",
            #                user = user
            #                )
        else:
            session["known"] = True
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for(".index"))
    return render_template(
        "form.html",
        form=form,
        name=session.get("name", ""),
        known=session.get("known", ""),
    )
