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