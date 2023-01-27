from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Length(1, 64), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    # recaptcha = RecaptchaField()
    submit = SubmitField("Log in")
    ## Remember a captcha space

class RegistrationForms(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
    email = StringField("Email", validators = [DataRequired(), Length(1, 64), Email()])
    password = PasswordField("Password", validators = [DataRequired(), EqualTo('password2', message = 'Password must match.')])
    password2 = PasswordField("Confirm password", validators = [DataRequired()])
    # recaptcha = RecaptchaField()
    submit = SubmitField("Register")
           
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already registered")
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered")