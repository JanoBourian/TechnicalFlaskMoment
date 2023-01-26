from flask import Blueprint

main = Blueprint('main', __name__, url_prefix = "/app")

## for avoid circular errors
from . import views, errors 