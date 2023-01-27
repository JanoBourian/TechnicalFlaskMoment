from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Length(1, 64), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    recaptcha = RecaptchaField()
    submit = SubmitField("Log in")
    ## Remember a captcha space
