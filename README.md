# TechnicalFlaskMoment
A little approach and brief with Flask and its Features from a REST API perspective.

# Index
- [Configured and started](#section1)
- [All packages](#section2)
- [All imports](#section3)
- [About Flask](#section4)
    - [Flask context](#section4-1)
- [Request Object](#section5)
    - [Request Attributes or methods](#section5-1)
    - [Request Hooks](#section5-2)
- [Response Object](#section6)
    - [Response Attributes or methods](#section6-1)
    - [Redirect and Abort](#section6-2)
- [Templates](#section7)
    - [Jinja Template](#section7-1)
        - [Filters](#section7-1-1)
        - [Control Structures](#section7-1-2)
    - [Bootstrap Integration](#section7-2)
    - [Custom Error Pages](#section7-3)
    - [Links](#section7-4)
    - [Static Files](#section7-5)
    - [Dates and times](#section7-6)
- [Web Forms](#section8)
    - [Configuration](#section8-1)
    - [Form Classes](#section8-2)
    - [HTML Rendering of Forms](#section8-3)
    - [Form Handling in View Functions](#section8-4)
    - [Redirects and User Sessions](#section8-5)
    - [Message Flashing](#section8-6)
- [Databases](#section9)
    - [SQL Databases](#section9-1)
    - [NoSQL Databases](#section9-2)
    - [SQL or NoSQL?](#section9-3)
    - [Python Database Frameworks](#section9-4)
    - [Database Management With Flask-SQLAlchemy](#section9-5)
    - [Model definition](#section9-6)
    - [Relationships](#section9-7)
    - [Database Operations](#section9-8)
    - [Database Use in VIew Functions](#section9-9)
    - [Integration with the Python Shell](#section9-10)
    - [Database Migrations with Flask-Migrate](#section9-11)
- [Email](#section10)
    - [Email Support with Flask-Mail](#section10-1)
    - [Sending Email from the Python Shell](#section10-2)
    - [Integration Emails with the Application](#section10-3)
    - [Sending Asyncronous Email](#section10-4)
- [Large Application Structure](#section11)
    - [Configuration options](#section11-1)
    - [Application packages](#section11-2)
        - [Using an application factory](#section11-3)
        - [Implementing application functionality in a Blueprint](#section11-4)
    - [Application Script](#section11-5)
    - [Requirements file](#section11-6)
    - [Unit Test](#section11-7)
    - [Database setup](#section11-8)
    - [Running the application](#section11-9)
- [User Authentication](#section12)
- [User Roles](#section13)
- [User Profiles](#section14)
- [Blog Posts](#section15)
- [Followers](#section16)
- [User Comments](#section17)
- [Application Programming Interfaces](#section18)
- [Testing](#section19)
- [Performance](#section20)
- [Deployment](#section21)
- [Additional resources](#section22)


<div id="section1"></div>

# Configured and started

## First steps

Always, before all, we need to create a virtual environment and the most easy way to do it is with venv (included in python), after that we need to activate the virtual environment and the next step is to have a requeriments.txt file

```bash
python -m venv flask
flask\Scripts\activate.bat
pip install black
pip freeze > requirements.txt
```

## Set for the first execution

```bash
set FLASK_APP=main.py
set FLASK_DEBUG=1
flask run
```

## Get help

```bash
flask --help
```

## Another options

In this case we can use other flags as: --reload, --no-reload, --debugger and --no-debugger.

```bash
flask run --host 0.0.0.0
```

<div id="section2"></div>

# All packages

```bash
black
flask
flask-bootstrap
flask-moment
flask-sqlalchemy
flask-wtf
python-dotenv
flask-migrate
flask-mail
```

<div id="section3"></div>

# All imports

```python
from flask import Flask
from flask import request
from flask import current_app
from flask import g
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask_moment import Moment
from flask import url_for
from flask import session
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_mail import Message
```

<div id="section4"></div>

# About Flask

<div id="section4-1"></div>

## Flask context

We have two context in Flask: application context and the request context:

- current_app: The application instance for the active application
- g: An temporary object. This variable is reset with each request
- request: It encapsulates the contents of an HTTP request
- session: A dictionary that the application can use to store values.

Some useful statements are:
```python
app.context_app()
app.name
app.url_map
```

<div id="section5"></div>

# Request Object

This is the object that contains all information sent by our client in the HTTP request.

<div id="section5-1"></div>

## Request Attributes or methods

- **form**: A dictionary eith all the form fields submitted with the request
- **args**: A dictionary with all the arguments passed in the query string of the URL
- **values**: A dictionary that combines the values in form and args
- **cookies**: A dictionary with all the cookies included in the request.
- **headers**: A dictionary with all the HTTP headers included in the request.
- **files**: A dictionary with all the file uploads included with the request
- **get_data()**: Returns the buffered data from the request body
- **get_json()**: Returns a Python dictionary with the parsed JSON included in the body of the request
- **blueprint**: 
- **endpoint**: The name of the Flask endpoint
- **method**: The HTTP method
- **scheme**: The URL scheme (HTTP or HTTPS)
- **is_secure()**: Return true if the request came through a secure HTTPS
- **host**: The host defined in the request
- **path**: The path portion of the URL
- **query_string**: The query string portion of the URL, as a raw binary value.
- **full_path**: The path and query string
- **url**: The complete URL
- **base_url**: Same as url, but without the query string component
- **remote_addr**: The IP Address of the client
- **environ**: The raw WSGI environment dictionary for the request

<div id="section5-2"></div>

## Request Hooks

The hooks are functions that start in a specific moment in the request process. 

- **before_request**: Occurs before each request
- **before_first_request**: Occurs only in the first request, here we can put the database built.
- **after_request**: After each request if no unhandled exception ocurred
- **teardown_request**: Is a function to run after each request, even if unhandled exceptions ocurred.

<div id="section6"></div>

# Response Object

Response object is the object that flask returns after a request or like a result of a request. 

<div id="section6-1"></div>

## Response Attributes or methods

- **status_code**: The numeric HTTP status code
- **headers**: A dictionary object
- **set_cookie()**: Adds a cookie to the response
- **delete_cookie()**: jejeje
- **content_length**: 
- **content_type**: The media type of the response body
- **set_data()**: Sets the response body as a string or bytes value
- **get_data()**: Gets the response body

<div id="section6-2"></div>

## Redirect and Abort

```python
from flask import redirect
from flask import abort
# a lot of code
@app.route("/user/<user:int>")
def index(user:int):
    if (user == 0):
        abort(404)
    else:
        redirect("https://wwww.google.com.mx")
```

<div id="section7"></div>

# Templates

The process where Flask replaces the variables with actual values and returns a final response string is called __rendering__

<div id="section7-1"></div>

## Jinja Template

The directory for our templates is called templates, inside that template we can put the html code. If you need more information about Jinja2 Templates please visit https://jinja.palletsprojects.com/en/3.1.x/

- render_template
- variable: {{name}}

<div id="section7-1-1"></div>

### Filters

- safe: Renders the value without applying escaping
- striptags: Removes any HTML tags from the value before rendering
- capitalize: 
- lower:
- upper:
- title:
- trim:

<div id="section7-1-2"></div>

### Control Structure

You can remind that we have some statements for control flux as conditionals and loops. Below you can see twice examples.

#### If statement
```python
{% if user%}
    Hello {{user}}!
{% else %}
    Hello stranger!
{% endif %}
```

#### For statement
```python
<ul>
    {% for comment in comments %}
        <li> {{comment}} </li>
    {% endfor %}
</ul>
```

#### Macro 

Macros are similar to python functions, but inside of html code. We can put the macros inside a html file named __macros.html__
```python
{% macro render_comment(comment) %}
    <li>{{comment}}</li>
{% endmacro %}
```

```python
<ul>
    {% for comment in comments %}
        {{render_comment(comment)}}
    {% endfor %}
</ul>
```

#### import statement
Import includes in current file the information contents in some other file.
```python
{% import 'macros.html' as macros %}
```

#### extend statement
Is a common way to reuse the templates structure for example the headers, navigation bar, footer or another common information inside the  several templates.
```python
{% include 'base.html' %}
```
#### include statement
```python
{% include "navbar.html" %}
```

#### differences between statements

import -> macro
extends -> base.html
include -> navbar.html

#### block statement
```html
{% block body %}
{% endblock %}
```

<div id="section7-2"></div>

## Bootstrap Integration

For this application I'm not going to install bootstrap directly from pip, I'm gonna use Bootstrap from the html integration. For more information please check the last version for Bootstrap: https://getbootstrap.com/docs/5.0/getting-started/introduction/

<div id="section7-3"></div>

## Custom Error Pages

The custom error pages are important because they respond a some different problems in the application. We can render a html page or we can do other process with the information, for example to save information if we find some error during the execution.

```python
@app.errorhandler(404)
def page_not_found(e) -> Response:
    return make_response({"message": f"{e}"}, 404)

@app.errorhandler(500)
def page_not_found(e) -> Response:
    return make_response({"message": f"{e}"}, 500)
```

<div id="section7-4"></div>

## Links

Links are so useful when we have a dynamic information to link in our templates, for example, if we have a card template for our clients and each client inside of card template has different links, we can add dynamic links.

We have two types or urls: relatives and absolute. Relatives are in our context app, and absolutes are used for connect with external pages. 

- links inside our application
```python
url_for("index") #our function called "index"
```

- dynamic links
```python
<ul>
    {% for d in data %}
        <li>
            <a href="{{url_for('user', name=d.get('name', ''))}}">{{d.get("name", "")}}</a>
        </li>
    {% endfor %}
</ul>
```

<div id="section7-5"></div>

## Static files

We can allow automatically static files inside the directory called __static/__. At this moment is no too much necessary to work with static files. 

<div id="section7-6"></div>

## Dates and times

This is not a trivial problema because exists a lot of people request our page, and they could be around the world, for this reason is important to have a proper way to show dates and hours.

We need to implement it correctly, and we need to write code in two moments in two different parts. First part is inside our __app.py__ file:

```python
from flask_moment import Moment
from datetime import datetime
moment = Moment(app)
...
    return render_template("index.html", data=data, datetime = datetime.utcnow())
```

in our __base.html__ for allow it in all project:
```html
{{ moment.include_moment()}}
{{ moment.locale('es')}}
```

and the next place is in our __.html__ file:

```html
<footer class="text-center">
    <p>The local date and time is {{moment(datetime).format('LLL')}}</p>
    <p>That was {{moment(datetime).fromNow(refresh=True)}}</p>
</footer>
```

Exist other commands for flask-moment:

```js
format()
fromNow()
fromTime()
calendar()
valueOf()
unix()
```

<div id="section8"></div>

# Web Forms

We can start to work with forms through flask request package but is too much interesting and necessary work with __flask-wtf__ 

<div id="section8-1"></div>

## Configuration

Before all we need to set a __SECRET_KEY__ value that will be used as an encryption. 

<div id="section8-2"></div>

## Form Classes

The basic code for a WebForm in Python (using FlaskForm)

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
```

Field types (a long list)

- **BooleanField**: Checkbox with True and False values
- **DateField**: Text Field that accepts a datetime.date value in a given format
- **DateTimeField**: Text Field that accepts a datetime.datime value in a given format
- **DecimalField**: Text field that accepts a decimal.Decimal value
- **FileField**: File upload field
- **HiddenField**: Hidden text field
- **MultiplFileField**: Multiple file upload field
- **FieldList**: List of fields of a given type
- **FloatField**: Text field that accepts a floating-point value
- **FormField**: Form embedded as a field in a container form
- **IntegerField**: Text Field that accepts an integer value
- **PasswordField**: Password text field
- **RadioField**: List of radio buttons
- **SelectField**: Drop-down list of choices
- **SelecMultipleFields**: Drop-down list of choices with multiple selections
- **SubmitField**: Form submissions button
- **StringField**: Text field
- **TextAreaField**: Multiple-line text field 

WTForm validators

- **DataRequired**: Validates that the field contains data after type conversion
- **Email**: Validates an email address
- **EqualTo**: Compares the values of two fields; useful when requesting a password to be entered twice for confirmation
- **InputRequired**: Validates that the field contains data before type conversion
- **IPAdress**: Validates an IPv4 network address
- **Length**: Validates the length of the string entered
- **MacAdress**: Validate a MAC address
- **NumberRange**: Validates that the value entered is within a numeric range
- **Optional**: Allows ampty input field, skippingg additional validators
- **Regexp**: Validates the input agaisnt a regular expression
- **URL**: Validates a URL
- **UUID**: Validates a UUID
- **AnyOf**: Validates that the input is one of a list of possible values
- **NoneOf**: Validates that the input is none of a list of possible values

<div id="section8-3"></div>

## HTML Rendering of Forms

The most basic way to call a form into HTML code:

```html
<form method="POST">
    {{form.hidden_tag()}}
    {{form.name.label}} {{form.name(class="center")}}
    {{form.submit()}}
</form>
```

__{{form.hidden_tag()}}__ provides extra protection against CSRF attacks.

<div id="section8-4"></div>

## Form Handling in View Functions

HTML code:

```html
{% extends 'base.html' %}

{% block title %}
Form | Form
{% endblock %}

{% block body %}

{% if name %}
    <h1 class = "text-center mt-2"> {{name}} </h1>
{% endif %}

<!--
    <h1 class="text-center mt-2"> There is a Form </h1>
    {% if name%}
        <h1 class = "text-center mt-2"> {{name}} </h1>
    {% else %}
        <h1 class = "text-center mt-2"> Stranger! </h1>
    {% endif %}
-->

    <form method="POST" class="text-center mt-4">
        {{form.hidden_tag()}}
        <div class="mb-3">
            <div class="form-label">
                {{form.name.label}}
            </div>
            <div class = "d-flex justify-content-center">
                <div class="col-sm-4">
                    {{form.name(class="form-control form-control-md", placeholder="Your name here")}}
                </div>
            </div>
        </div>
        <div class="mb-3">

        </div>
        {{form.submit(class="btn btn-primary")}}
    </form>
{% endblock %}
```

Python Code:
```python
@app.route("/form", methods=["GET", "POST"])
def user_form():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template("form.html", form=form, name=name)
```
<div id="section8-5"></div>

## Redirects and User Sessions

Browsers repeat the last request they sent when they are asked to refresh a page. At this point we have two problems: we need to implement something for avoid to send a POST method in a refresh and the second one is to keep the information about our user. 

The last version of __main.py__ is:

```python
@app.route("/form", methods=["GET", "POST"])
def user_form():
    form = NameForm()
    if form.validate_on_submit():
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for("index"))
    return render_template("form.html", form=form, name=session.get("name", ""))
```

<div id="section8-6"></div>

## Message Flashing

Now, this is the last version:

```python
@app.route("/form", methods=["GET", "POST"])
def user_form():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name", "")
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for("index"))
    return render_template("form.html", form=form, name=session.get("name", ""))
```

New HTML version (in base.html):
```html

```

<div id="section9"></div>

# Databases

We have two alternatives to develop a store system: SQL or NoSQL databases.

<div id="section9-1"></div>

## SQL Databases

For us is important rember that exist two important columns: **primary_key** and **foreign_key**. The first is to have a unique identifier inside the table and the second is to have a relationships between tables. 

<div id="section9-2"></div>

## NoSQL Databases

This databases use collections instead of tables and documents instead of records. 

<div id="section9-3"></div>

## SQL or NoSQL?

For SQL databases exist an ACID paradigm: Atomicity, Consistency, Isolation and Durability. 

<div id="section9-4"></div>

## Python Database Frameworks

Exists a lot of database engines to work with Flask: **MySQL**, **PostgreSQL**, **SQLite**, **Redis**, **MongoDB**, **CouchDB**, **DynamoDB**

Factors to evaluate when choose one or another database framework:

- Ease of use
- Performance
- Portability
- Flask integration

<div id="section9-5"></div>

## Database Management with Flask-SQLAlchemy

Flask-SQLAlchemy most popular database engines:

- MySQL: mysql://username:password@hostname/database
- Postrges: postgresql://username:password@hostname/database
- SQLite(Linux, macOS): sqlite:////absolute/path/to/database
- SQLite(Windows): sqlite:///c:/absolute/path/to/database

Specific configuration:

```python
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.update(**CONFIGURATION)
moment = Moment(app)
db = SQLAlchemy(app)
```

<div id="section9-6"></div>

## Model Definition

Type name and Python type relationship:

- Integer: int
- SmallInteger: int
- BigInteger: int OR long
- Float: float
- Numeric: decimal.Decimal
- String: str
- Text: str
- Unicode: unicode
- UnicodeText: unicode
- Booleans: bool
- Date: datetime.date
- Time: datetime.time
- DateTime: datetime.datetime
- Interval: datetime.timedelta
- Enum: str
- PickleType: Any Python object
- LargeBinary: str

Specific configuration inside to configuration:

- primary_key
- unique
- index
- nullable
- default

<div id="section9-7"></div>

## Relationship

In this example I show you a one-to-many relationship and how it is implemented:

```python
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref="role")
    
    def __repr__(self):
        return f"<Role {self.name}>"

class User(db.Model):
    __tablename__ = 'users'

    id = db.Columns(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return f"<User {self.username}>"
```

For a relationship configuration we can use:

- backref: Add a back reference in the other model in the relationship
- primaryjoin: Specify the join condition between the two models explicitly. This is necessary only for ambiguous relationships.
- lazy: Specify how the related items are to be loaded. 
- uselist: If set to False, use a scalar instead of a list.
- order_by: Specify the ordering used for the items in the relationship
- secondary: Specify the name of the association table to use in many-to-many relationships.
- secondaryjoin: Specify the secondary join conditions for many-to-many relationships when SQLAlchemy cannot determine it on its own.

<div id="section9-8"></div>

## Database operations

For this section we can create tables using flask console. In root path we can type:

```cmd
flask shell 
from main import db
dir(db)
db.create_all()
db.drop_all()
```
### Inserting Information

```cmd
from main import Role, User
dir(Role)
admin = Role(name="admin")
user = Role(name="user")
user_john = User(username="user_john", role=user)
user_susan = User(username="susan", role=admin)
db.session.add(admin)
db.session.add(user)
db.session.add(user_john)
db.session.add(user_susan)
db.session.commit()
```

And now is available the user.id because that already exist in database.

If you need to check more information you can type, for example: dir(db.session) or dir(db.session.rollback)

### Modifying rows

```cmd
admin.name = "administrator"
db.session.add(admin)
db.session.commit()
```

### Deleting rows

```cmd
db.session.delete(admin)
db.session.commit()
```

### Querying rows

```cmd
dir(Role)
Role.query.all()
User.query.all()
dir(User.query)
User.query.filter_by(role=admin).all()
str(User.query.filter_by(role=admin))
User.query.filter_by(role=admin).first()
```

### Common SQLAlchemy filters

- filter():
- filter_by():
- limit():
- offset():
- order_by():
- gropu_by():

### Most common SQLAlchemy query executors

- all():
- first():
- first_or_404():
- get():
- get_or_404():
- count():
- paginate():

<div id="section9-9"></div>

## Database Use in View Functions

```python
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
    return render_template("form.html", form=form, name=session.get("name", ""), known = session.get("known",""))
```

<div id="section9-10"></div>

## Integration with the Python Shell

If you write the next lines, you can get:

```python
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
```

```cmd
flask shell
app
db
User
Role
```

<div id="section9-11"></div>

## Database Migrations with Flask-Migrate

We can use Database Migrations instead of to delete and create databases again. 

```python
from flask_migrate import Migrate
## 
migrate = Migrate(app, db)
##
```

And now, we can go to the console to see other configurations. Before make some changes is necessary review the next steps:

- Make the necessary changes to the model classes
- Create an automatic migration script with the flask db migrate command
- Review the generated script and adjust it so that it accurately represents the changes that were made to the models
- Add the migration script to source control
- Apply the migration to the database with the flaks db upgrade command

```cmd
flask db init
flask db migrate -m "Inital migration"
flask db upgrade
```

<div id="section10"></div>

# Email

Is a simple way to notify.

<div id="section10-1"></div>

## Email Suuport with Flask-Mail

```cmd
pip install flask-mail
```

Configuration keys:
- MAIL_SERVER (localhost): Hostname or IP address of the email server
- MAIL_PORT (25): Port of the email server
- MAIL_USER_TLS (False): Enable Transport Layer Security (TLS) security
- MAIL_USE_SSL (False): Enable Secure Sockets Layer (SSL) security
- MAIL_USERNAME (None): Mail account username
- MAIL_PASSWORD (None): Mail account password

```python
from flask_mail import Mail
...
mail = Mail(app)
```

<div id="section10-2"></div>

## Sending Email from the Python Shell

```shell
from flask_mail import Message
from main import mail
msg = Message("Test mail", sender="sender@sender.mx",recipients=["recipients@recipients.com"])
msg.body = "This is the plan text body"
msg.html = "This is the <b> HTML </b> body"
with app.app_context():
    mail.send(msg)
```

<div id="section10-3"></div>

## Integrating Email with the Application

```python
## Mail send()
def send_email(to, subject, template, **kwargs):
    msg = Message(
        CONFIGURATION.get("FLASKY_MAIL_SUBJECT_PREFIX")+ subject,
        sender = CONFIGURATION.get("FLASKY_MAIL_SENDER"),
        recipients = [to]
        )
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    mail.send(msg)

...

            if app.config["FLASKY_ADMIN"]:
                send_email(app.config["FLASKY_ADMIN"],
                           "New User",
                           "mail/new_user",
                           user = user
                           )
```

<div id="section10-4"></div>

## Sending Asynchonous Email

```python
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
```

<div id="section11"></div>

# Large Application Structure

The structure suggested is showed below:

* flasky/
    * app/
        * templates/
        * static/
        * main/
            * \_\_init\_\_.py
            * errors.py
            * forms.py
            * views.py
        * \_\_init\_\_.py
        * email.py
        * models.py
        * migrations/
        * tests/
            * \_\_init\_\_.py
            * test*.py
* venv/
* requirements.txt
* config.py
* flasky.py

<div id="section11-1"></div>

## Configuration options

Below is the **configuration.py** script:

```python
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()  # take environment variables from .env.

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") 
    MAIL_SERVER = os.environ.get('MAIL_SERVER') 
    MAIL_PORT = int(os.environ.get("MAIL_PORT")) 
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() 
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") 
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") 
    FLASKY_MAIL_SUBJECT_PREFIX =os.environ.get("FLASKY_MAIL_SUBJECT_PREFIX")  
    FLASKY_MAIL_SENDER = os.environ.get("FLASKY_MAIL_SENDER") 
    FLASKY_ADMIN = os.environ.get("FLASKY_ADMIN") 
    SQLALCHEMY_TRACK_MODIFICATION = os.environ.get("SQLALCHEMY_TRACK_MODIFICATION") 
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")

class IntegrationConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("INT_DATABASE_URI")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI")

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "integration": IntegrationConfig,
    "production": ProductionConfig,
    
    "default": DevelopmentConfig
}
```

<div id="section11-2"></div>

## Application packages

Is where the code, templates, and static files lives. Usually is called **app**

<div id="section11-3"></div>

### Using an application factory

The factory constructor will be inside the app, in */flasky/app/\_\_init\_\_.py*

```python
from flask import Flask, render_template
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name:str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_name)
    
    ## Start the app
    config[config_name].init_app(app)
    
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    ## Attach routes and custom error pages here
    
    return app
```

<div id="section11-4"></div>

### Implementing application functionality in a Blueprint

This imply several configurations, but in little words is about the *main/* file configuration.

<div id="section11-5"></div>

## Application Script

```python
import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

app = create_app(os.environ.get("FLASK_CONFIGURATION"))
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
```

<div id="section11-6"></div>

## Requirements File

<div id="section11-7"></div>

## Unit Test

<div id="section11-8"></div>

## Database setup

<div id="section11-9"></div>

## Running the application

<div id="section12"></div>

# User Authentication

<div id="section13"></div>

# User Roles

<div id="section14"></div>

# User Profiles

<div id="section15"></div>

# Blog Posts

<div id="section16"></div>

# Followers

<div id="section17"></div>

# User Comments

<div id="section18"></div>

# Application Programming Interfaces

<div id="section19"></div>

# Testing

<div id="section20"></div>

# Performance

<div id="section21"></div>

# Deployment

<div id="section22"></div>

# Additonal resources
