from flask import Flask

app = Flask(__name__)

@app.route("/")
def index() -> str:
    return "<h1> Hello, Flask! </h1>"

@app.route("/user/<name>")
def user(name:str) -> str:
    return "<h1> Hello, {}!</h1>".format(name)

