from flask import Flask, request, g, make_response, redirect, Response, render_template
from flask_moment import Moment
from datetime import datetime
import logging

app = Flask(__name__)
moment = Moment(app)

# @app.route("/", methods=['GET'])
@app.get("/")
def index() -> str:
    logging.warning(app.app_context())
    logging.warning(app.name)
    logging.warning(app.url_map)
    logging.warning(request.endpoint)
    logging.warning(request.host)
    logging.warning(request.query_string)
    logging.warning(request.remote_addr)
    logging.warning(request.environ)
    logging.warning(g)
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
    logging.warning(app.app_context())
    logging.warning(app.name)
    logging.warning(app.url_map)
    logging.warning(request.endpoint)
    logging.warning(request.host)
    logging.warning(request.query_string)
    logging.warning(request.remote_addr)
    logging.warning(request.environ)
    logging.warning(g)
    user_agent = request.headers.get("User-Agent")
    response = make_response(
        "<h1> Hello, {}! Your User-Agent is: {}</h1>".format(name, user_agent)
    )
    response.set_cookie(name, "42")
    response.status_code = 200
    data = {"name": name}
    return render_template("user.html", data=data)


@app.errorhandler(404)
def page_not_found(e) -> Response:
    return make_response({"message": f"{e}"}, 404)


@app.errorhandler(500)
def page_not_found(e) -> Response:
    return make_response({"message": f"{e}"}, 500)
