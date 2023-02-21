import os 
from flask import render_template
from flask_mail import Message
from threading import Thread
from . import mail 

## Mail send()
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
        
def send_email_thread(to, subject, template, **kwargs):
    msg = Message(
        os.getenv.get("FLASKY_MAIL_SUBJECT_PREFIX")+ subject,
        sender = os.getenv.get("FLASKY_MAIL_SENDER"),
        recipients = [to]
        )
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

def send_email(to, subject, template, **kwargs):
    msg = Message(
        os.environ.get("FLASKY_MAIL_SUBJECT_PREFIX")+ subject,
        sender = os.environ.get("FLASKY_MAIL_SENDER"),
        recipients = [to]
        )
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    mail.send(msg)