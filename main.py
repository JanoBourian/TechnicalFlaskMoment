from flask import Flask, request, g, make_response, redirect, Response, render_template, url_for, session, flash
from flask_moment import Moment
from datetime import datetime
import logging
from configuration_info import SECRET_KEY
from custom_forms import NameForm 

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

moment = Moment(app)

# @app.route("/", methods=['GET'])
@app.get("/")
def index() -> str:
    user_agent = request.headers.get("User-Agent")
    response = make_response(
        "<h1> Hello, Flask! Your User-Agent is: {}</h1>".format(user_agent)
    )
    response.set_cookie("answer", "42")
    response.status_code = 200
    data = [{"name": "janobourian"}, {"name": "peter"}, {"name": "sysadmin"}]
    return render_template("index.html", data=data, datetime=datetime.utcnow())


@app.route("/user/<name>", methods=["GET"])
def user(name: str) -> str:
    user_agent = request.headers.get("User-Agent")
    response = make_response(
        "<h1> Hello, {}! Your User-Agent is: {}</h1>".format(name, user_agent)
    )
    response.set_cookie(name, "42")
    response.status_code = 200
    data = {"name": name}
    return render_template("user.html", data=data)

@app.route("/form", methods=["GET", "POST"])
def user_form():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name", "")
        if old_name is not None and old_name != form.name.data:
            flash("You have changed your name!")
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for("index"))
    return render_template("form.html", form=form, name=session.get("name", ""))

@app.errorhandler(404)
def page_not_found(e) -> Response:
    return make_response({"message": f"{e}"}, 404)


@app.errorhandler(500)
def page_not_found(e) -> Response:
    return make_response({"message": f"{e}"}, 500)
