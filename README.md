# TechnicalFlaskMoment
A little approach and brief with Flask and its Features from a REST API perspective.

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