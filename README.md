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
- [Databases](#section9)
- [Email](#section10)
- [Large Application Structure](#section11)

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

<div id="section9"></div>

# Databases

<div id="section10"></div>

# Email