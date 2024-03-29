import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

app = create_app(os.environ.get("FLASK_CONFIGURATION"))
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.cli.command()
def test():
    """ Run the unittest """
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)