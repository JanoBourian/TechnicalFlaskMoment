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
from flask_mail import Mail, Message
from datetime import datetime
import logging
from configuration_info import CONFIGURATION
from custom_forms import NameForm
from threading import Thread

app = Flask(__name__)
app.config.update(**CONFIGURATION)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

## Mail send()
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
        
def send_email(to, subject, template, **kwargs):
    msg = Message(
        CONFIGURATION.get("FLASKY_MAIL_SUBJECT_PREFIX")+ subject,
        sender = CONFIGURATION.get("FLASKY_MAIL_SENDER"),
        recipients = [to]
        )
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

