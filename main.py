from flask import Flask, request
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
    user_agent = request.headers.get("User-Agent")
    return "<h1> Hello, Flask! Your User-Agent is: {}</h1>".format(user_agent)

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
    user_agent = request.headers.get("User-Agent")
    return "<h1> Hello, {}! Your User-Agent is: {}</h1>".format(name, user_agent)

