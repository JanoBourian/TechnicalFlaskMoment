from flask import (
    Flask,
    request,
    g,
    make_response,
    redirect,
    Response,
    render_template,
    url_for,
    session,
    flash,
)
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import logging
from configuration_info import CONFIGURATION
from custom_forms import NameForm

app = Flask(__name__)
app.config.update(**CONFIGURATION)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

## Models
class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return f"<Role {self.name}>"


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return f"<User {self.username}>"


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


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
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
        else:
            session["known"] = True
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for("index"))
    return render_template(
        "form.html",
        form=form,
        name=session.get("name", ""),
        known=session.get("known", ""),
    )


@app.errorhandler(404)
def page_not_found(e) -> Response:
    return make_response({"message": f"{e}"}, 404)


@app.errorhandler(500)
def page_not_found(e) -> Response:
    return make_response({"message": f"{e}"}, 500)
