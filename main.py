from flask import Flask, request, g, make_response, redirect
import logging 

app = Flask(__name__)

@app.route("/")
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
    response = make_response("<h1> Hello, Flask! Your User-Agent is: {}</h1>".format(user_agent))
    response.set_cookie('answer', '42')
    response.status_code = 200
    return response

@app.route("/user/<name>")
def user(name:str) -> str:
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
    response = make_response("<h1> Hello, {}! Your User-Agent is: {}</h1>".format(name, user_agent))
    response.set_cookie(name, '42')
    response.status_code = 200
    return response

